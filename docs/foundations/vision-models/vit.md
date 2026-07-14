# Vision Transformer (ViT)

> Attention-based visual models capturing global dependencies and semantic alignments.

---

## Overview

Transformers applied to image patches using self-attention:

| Model | Year | Key Feature |
|-------|------|------------|
| **ViT-B/L/H** | 2020 | Standard patch-based image transformer |
| **DeiT** | 2021 | Data-efficient ViT training |
| **Swin Transformer** | 2021 | Hierarchical ViT with shifted windows |
| **BEiT** | 2021 | Masked image modeling pre-training |

---

## Role in Brain Decoding

### Semantic Representations
ViT features (especially from large, pre-trained models like `ViT-L/14`) provide semantically rich representations that align well with higher visual cortex areas. The self-attention mechanism in ViTs allows them to learn global dependencies, making their final layers closely resemble the abstract semantic representations found in the human inferior temporal (**IT**) cortex and lateral occipital complex (**LOC**).

### Visual Attention Mapping
Using self-attention maps from ViTs, researchers can study visual attention. By mapping fMRI/EEG attention coefficients back to ViT attention maps, we can evaluate whether the deep model's visual attention aligns with the human eye-gaze and cortical attention patterns when viewing identical stimuli.
