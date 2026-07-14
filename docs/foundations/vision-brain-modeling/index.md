# Vision-Brain Modeling

> Understand how visual information is represented inside the brain and how to model that relationship computationally.

---

## Overview

**Vision-Brain Modeling** is the study of how visual information is encoded and decoded in the brain. The field combines:

- **Neuroscience**: Understanding how the visual cortex represents scenes, objects, and features.
- **Machine Learning**: Building computational models that approximate or decode these neural representations.
- **Computer Vision**: Providing powerful image encoders and generative decoders.

The central goal is to establish **bidirectional mappings** between brain activity (fMRI voxels, EEG time-series, etc.) and visual content (images, concepts, semantic descriptions).

---

## Encoding vs. Decoding

| Direction | Task | Example |
|-----------|------|---------|
| **Encoding** (Image → Brain) | Predict brain response given a visual stimulus | Train a model to predict fMRI BOLD responses from image features |
| **Decoding** (Brain → Image/Text) | Reconstruct stimulus from neural activity | Reconstruct a viewed image from fMRI signals |

Encoding models help us understand **what visual features are represented** in specific brain regions.  
Decoding models allow **reading out perceived or imagined content** from brain signals.

---

## Brain Representation Learning

Brain representation learning aims to learn structured, generalizable embeddings from neural signals:

- **Voxel-wise encoding models**: Map image features to individual fMRI voxel responses using linear or nonlinear regression.
- **ROI-based representations**: Aggregate signals from anatomically or functionally defined regions of interest (ROIs).
- **Subject-level embeddings**: Produce a single brain embedding vector per trial (analogous to a sentence embedding).
- **Cross-subject alignment**: Map multiple subjects into a common latent space to enable transfer learning.

Key insight: Representations in early visual cortex (V1, V2) align well with **low-level features** (edges, frequency), while higher areas (IT, FFA) align with **high-level semantics** (object categories, faces).

---

## Vision-Brain Alignment

Alignment methods establish a correspondence between visual model embeddings and brain signals:

### Linear Mapping
- Ridge regression (L2-regularized) is the most common baseline.
- Maps image features from a DNN layer to fMRI voxel activations.
- Used in encoding model benchmarks like **Brain-Score**.

### Contrastive Alignment (CLIP-style)
- Train an encoder on (brain signal, image) pairs with a contrastive loss (e.g., InfoNCE).
- Example: **MindEye**, **MindBridge**, **UniBrain**.
- Aligns brain embeddings to the **CLIP image embedding space**.

### Cross-Attention Alignment
- Use transformer cross-attention to softly attend over image patch tokens conditioned on brain signals.
- Allows fine-grained spatial alignment between cortical patches and image regions.

---

## Feature Decoding

Feature decoding refers to predicting specific image features from brain activity:

- **Category decoding**: Predict object category labels (e.g., ImageNet classes).
- **Low-level feature decoding**: Decode edge orientations, spatial frequencies, color from V1/V2.
- **High-level feature decoding**: Decode semantic scene content from ventral stream regions.
- **DNN feature decoding**: Decode intermediate features of a pre-trained network (e.g., AlexNet, CLIP) from fMRI responses.

Foundational work: **Miyawaki et al. (2008)**, **Nishimoto et al. (2011)**, **Shen et al. (2019 — Deep Image Reconstruction)**.

---

## Latent Representation

Modern brain decoding leverages the latent spaces of generative models:

| Latent Space | Model | Usage in Brain Decoding |
|-------------|-------|------------------------|
| CLIP image space | CLIP ViT/RN | Semantic similarity + zero-shot retrieval |
| CLIP text space | CLIP text encoder | Brain captioning via embedding alignment |
| VAE latent space | Stable Diffusion VAE | Low-level image reconstruction |
| Diffusion noise space | DDPM / DDIM | Conditioning for reconstruction |
| LLM embedding space | LLAMA, GPT | Brain-to-text generation |

The typical pipeline: **Brain → Encoder → Latent Space → Decoder → Image/Text**.

---

## Semantic Alignment

Semantic alignment ensures that decoded representations capture the **conceptual meaning** of the stimulus, not just its pixel appearance:

- CLIP-based loss functions penalize semantic dissimilarity.
- Brain captioning tasks explicitly align neural signals to natural language descriptions.
- **PRISM (2025)**: Discovered that fMRI signals align more naturally to **text embedding space** than image embedding space, improving structural reconstruction fidelity.

---

## Cross-Modal Learning

Cross-modal learning enables knowledge transfer between different signal types or modalities:

- **EEG ↔ fMRI translation**: Diffusion-based cross-modal generation to produce fMRI-like spatial maps from EEG temporal signals.
- **Image ↔ Brain**: Vision-language-brain trimodal training.
- **Modality-agnostic encoders**: Unified architectures (e.g., transformer with modality tokens) that process EEG, MEG, and fMRI.

---

## Contrastive Learning in Brain Decoding

Contrastive learning is widely used to align brain signals with visual representations:

- **InfoNCE loss**: Maximize agreement between a brain embedding and its matched image embedding.
- **MindEye (2023)**: Projects fMRI to CLIP space via a retrieval-contrastive objective.
- **ATM (Adaptive Thinking Mapper, 2024)**: EEG-based zero-shot reconstruction via contrastive alignment.
- **Advantages**: Works with small datasets; allows zero-shot retrieval without reconstruction.

---

## Key Models and Papers

| Paper | Year | Modality | Task | Key Contribution |
|-------|------|----------|------|-----------------|
| Miyawaki et al. | 2008 | fMRI | Reconstruction | First pixel reconstruction from fMRI |
| Nishimoto et al. | 2011 | fMRI | Motion reconstruction | Decoding natural movies from V1 |
| Shen et al. (Deep Image Rec.) | 2019 | fMRI | Reconstruction | DNN features as intermediate bridge |
| Ozcelik et al. (MindEye) | 2023 | fMRI | Retrieval + Reconstruction | CLIP-space alignment with diffusion |
| Chen et al. (MindBridge) | 2023 | fMRI | Cross-subject | Unified cross-subject decoder |
| Scotti et al. (MindEye2) | 2024 | fMRI | Reconstruction | Large-scale multisubject training |
| Zhou et al. (ATM) | 2024 | EEG | Reconstruction | Zero-shot EEG reconstruction |
| PRISM | 2025 | fMRI | Reconstruction | Text-space alignment for structure fidelity |
