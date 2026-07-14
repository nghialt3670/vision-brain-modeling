# SAM (Segment Anything Model)

> Zero-shot segmentation model used to decode visual boundaries and validate reconstruction layouts.

---

## Overview

**SAM** (Kirillov et al., Meta 2023) is a prompt-driven foundation model for image segmentation, trained on a dataset of 1.1 billion mask annotations:

- Produces high-quality, pixel-accurate segmentation masks for any object in an image.
- Capable of zero-shot generalization to unseen categories and domains.

---

## Role in Brain Decoding

### Layout and Boundary Decoding
SAM features encode spatial layout, depth layers, and object boundaries. In brain-to-image pipelines, SAM can be used as a target to decode the "spatial scaffolding" of a scene from early visual areas, providing a structural layout prior to rendering details.

### Semantic Segmentation Validation
SAM is widely used to evaluate the **spatial fidelity** of reconstructed images. By segmenting the original stimulus and the reconstructed output, researchers can calculate overlap metrics (like Intersection over Union, IoU) on object boundaries to measure how well the model captured the placement and size of viewed items.
