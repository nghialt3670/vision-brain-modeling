# Papers

> Key publications in visual brain decoding and brain-guided image editing.

| Paper | Year | Modality | Dataset | Model | Task | Performance |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **[Kay et al.](https://doi.org/10.1038/nature06713)** | 2008 | fMRI | [Vim-1](../resources/datasets/vim-1.md) | Bayesian reg. | Category decoding | Top-1 ~75% |
| **[Nishimoto et al.](https://doi.org/10.1016/j.cub.2011.08.031)** | 2011 | fMRI | Custom Movie set | Motion-energy + Bayesian | Movie reconstruction | Qualitative |
| **[Horikawa & Kamitani (Science)](https://doi.org/10.1126/science.1234330)** | 2013 | fMRI | [GOD (Dream)](../resources/datasets/god.md#dream-dataset) | Linear Classifier | Dream decoding | Significant |
| **[Horikawa & Kamitani (Nat. Comm.)](https://doi.org/10.1038/ncomms15037)** | 2017 | fMRI | [GOD](../resources/datasets/god.md) | Sparse Linear Regression | Hierarchical feature decoding | Recognizable |
| **[Shen et al.](https://doi.org/10.1371/journal.pcbi.1006633)** | 2019 | fMRI (7T) | [ds001506](../resources/datasets/ds001506.md) | DNN (VGG) + DGN | Image reconstruction | Resembled inputs |
| **[Gaziv et al.](https://doi.org/10.1016/j.neuroimage.2022.119047)** | 2022 | fMRI | [NSD](../resources/datasets/nsd.md) | Cycle-consistent VAE | Reconstruction + 1000-way | SOTA |
| **[Davis et al.](https://openaccess.thecvf.com/content/CVPR2022/html/Davis_Visual_Image_Reconstruction_From_Human_Brain_Activity_Using_a_CVPR_2022_paper.html)** | 2022 | EEG | Synthetic faces | GAN latent + EEG classifier | Latent-space editing | ≈ Manual labeling |
| **[Ozcelik & VanRullen](https://doi.org/10.1038/s41598-023-42456-4)** | 2023 | fMRI (7T) | [NSD](../resources/datasets/nsd.md) | VDVAE + Latent Diffusion | Image reconstruction | SOTA |
| **[Miliotou et al.](https://proceedings.mlr.press/v202/miliotou23a.html)** | 2023 | fMRI | [GOD](../resources/datasets/god.md) | Hierarchical VAE | Image reconstruction | Improved |
| **[Benchetrit et al.](https://arxiv.org/abs/2310.19812)** | 2023 | MEG | [THINGS-MEG](../resources/datasets/things.md) | ConvNet (DINOv2) | Image retrieval | Top-5 ~69.8% |
| **[Huo et al. (NeuroPictor)](https://arxiv.org/abs/2404.14811)** | 2024 | fMRI | [NSD](../resources/datasets/nsd.md) / [GOD](../resources/datasets/god.md) | Diffusion (high/low net) | Image reconstruction | SOTA |
| **[Zhou et al. (LoongX)](https://arxiv.org/abs/2507.05397)** | 2025 | EEG/fNIRS/PPG | [LoongX](../resources/datasets/loongx.md) | Conditional DiT | Brain-driven editing | CLIP-I 0.6605 |
| **[Beliy et al. (Brain-IT)](https://arxiv.org/abs/2602.04066)** | 2026 | fMRI | [NSD](../resources/datasets/nsd.md) | Transformer + Diffusion | Image reconstruction | SOTA |
