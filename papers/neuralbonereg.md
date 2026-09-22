# NeuralBoneReg: An Instance-Specific Label-Free Point Cloud-Based Method for Multi-Modal Bone Surface Registration

**TL;DR:** NeuralBoneReg is a self-supervised, modality-agnostic framework that registers preoperative and intraoperative bone surfaces (CT, ultrasound, RGB-D) as 3D point clouds, using a neural unsigned distance field plus an MLP registration head, matching or beating supervised state-of-the-art across three multi-modal surgical datasets without any inter-subject training data.

## Metadata

- **Authors:** Luohong Wu, Matthias Seibold, Nicola A. Cavalcanti, Yunke Ao, Roman Flepp, Aidana Massalimova, Lilian Calvet, Philipp Fürnstahl
- **Venue:** arXiv preprint, submitted November 18, 2025; journal version in *Medical Image Analysis*
- **arXiv ID:** [2511.14286](https://arxiv.org/abs/2511.14286)
- **DOI:** https://doi.org/10.48550/arXiv.2511.14286
- **Journal reference:** https://doi.org/10.1016/j.media.2026.104133

## Abstract

In computer- and robot-assisted orthopedic surgery (CAOS), patient-specific surgical plans derived from preoperative imaging define target locations and implant trajectories. During surgery, these plans must be accurately transferred, relying on precise cross-registration between preoperative and intraoperative data. However, substantial modality heterogeneity across imaging modalities makes this registration challenging and error-prone. Robust, automatic, and modality-agnostic bone surface registration is therefore clinically important. We propose NeuralBoneReg, a self-supervised, surface-based framework that registers bone surfaces using 3D point clouds as a modality-agnostic representation. NeuralBoneReg includes two modules: an implicit neural unsigned distance field (UDF) that learns the preoperative bone model, and an MLP-based registration module that performs global initialization and local refinement by generating transformation hypotheses to align the intraoperative point cloud with the neural UDF. Unlike SOTA supervised methods, NeuralBoneReg operates in a self-supervised manner, without requiring inter-subject training data.

## Key Contributions

- **NeuralBoneReg**, a self-supervised, surface-based registration framework that represents bone anatomy as **3D point clouds** — a single modality-agnostic representation usable across CT, ultrasound, and RGB-D data.
- A two-module architecture: (1) an **implicit neural unsigned distance field (UDF)** that learns a continuous preoperative bone-surface model, and (2) an **MLP-based registration module** performing global pose initialization followed by local refinement.
- **No inter-subject training data required** — unlike state-of-the-art supervised registration methods, the model is fit per-instance in a self-supervised manner, avoiding the need for large labeled cross-patient datasets.
- **UltraBones-Hip**, a new CT-ultrasound cadaveric dataset covering the femur and pelvis, introduced and made publicly available alongside the method.
- Evaluation across **three multi-modal datasets** spanning three anatomical regions and three modality pairs (CT-ultrasound tibia/fibula, CT-ultrasound femur/pelvis, CT-RGB-D spine), demonstrating strong cross-anatomy, cross-modality generalization.

## Results

| Dataset | Modality Pair | Anatomy | Mean RRE (°) | Mean RTE (mm) |
| --- | --- | --- | --- | --- |
| UltraBones100k | CT–ultrasound | Fibula, tibia | 1.83 | 2.02 |
| UltraBones-Hip (new) | CT–ultrasound | Femur, pelvis | 1.90 | 1.56 |
| SpineDepth | CT–RGB-D | Spinal vertebrae | 3.78 | 2.80 |

- NeuralBoneReg **matches or surpasses existing (including supervised) baseline methods** on all three benchmarks despite requiring no cross-patient training data.
- Sub-2° / sub-2.1 mm mean error on both CT-ultrasound datasets, indicating clinically relevant accuracy for cross-modal registration in computer-assisted orthopedic surgery (CAOS).

## Key Terms

- **RRE / RTE (Relative Rotation Error / Relative Translation Error):** standard rigid-registration accuracy metrics measuring the angular (°) and positional (mm) deviation between the estimated and ground-truth alignment.
- **Unsigned distance field (UDF):** an implicit neural representation that encodes a 3D surface as a continuous field of (unsigned) distances to the nearest surface point, learned by a neural network instead of stored as an explicit mesh.
- **Modality-agnostic registration:** an alignment approach that operates on a shared representation (here, point clouds) so the same model generalizes across imaging modalities — CT, ultrasound, RGB-D — without modality-specific retraining.
- **Self-supervised, instance-specific registration:** the model is optimized per surgical case from the case's own data, rather than trained once on a labeled multi-patient dataset.

## Citation

```bibtex
@article{wu2026neuralbonereg,
  title   = {NeuralBoneReg: An Instance-Specific Label-Free Point Cloud-Based Method for Multi-Modal Bone Surface Registration},
  author  = {Wu, Luohong and Seibold, Matthias and Cavalcanti, Nicola A. and Ao, Yunke and Flepp, Roman and Massalimova, Aidana and Calvet, Lilian and F{\"u}rnstahl, Philipp},
  journal = {Medical Image Analysis},
  year    = {2026},
  doi     = {10.1016/j.media.2026.104133},
  url     = {https://arxiv.org/abs/2511.14286}
}
```

---
[← Back to portfolio](../index.html)
