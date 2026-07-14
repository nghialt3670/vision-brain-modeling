# MAE (Masked Autoencoder)

> Self-supervised masked reconstruction models for robust structural feature extraction.

---

## Overview

**MAE** (He et al., Meta 2022) is a self-supervised pre-training method that masks a high percentage (75–80%) of image patches and trains a ViT autoencoder to reconstruct the missing pixels:

- Focuses on learning both structural continuity and high-level semantics.
- Highly efficient pre-training compared to contrastive approaches.

---

## Role in Brain Decoding

### Masked Neural Modeling
The core concept of MAE (mask-and-reconstruct) has been directly adapted to brain signal encoders. For instance, **NICE (2023)** and **DreamDiffusion (2023)** apply masked autoencoding directly to raw EEG signals:
1. Mask out sections of the temporal EEG time-series.
2. Train a transformer encoder to reconstruct the missing signals.
3. This pre-training step allows the encoder to learn robust temporal representations of brain activity before fine-tuning on image-paired decoding tasks.

### Structural Encoding
Because MAE is trained on pixel reconstruction, its intermediate representations retain high-fidelity structural details (like spatial geometry and outline details) making it a valuable target for structural fMRI decoding pipelines.
