# Automatic Multi-View X-Ray/CT Registration Using Bone Substructure Contours

**TL;DR:** A fully automatic, two-view X-ray/CT registration method that matches contours of specific bone substructures (instead of the whole bone silhouette) via multi-view iterative closest point (ICP), reaching 0.67 mm mean reprojection error — roughly 8× more accurate than a commercial solution that still needs manual key-point annotation.

## Metadata

- **Authors:** Roman Flepp, Leon Nissen, Bastian Sigrist, Arend Nieuwland, Nicola Cavalcanti, Philipp Fürnstahl, Thomas Dreher, Lilian Calvet
- **Venue:** Accepted to IPCAI 2025; published in the *International Journal of Computer Assisted Radiology and Surgery (IJCARS)*, May 2025
- **arXiv ID:** [2506.13292](https://arxiv.org/abs/2506.13292)
- **DOI:** [10.1007/s11548-025-03391-4](https://doi.org/10.1007/s11548-025-03391-4)
- **Code:** [github.com/rflepp/MultiviewXrayCT-Registration](https://github.com/rflepp/MultiviewXrayCT-Registration)
- **Dataset:** [5-specimen cadaveric X-ray/CT dataset on Hugging Face](https://huggingface.co/datasets/eigenvivek/xvr-data) ([also on Zenodo](https://zenodo.org/records/15753063))
- **Project page (HTML, figures, demo videos):** [bone-substructure-contours-xray-ct-registration.html](../bone-substructure-contours-xray-ct-registration.html)

## Abstract

**Purpose:** Accurate intraoperative X-ray/CT registration is essential for surgical navigation in orthopedic procedures. However, existing methods struggle with consistently achieving sub-millimeter accuracy, robustness under broad initial pose estimates, or need manual key-point annotations. This work aims to address these challenges by proposing a novel multi-view X-ray/CT registration method for intraoperative bone registration.

**Methods:** The proposed registration method consists of a multi-view, contour-based iterative closest point (ICP) optimization. Unlike previous methods, which attempt to match bone contours across the entire silhouette in both imaging modalities, we focus on matching specific subcategories of contours corresponding to bone substructures. This leads to reduced ambiguity in the ICP matches, resulting in a more robust and accurate registration solution. This approach requires only two X-ray images and operates fully automatically. Additionally, we contribute a dataset of 5 cadaveric specimens, including real X-ray images, X-ray image poses and the corresponding CT scans.

**Results:** The proposed registration method is evaluated on real X-ray images using mean reprojection error (mRPD). The method consistently achieves sub-millimeter accuracy with a mRPD of 0.67 mm compared to 5.35 mm by a commercial solution requiring manual intervention.

**Conclusion:** Our method offers a practical, accurate, and efficient solution for multi-view X-ray/CT registration in orthopedic surgeries, which can be easily combined with tracking systems.

## Key Contributions

- A **multi-view, contour-based ICP registration algorithm** that matches **bone-substructure contour subcategories** (e.g., distinct anatomical sub-regions) rather than the full bone silhouette, reducing correspondence ambiguity in the ICP optimization.
- A **fully automatic pipeline** requiring only **two X-ray images** and no manual key-point annotation, in contrast to commercial navigation solutions that require manual intervention.
- A new **cadaveric benchmark dataset** of 5 specimens with real X-ray images, calibrated X-ray poses, and paired CT scans, released publicly for reproducible evaluation.
- **Sub-millimeter registration accuracy** (0.67 mm mean reprojection distance), an ~8× improvement over a manually-assisted commercial solution (5.35 mm).
- Designed to be **easily combined with existing tracking systems** for full intraoperative navigation pipelines.

## Results

| Method | Mean Reprojection Distance (mRPD) | Manual Intervention |
| --- | --- | --- |
| Commercial solution | 5.35 mm | Required |
| **Proposed method (ours)** | **0.67 mm** | None (fully automatic) |

- **~8× lower mean reprojection error** than the commercial baseline.
- Sub-millimeter accuracy achieved from only **2 X-ray views**, fully automatically.

## Key Terms

- **Iterative Closest Point (ICP):** an optimization algorithm that iteratively minimizes the distance between corresponding points (or contours) of two point sets to estimate the rigid transformation aligning them.
- **Mean reprojection distance (mRPD):** the average 2D pixel-space distance between a projected 3D landmark and its true position in the X-ray image after registration — a standard sub-millimeter accuracy metric for X-ray/CT registration.
- **Bone substructure contours:** anatomically distinct sub-regions of a bone's projected silhouette (e.g., specific ridges or condyles) used as matching primitives instead of the full outline, reducing ambiguous correspondences.

## Citation

```bibtex
@article{Flepp2025,
  author  = {Flepp, Roman and Nissen, Leon and Sigrist, Bastian and Nieuwland, Arend and Cavalcanti, Nicola and F{\"u}rnstahl, Philipp and Dreher, Thomas and Calvet, Lilian},
  title   = {Automatic Multi-View X-Ray/CT Registration Using Bone Substructure Contours},
  journal = {International Journal of Computer Assisted Radiology and Surgery},
  year    = {2025},
  month   = may,
  day     = {20},
  doi     = {10.1007/s11548-025-03391-4},
  url     = {https://link.springer.com/article/10.1007/s11548-025-03391-4},
}
```

---
[← Back to portfolio](../index.html)
