# Vim-1

> The foundational fMRI dataset that enabled the first large-scale natural image identification from brain signals.

**Used in**: [Kay et al. 2008](../../works/timeline.md)

---

## Overview

| Property | Value |
| :--- | :--- |
| **Modality** | fMRI (3 Tesla) |
| **Subjects** | 2 healthy adults |
| **Stimuli** | 1,750 natural images (1,500 training, 250 test) |
| **Image source** | Flickr natural photographs |
| **Voxel coverage** | Primary visual cortex (V1) and surrounding areas |
| **Access** | Public — [crcns.org/data-sets/vc/vim-1](https://crcns.org/data-sets/vc/vim-1) |
| **Paper** | Kay et al., *Nature* 2008 — [DOI](https://doi.org/10.1038/nature06713) |

---

## Design

Subjects viewed natural photographs presented at 200 ms intervals while fMRI BOLD responses were recorded from early visual cortex (V1). The dataset was used to train a Gabor-Wavelet-Pyramid **encoding model** that could then identify which of 120 candidate images a subject was viewing based on novel fMRI responses alone.

---

## Significance

Vim-1 established that visual images could be **identified** (not yet reconstructed) purely from fMRI signals using voxelwise encoding models. It set the template for the encoding→decoding paradigm that drives all subsequent work.

---

## Related Datasets

- [NSD](nsd.md) — the modern successor with 40× more stimuli at 7T resolution
- [ds001506](ds001506.md) — another early small-N 7T dataset used for reconstruction
- [GOD](god.md) — object-level fMRI dataset that extended to imagined stimuli
