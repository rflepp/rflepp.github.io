# Real-World Mobile Image Denoising Dataset with Efficient Baselines

**TL;DR:** A real-world mobile-noise image denoising dataset paired with efficient, on-device-deployable baseline models, aimed at more realistic benchmarking of mobile imaging pipelines than synthetic-noise datasets allow.

## Metadata

- **Venue:** CVPR 2024 (IEEE/CVF Conference on Computer Vision and Pattern Recognition)
- **Topic area:** Computational photography, image denoising, mobile/on-device deep learning
- **Paper (PDF):** [CVF Open Access](https://openaccess.thecvf.com/content/CVPR2024/papers/Flepp_Real-World_Mobile_Image_Denoising_Dataset_with_Efficient_Baselines_CVPR_2024_paper.pdf)
- **Dataset download:** [ai-benchmark.com mirror](https://download.ai-benchmark.com/s/Gq3n2cS7QkH7ZMz)
- **Full author list and formal citation:** see the official CVF Open Access page linked above.

## Abstract

A curated dataset that captures the complexity of mobile noise patterns alongside strong baseline models optimized for on-device deployment. The work sets a new foundation for realistic benchmarking and rapid experimentation in mobile imaging pipelines.

## Key Contributions

- A **real-world mobile image denoising dataset** capturing authentic smartphone sensor-noise characteristics, rather than synthetically injected Gaussian/Poisson noise.
- **Efficient baseline denoising models** designed for **on-device deployment**, targeting realistic mobile compute and memory budgets rather than server-scale architectures.
- A benchmarking foundation intended to make mobile-imaging denoising research **more reproducible and closer to real deployment conditions**.

## Key Terms

- **Mobile image denoising:** the task of removing sensor noise from photos captured on smartphone cameras, complicated by small sensors, variable lighting, and on-device compute constraints.
- **Real-world (vs. synthetic) noise dataset:** a dataset built from noise patterns captured directly from physical camera sensors, as opposed to noise simulated with standard statistical models — real-world noise is generally harder to remove and more representative of deployment conditions.
- **On-device deployment baseline:** a model architecture explicitly constrained (in parameter count, latency, or memory) to run efficiently on mobile hardware rather than a cloud GPU.

## Citation

```bibtex
@inproceedings{flepp2024mobiledenoising,
  title     = {Real-World Mobile Image Denoising Dataset with Efficient Baselines},
  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
  year      = {2024},
  url       = {https://openaccess.thecvf.com/content/CVPR2024/papers/Flepp_Real-World_Mobile_Image_Denoising_Dataset_with_Efficient_Baselines_CVPR_2024_paper.pdf}
}
```

*Note: the full, verified author list and BibTeX key should be taken from the official CVF Open Access page — this summary reflects only the metadata available on this portfolio site.*

---
[← Back to portfolio](../index.html)
