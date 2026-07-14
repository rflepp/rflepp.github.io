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
            "summary": abstract, # We just use the full abstract directly as the summary
            "links": links
        })
        
    return entries

def main():
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
            # Check if title, venue, or summary (abstract) needs updating/synchronizing
            needs_update = (
                existing_paper.get("summary") != entry["summary"] or
                existing_paper.get("venue") != entry["venue"] or
                existing_paper.get("title") != entry["title"] or
                "ai_generated" in existing_paper # We want to remove the ai_generated field
            )
            
            if needs_update:
                print(f"Updating abstract/details for paper: {entry['title']} (ID: {paper_id})")
                existing_paper["title"] = entry["title"]
                existing_paper["summary"] = entry["summary"]
                existing_paper["venue"] = entry["venue"]
                # Remove ai_generated field since we are displaying full abstracts
                existing_paper.pop("ai_generated", None)
                changes_made = True
            
        else:
            # Completely new paper
            print(f"New paper found: {entry['title']} (ID: {paper_id})")
            new_paper = {
                "id": paper_id,
                "title": entry["title"],
                "venue": entry["venue"],
                "summary": entry["summary"],
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
        print(f"Successfully updated papers and saved to {PAPERS_JSON_PATH}.")
    else:
        print("No updates needed.")

if __name__ == "__main__":
    main()
