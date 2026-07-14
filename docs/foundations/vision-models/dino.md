# DINO / DINOv2

> Self-supervised ViT representations capturing fine-grained spatial and semantic details.

---

## Overview

**DINO** (2021) and **DINOv2** (2023) by Meta are self-supervised ViT models trained using a self-distillation objective without labels:

- **Key Property**: Produces highly localized semantic features. Each patch embedding relates to a specific, segmentable image region (e.g., object parts).
- **DINOv2**: Trained on a massive, curated dataset of 142M images, yielding universal visual features.

---

## Role in Brain Decoding

### Spatial Semantics
DINOv2 features serve as spatially detailed, semantically rich targets in brain decoding. Because DINOv2 retains spatial patch layouts, researchers can train brain encoders to predict patch-level features, allowing reconstruction models to understand where specific semantic objects are positioned in the visual field.

### Spatial Selectivity Probing
Useful for probing **where** in the visual field the brain is attending. By correlating DINOv2 patch attention maps with retinotopic fMRI voxel patterns, we can identify how specific visual cortex areas represent localized object shapes and boundaries.
