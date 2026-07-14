# fMRI

> Functional Magnetic Resonance Imaging — the gold standard for brain decoding research due to its unmatched spatial resolution.

---

## How fMRI Works

fMRI measures **BOLD (Blood-Oxygen-Level-Dependent)** contrast — a proxy for neural activity based on local changes in blood oxygenation:

1. Neural activity → increased local metabolic demand.
2. Increased cerebral blood flow delivers oxygenated hemoglobin.
3. Deoxyhemoglobin (paramagnetic) vs. oxyhemoglobin (diamagnetic) produces detectable MR signal differences.
4. The **hemodynamic response function (HRF)** describes this slow response (~6 s peak).

---

## Technical Specifications

| Property | Typical Value |
|----------|--------------|
| Spatial resolution | 1–3 mm (7T achieves ~0.8 mm) |
| Temporal resolution (TR) | 1–3 s |
| Hemodynamic lag | ~4–6 s after stimulus |
| Field strength | 1.5T, 3T, 7T (ultra-high field) |
| Data unit | BOLD signal (% change) |

---

## Strengths

- **Whole-brain coverage** with millimeter spatial precision.
- Non-invasive and safe for repeated sessions.
- Excellent for identifying **which brain regions** process visual features.
- Compatible with complex naturalistic stimuli (images, videos, audio).

---

## Limitations

- **Slow temporal resolution** (~2 s TR, ~6 s HRF lag) — cannot capture rapid neural dynamics.
- Expensive equipment (~$1–3M per scanner) and high operational costs.
- Susceptible to head motion artifacts.
- BOLD is an **indirect proxy** for neural activity.
- Requires subjects to remain still in a noisy, claustrophobic environment.

---

## Key fMRI Datasets for Brain Decoding

| Dataset | Subjects | Stimuli | Field Strength | Notes |
|---------|----------|---------|---------------|-------|
| **NSD** (Natural Scenes Dataset) | 8 | ~73,000 COCO images | 7T | Gold standard; used by MindEye, Brain Diffuser |
| **THINGS-fMRI** | 3 | 22,248 object images | 3T | Large concept coverage; paired with MEG/EEG |
| **GOD** (Generic Object Decoding) | 6 | 1,200 ImageNet images | 3T | Seminal decoding benchmark by Shen et al. |
| **BOLD5000** | 4 | 5,254 images | 3T | Diverse stimuli (COCO, ImageNet, SUN) |
| **NSD-Imagery** | 8 | Mental imagery | 7T | Extends NSD to imagined stimuli (2025) |

---

## fMRI in Brain Decoding Pipelines

### Trial-Level GLM

For brain decoding, individual trial responses are estimated via a General Linear Model (GLM):

```
Y = X β + ε
```

- `Y`: voxel time-series
- `X`: design matrix (stimulus onset convolved with HRF)
- `β`: trial-level beta coefficients (one per voxel per trial)

The resulting **beta maps** (3D images of voxel activations) are used as input to the brain encoder.

### Common Brain Encoder Architectures for fMRI

| Architecture | Details |
|-------------|---------|
| Linear projection | Ridge regression from voxels → embedding |
| MLP | 2–4 layer MLP on flattened voxel vector |
| Brain-ViT | Patch the voxel volume as a 3D spatial grid; apply ViT |
| ROI pooling | Average voxels within anatomical ROIs; reduce dimensionality |

---

## Representative Papers Using fMRI

| Paper | Year | Key Idea |
|-------|------|---------|
| Miyawaki et al. | 2008 | First pixel-level reconstruction from fMRI |
| Nishimoto et al. | 2011 | Natural movie reconstruction using motion energy model |
| Shen et al. (Deep Image Rec.) | 2019 | DNN features as intermediary for image generation |
| Ozcelik & VanRullen (Brain Diffuser) | 2022 | Stable Diffusion conditioned on fMRI |
| Scotti et al. (MindEye) | 2023 | CLIP alignment + diffusion reconstruction |
| Scotti et al. (MindEye2) | 2024 | Multi-subject generalization with 7-subject NSD training |
| PRISM | 2025 | Text-space alignment outperforms vision-space for fMRI |
