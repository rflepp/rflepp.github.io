# Electromagnetic Navigation for Femoral Osteotomy Using High-Accuracy X-ray-to-CT Registration

**TL;DR:** An electromagnetic-tracking (EMT) surgical navigation system guides femoral corrective osteotomies using only two intraoperative X-ray images for registration, matching the accuracy of patient-specific 3D-printed guides while cutting angular error by 52% versus free-hand technique, with no added soft-tissue exposure.

## Metadata

- **Authors:** Roman Flepp, Arend Nieuwland, Bastian Sigrist, Philipp Fürnstahl, Lilian Calvet, Thomas Dreher
- **Affiliations:** Department of Pediatric Orthopedics and Traumatology, University Children's Hospital Zürich; Research in Orthopedic Computer Science (ROCS), University Hospital Balgrist, University of Zurich; Department of Orthopedic Surgery, University Hospital Balgrist, University of Zurich
- **Venue:** arXiv preprint, June 2026 — to be published in the *International Journal of Computer Assisted Radiology and Surgery (IJCARS)*
- **arXiv ID:** [2606.03893](https://arxiv.org/abs/2606.03893)
- **DOI:** https://doi.org/10.48550/arXiv.2606.03893
- **Project page (HTML, figures, demo video):** [electromagnetic-navigation-femoral-osteotomy.html](../electromagnetic-navigation-femoral-osteotomy.html)

## Abstract

Accurate execution of preoperative plans in corrective femoral osteotomies remains challenging. Current techniques are limited by variable accuracy, invasiveness, and radiation exposure, with free-hand methods and patient-specific instrumentation (PSI) often requiring >30 and >6 fluoroscopic images, respectively. We present an integrated, electromagnetic tracking (EMT)-based navigation system for femoral osteotomies that minimizes dissection and intraoperative fluoroscopy. The system couples CT-based preoperative planning with one-time intraoperative C-arm calibration and accurate X-ray-to-CT registration from two fluoroscopic images acquired at initialization. This enables real-time, fluoroscopy-free EMT navigation of the saw blade and bone fragments relative to the preoperative plan, and is compatible with uniplanar and biplanar osteotomies. In a feasibility study using 18 synthetic femora, EMT guidance significantly outperformed free-hand execution in total angular error (3.05° ± 0.75° vs. 6.32° ± 2.36°, p = 0.031). No EMT-guided trials exceeded the >5° clinical threshold, whereas free-hand produced 4 outliers of 6 trials. The system achieved statistical equivalence (±2°, ±2 mm) to PSI for total angular (p ≤ 0.02) and total translational (p = 0.048) errors, with no significant differences in user questionnaire scores.

## Key Contributions

- An integrated **EMT-based navigation pipeline** unifying CT-based preoperative planning, one-time intraoperative C-arm calibration, and X-ray-to-CT registration into a single fluoroscopy-minimal workflow.
- **X-ray-to-CT registration from only two fluoroscopic images**, replacing the >30 images typically needed for free-hand navigation and the >6 needed to validate PSI guide placement.
- A **U-Net-based calibration-bead detector** that automatically solves C-arm intrinsic/extrinsic parameters from the two acquired X-ray views.
- **Real-time, line-of-sight-free tracking** of the saw blade and distal bone fragment relative to the preoperative plan, decomposed live into extension, derotation, and varisation error.
- **Feasibility validation on 18 synthetic femora** showing a 52% reduction in mean total angular error versus free-hand technique and statistical equivalence to patient-specific instrumentation (PSI), without PSI's added soft-tissue exposure or fabrication lead time.

## Method

1. **Preoperative planning:** A corrective osteotomy plan (cut plane, target extension/derotation/varisation) is derived from CT.
2. **Initial registration:** A calibration sleeve fitted with EMT sensors links the preoperative CT bone model to the EMT coordinate system. Two fluoroscopic C-arm images are used with the U-Net bead detector to solve C-arm pose and compute the X-ray-to-CT transform.
3. **Real-time navigation:** EMT sensors mounted on 3 mm Kirschner wires (K-wires) track the distal fragment relative to the proximal femur. A GUI displays live alignment error decomposed into clinically meaningful correction axes.

## Results

| Method | Mean Angular Error (°) | Mean Translational Error (mm) | Outliers (>5° clinical threshold) |
| --- | --- | --- | --- |
| Free-hand | 6.32 ± 2.36 | 5.56 ± 2.25 | 4 / 6 trials |
| PSI (guides) | 3.44 ± 1.16 | 3.36 ± 1.18 | 0 / 6 trials |
| **EMT Navigation (ours)** | **3.05 ± 0.75** | 3.59 ± 1.44 | 0 / 6 trials |

- **52% reduction** in mean angular error versus free-hand technique.
- **Statistical equivalence to PSI** (±2°, ±2 mm margins) in both angular (p ≤ 0.02) and translational (p = 0.048) accuracy.
- Requires only **2 fluoroscopic images** for initialization, versus a clinical free-hand benchmark averaging **34 images**.
- No significant difference in surgeon user-questionnaire scores versus PSI.

## Key Terms

- **Electromagnetic tracking (EMT):** a surgical navigation modality that localizes sensor-equipped instruments via magnetic fields, requiring no direct line of sight — unlike optical tracking systems.
- **Patient-specific instrumentation (PSI):** pre-manufactured, 3D-printed cutting/drilling guides matched to a patient's anatomy from preoperative CT, physically constraining tool placement to the plan.
- **X-ray-to-CT registration:** the process of aligning intraoperative 2D fluoroscopic images with a preoperative 3D CT volume to recover the patient's pose in the surgical coordinate frame.

## Citation

```bibtex
@article{flepp2026emtosteotomy,
  title   = {Electromagnetic Navigation for Femoral Osteotomy Using High-Accuracy X-ray-to-CT Registration},
  author  = {Flepp, Roman and Nieuwland, Arend and Sigrist, Bastian and F{\"u}rnstahl, Philipp and Calvet, Lilian and Dreher, Thomas},
  journal = {arXiv preprint arXiv:2606.03893},
  year    = {2026},
  url     = {https://arxiv.org/abs/2606.03893}
}
```

---
[← Back to portfolio](../index.html)
