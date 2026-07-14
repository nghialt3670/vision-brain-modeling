# Datasets

> A curated catalog of public neuroimaging and brain-computer interface datasets used for training and benchmarking visual decoding models.

---

## Public Datasets

### 1. Natural Scenes Dataset (NSD)

The **Natural Scenes Dataset (NSD)** is the premier dataset for high-resolution visual decoding.

- **Modality**: fMRI (7-Tesla, ultra-high-resolution)
- **Subjects**: 8 healthy subjects
- **Stimuli**: 73,000 unique natural images from the MS COCO dataset
- **Design**: Subjects viewed images for 3 seconds, performing a recognition memory task. Each subject saw up to 30,000 trials across 30-40 scanner sessions.
- **Why it's important**: The ultra-high spatial resolution (1.8 mm isotropic voxels) captures fine-grained spatial representations. It is the core training and test set for models like *MindEye* and *Brain Diffuser*.

### 2. THINGS-data (fMRI, EEG, & MEG)

The **THINGS** initiative provides a unique multimodal dataset containing different recordings for the same stimulus set.

- **Stimuli**: 22,248 natural object images representing 1,854 distinct concepts (e.g., Apple, Tiger, Chair).
- **Subsets**:
    - **THINGS-fMRI**: 3 subjects, 3-Tesla fMRI, high semantic coverage.
    - **THINGS-EEG**: 50 subjects, 64-channel EEG, capturing high temporal dynamics of object recognition.
    - **THINGS-MEG**: 4 subjects, 306-channel MEG, combining high temporal and decent spatial resolution.
- **Why it's important**: Enables direct cross-modal comparisons (e.g., mapping EEG patterns to fMRI activations) and is highly suited for testing object classification and semantic representation.

---

## EEG Benchmark Datasets

### 1. EEG-ImageNet
- **Modality**: 128-channel EEG
- **Subjects**: 6 subjects
- **Stimuli**: 2,000 images selected from 40 ImageNet categories
- **Usage**: A classic benchmark for classifying viewed objects using deep learning backbones like EEGNet.

### 2. BOLD5000
- **Modality**: 3T fMRI
- **Subjects**: 4 subjects
- **Stimuli**: 5,254 images from COCO, ImageNet, and Scene datasets.
- **Usage**: Bridges the gap between traditional small-scale fMRI datasets and large-scale vision benchmarks.

---

## Data Repositories

### OpenNeuro
An open-science repository hosting hundreds of raw neuroimaging datasets:
- **EEG/fMRI Naturalistic Viewing Dataset**: Multi-subject recordings during movie clips.
- **BIDS Format**: OpenNeuro strictly uses the Brain Imaging Data Structure (BIDS) standard, simplifying code pipelines.

---

## Evaluation Protocols

When benchmarked against these datasets, models must follow strict validation protocols to ensure results are not inflated by leakage:

1. **Leave-One-Session-Out**: Test on a completely separate scanner session to control for temporal drifts.
2. **Leave-One-Subject-Out (Zero-shot Subject)**: Test on a subject whose data was never seen during training (critical for evaluating generalizability).
3. **Unseen Images**: The test set must consist of brain responses to images that the encoder and generative decoders have never encountered during training.
