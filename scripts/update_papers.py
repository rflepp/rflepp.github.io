import os
import re
import json
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET

# Configuration
ARXIV_AUTHOR_NAME = "Roman Flepp"
PAPERS_JSON_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "assets", "data", "papers.json"
)

# Map common arXiv categories to user-friendly titles
CATEGORY_MAP = {
    "cs.CV": "Computer Vision",
    "cs.LG": "Machine Learning",
    "cs.AI": "Artificial Intelligence",
    "eess.IV": "Medical Imaging",
    "cs.RO": "Robotics"
}

def clean_text(text):
    if not text:
        return ""
    # Replace newlines, tabs and multiple spaces with a single space
    return re.sub(r'\s+', ' ', text).strip()

def get_arxiv_id(raw_id):
    # Extract the base arXiv ID (e.g. 'http://arxiv.org/abs/2606.03893v1' -> '2606.03893')
    match = re.search(r'abs/([^v\s]+)', raw_id)
    if match:
        return match.group(1)
    return raw_id

def fetch_arxiv_papers(author_name):
    query = f'au:"{author_name}"'
    encoded_query = urllib.parse.quote(query)
    url = f'http://export.arxiv.org/api/query?search_query={encoded_query}&sortBy=submittedDate&sortOrder=descending'
    
    print(f"Fetching publications from arXiv API: {url}")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            xml_data = response.read()
        return xml_data
    except Exception as e:
        print(f"Error fetching from arXiv: {e}")
        return None

def parse_arxiv_xml(xml_data):
    if not xml_data:
        return []
    
    namespaces = {
        'atom': 'http://www.w3.org/2005/Atom',
        'arxiv': 'http://arxiv.org/schemas/atom'
    }
    
    try:
        root = ET.fromstring(xml_data)
    except Exception as e:
        print(f"Error parsing XML: {e}")
        return []
        
    entries = []
    for entry in root.findall('atom:entry', namespaces):
        raw_id = entry.find('atom:id', namespaces).text
        base_id = get_arxiv_id(raw_id)
        
        title = clean_text(entry.find('atom:title', namespaces).text)
        abstract = clean_text(entry.find('atom:summary', namespaces).text)
        
        # Get publish year
        published = entry.find('atom:published', namespaces).text
        year = published[:4] if published else "2026"
        
        # Get category
        category = "Medical Imaging" # Default fallback
        primary_category_elem = entry.find('arxiv:primary_category', namespaces)
        if primary_category_elem is not None:
            term = primary_category_elem.attrib.get('term', '')
            category = CATEGORY_MAP.get(term, term)
        
        # Build standard venue format
        venue = f"arXiv {year} • {category}"
        
        # Links
        links = [
            {
                "text": "Read on arXiv",
                "url": f"https://arxiv.org/abs/{base_id}"
            }
        ]
        
        entries.append({
            "id": base_id,
            "title": title,
            "venue": venue,
            "abstract": abstract,
            "links": links
        })
        
    return entries

def generate_summary(title, abstract, api_key):
    if not api_key:
        print("No GEMINI_API_KEY found. Falling back to truncated abstract.")
        # Fallback to the first sentence of the abstract, up to 180 chars
        first_sentence = abstract.split('.')[0] + '.'
        if len(first_sentence) > 180:
            first_sentence = first_sentence[:177] + "..."
        return first_sentence, False

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key={api_key}"
    prompt = (
        f"You are a professional research assistant.\n"
        f"Summarize the following computer vision/medical imaging paper abstract into a few concise, professional sentences for a researcher's portfolio website.\n"
        f"Focus on the primary contribution or method. Write in third-person, active voice, and do not use marketing fluff.\n\n"
        f"Paper Title: {title}\n"
        f"Abstract: {abstract}"
    )
    
    payload = {
        "contents": [{
            "parts": [{
                "text": prompt
            }]
        }],
        "generationConfig": {
            "temperature": 0.2,
            "maxOutputTokens": 150
        }
    }
    
    try:
        data = json.dumps(payload).encode('utf-8')
        req = urllib.request.Request(
            url, 
            data=data, 
            headers={'Content-Type': 'application/json'}
        )
        with urllib.request.urlopen(req, timeout=15) as response:
            res_data = json.loads(response.read().decode('utf-8'))
            summary = res_data['candidates'][0]['content']['parts'][0]['text'].strip()
            summary = summary.replace('"', '').replace('`', '').strip()
            return summary, True
    except Exception as e:
        print(f"Error calling Gemini API: {e}")
        # Fallback
        first_sentence = abstract.split('.')[0] + '.'
        if len(first_sentence) > 180:
            first_sentence = first_sentence[:177] + "..."
        return first_sentence, False

def main():
    api_key = os.environ.get("GEMINI_API_KEY")
    
    # 1. Load existing papers
    if os.path.exists(PAPERS_JSON_PATH):
        with open(PAPERS_JSON_PATH, 'r', encoding='utf-8') as f:
            try:
                papers = json.load(f)
            except Exception:
                papers = []
    else:
        papers = []
        
    existing_papers_map = {p.get("id"): p for p in papers if "id" in p}
    print(f"Loaded {len(papers)} existing papers from papers.json.")

    # 2. Fetch papers from arXiv
    xml_data = fetch_arxiv_papers(ARXIV_AUTHOR_NAME)
    arxiv_entries = parse_arxiv_xml(xml_data)
    
    changes_made = False
    for entry in reversed(arxiv_entries): # Process oldest to newest
        paper_id = entry["id"]
        
        # Check if paper already exists
        existing_paper = existing_papers_map.get(paper_id)
        
        if existing_paper is not None:
            # If it already has an AI summary, or we don't have an API key to update it, skip.
            if existing_paper.get("ai_generated") is True or not api_key:
                continue
                
            print(f"\nUpdating summary for existing paper: {entry['title']} (ID: {paper_id})")
            print("Generating short summary using Gemini...")
            summary, is_ai = generate_summary(entry["title"], entry["abstract"], api_key)
            print(f"Summary: {summary}")
            
            existing_paper["summary"] = summary
            existing_paper["ai_generated"] = is_ai
            existing_paper["venue"] = entry["venue"]
            changes_made = True
            
        else:
            # Completely new paper
            print(f"\nNew paper found: {entry['title']} (ID: {paper_id})")
            print("Generating short summary using Gemini...")
            summary, is_ai = generate_summary(entry["title"], entry["abstract"], api_key)
            print(f"Summary: {summary}")
            
            new_paper = {
                "id": paper_id,
                "title": entry["title"],
                "venue": entry["venue"],
                "summary": summary,
                "ai_generated": is_ai,
                "links": entry["links"]
            }
            
            papers.insert(0, new_paper)
            existing_papers_map[paper_id] = new_paper
            changes_made = True

    # 3. Save updated papers back to JSON
    if changes_made:
        os.makedirs(os.path.dirname(PAPERS_JSON_PATH), exist_ok=True)
        with open(PAPERS_JSON_PATH, 'w', encoding='utf-8') as f:
            json.dump(papers, f, indent=2, ensure_ascii=False)
        print(f"\nSuccessfully updated papers and saved to {PAPERS_JSON_PATH}.")
    else:
        print("\nNo updates needed.")

if __name__ == "__main__":
    main()
