# Brain-to-Image Editing

### An Introduction

Vision-Brain Modeling Knowledge Base

Note:
Welcome. This deck introduces brain-to-image editing as a task, its relationship to reconstruction and generation, and showcases LoongX as a leading example.

---

## Outline

1. Vision-brain modeling landscape
2. Related tasks: reconstruction & generation
3. Brain-to-image editing defined
4. Problem formulation & pipeline
5. Motivation, significance, and applications
6. Open challenges
7. Case study: LoongX (Zhou et al., 2025)
8. Future directions

---

## Vision-Brain Modeling

**Goal:** decode visual information and intent from neural signals

| Signal | Examples |
|--------|----------|
| Brain | EEG, fNIRS, fMRI, MEG |
| Peripheral | PPG (arousal / engagement) |
| Output | Images — reconstructed, generated, or **edited** |

The field has moved from *what did you see?* toward *what do you want to change?*

Note:
Frame the shift from passive decoding to intention-driven interaction.

---

## Related Tasks

Brain-to-image editing builds on two predecessor tasks — both map brain signals to an output image, but differ in what the signal encodes.

<div style="text-align:center;">
<p><strong>Reconstruction</strong> &mdash; $f: B \rightarrow I'$</p>
<pre class="mermaid">
graph LR
    I["Visual Stimulus I"] -->|shown to| U["Subject U"]
    U -->|neural response| B["Brain Signals B"]
    B -->|input to| F["Reconstruction f"]
    F -->|predicts| IP["Reconstructed Image"]
    style I fill:#1565c0,color:#fff,stroke:#0d47a1
    style U fill:#6a1b9a,color:#fff,stroke:#4a148c
    style B fill:#2e7d32,color:#fff,stroke:#1b5e20
    style F fill:#37474f,color:#fff,stroke:#263238
    style IP fill:#bf360c,color:#fff,stroke:#7f0000
</pre>
<small>Ground-truth exists &rarr; measurable evaluation</small>
<p><strong>Generation</strong> &mdash; $f: B \rightarrow I'$</p>
<pre class="mermaid">
graph LR
    U["Subject U"] -->|imagines or dreams| B["Brain Signals B"]
    B -->|input to| F["Generation f"]
    F -->|predicts| IP["Generated Image"]
    style U fill:#6a1b9a,color:#fff,stroke:#4a148c
    style B fill:#2e7d32,color:#fff,stroke:#1b5e20
    style F fill:#37474f,color:#fff,stroke:#263238
    style IP fill:#bf360c,color:#fff,stroke:#7f0000
</pre>
<small>No ground truth &rarr; harder to evaluate</small>
</div>

---

## Editing is Different

Both reconstruction and generation answer: *"What is in the subject's mind?"*

Editing asks a fundamentally different question:

> *"How does the subject want **this specific image** to change?"*

- Image $I$ is an **input** — not just a training target
- Brain signals encode **intended modification** — not current content
- Requires **reference preservation**: unedited regions must stay unchanged

---

## Brain-to-Image Editing — Definition

$$f: (I, B) \rightarrow I'$$

<pre class="mermaid">
graph LR
    I["Observed Image I"] -->|shown to| U["Subject U"]
    U -->|imagines edits| B["Brain Signals B"]
    I -->|reference| F["Editing Function f"]
    B -->|intent| F
    F -->|predicts| IP["Edited Image"]
    style I fill:#1565c0,color:#fff,stroke:#0d47a1
    style U fill:#6a1b9a,color:#fff,stroke:#4a148c
    style B fill:#2e7d32,color:#fff,stroke:#1b5e20
    style F fill:#37474f,color:#fff,stroke:#263238
    style IP fill:#bf360c,color:#fff,stroke:#7f0000
</pre>

---

## Problem Formulation

Given:

- **Observed image** `I` shown to the subject
- **Brain signals** `B` recorded while the subject imagines edits to `I`

Learn:

$$f: (I, B) \rightarrow I'$$

where `I'` reflects the subject's **intended changes**, not just what they currently see.

---

## Motivation

- Reconstruction recovers **what** was perceived — not **how to modify** a scene
- Many applications need to change an **existing image**, not regenerate from scratch
- Full image regeneration is wasteful for local or attribute-level edits
- Users may know *how* an image should change without being able to describe it in text

---

## Significance

- Shifts brain decoding from **what you see** → **how you want it to change**
- Enables **intention-driven**, interactive BCIs
- Finer control than one-shot reconstruction or generation
- Foundation for brain-guided creative and assistive tools

---

## Applications

| Area | Benefit |
|------|---------|
| **Hands-free editing** | No keyboard, mouse, touchscreen, or text prompt |
| **Accessibility** | Creative control for motor or speech impairments |
| **Brain-guided creativity** | Direct cognitive intent → image manipulation |
| **Adaptive human-AI** | Systems infer preferences from neural feedback |

---

## Challenges

| Challenge | Why it matters |
|-----------|----------------|
| **Intent decoding** | Must infer desired *change*, not current content |
| **Reference preservation** | Unedited regions should stay unchanged |
| **Weak neural signals** | Edit intent is subtle and noisy |
| **Semantic ambiguity** | One neural pattern → many possible edits |

Note:
The first two challenges are unique to editing — reconstruction and generation do not face the preservation or intent-decoding problems.

---

## Traditional vs. Brain-Driven Editing

| Traditional | Brain-to-image editing |
|-------------|------------------------|
| Text prompts | Neural / physiological signals |
| Masks, sketches, drag | Imagined or intended transformation |
| Explicit UI interaction | Hands-free, implicit intent |
| Accessible to typical users | Promising for assistive BCIs |

---

## Case Study: LoongX

**Neural-Driven Image Editing** — Zhou et al. (NeurIPS 2025)

> Replace text prompts with multimodal brain and body signals to drive a diffusion transformer editor.

Paper: [arXiv:2507.05397](https://arxiv.org/abs/2507.05397)

LoongX is the first large-scale multimodal framework for brain-conditioned image editing.

Note:
LoongX directly instantiates the editing formulation f:(I,B)->I'.

---

## LoongX — Method Overview

```
EEG ────────┐
fNIRS ──────┤
PPG ────────┼──► CS3 encoders ──► Dynamic Gated Fusion ──► DiT editor ──► I'
Motion ─────┤                              ▲
Speech ─────┘                              │
                                    Input image I
```

**CS3 encoder** — cross-scale state-space modeling per modality  
**DGF** — learnable gates for adaptive fusion  
**DiT** — diffusion transformer for image editing

---

## LoongX — Modality Roles

| Modality | Contribution |
|----------|--------------|
| **EEG** | High-level semantic intent |
| **fNIRS** | Robust semantic representation |
| **PPG** | Engagement and physiological state |
| **Motion** | Contextual behavioral cues |
| **Speech** | Explicit semantic guidance (optional) |

Multimodal fusion captures **complementary** aspects of user intent.

---

## LoongX — L-Mind Dataset

| Property | Value |
|----------|-------|
| Samples | ~24,000 image-edit pairs |
| Subjects | 12 |
| Modalities | EEG, fNIRS, PPG, motion, speech |
| Task | Subject views source image and imagines the edit |

First dataset pairing **multimodal BCI signals** with image-editing intent.

---

## LoongX — Results

| Metric | Text baseline | Neural only | Neural + speech |
|--------|---------------|-------------|-----------------|
| **CLIP-I** | 0.6558 | **0.6605** | — |
| **DINO** | 0.4636 | **0.4812** | — |
| **CLIP-T** | 0.2549 | — | **0.2588** |

**Key finding:** neural signals alone can match or exceed text-driven editing on visual alignment metrics.

---

## LoongX — Takeaways

- Brain signals can **directly guide** image editing
- Multimodal fusion improves robustness and semantics
- Neural + speech is **complementary**, not redundant
- Hands-free creative tools are becoming **feasible**

---

## Limitations (Current State)

- Abstract or fine-grained instructions remain difficult
- Requires specialized sensing hardware
- Neural intent is hard to interpret and debug
- Generalization to unseen edit types is unclear

---

## Future Directions

- **Real-time** interactive editing loops
- **VR / AR** editing environments
- **Personalized** models per user
- Additional modalities: eye tracking, EMG, higher-density EEG
- Stronger **reference preservation** and edit controllability

---

## Summary

| | |
|---|---|
| **Task** | $f: (I, B) \rightarrow I'$ — decode intended edits |
| **Related to** | Reconstruction and Generation (both $f: B \rightarrow I'$) |
| **Key distinction** | Reference image as input; signals encode *change*, not content |
| **Promise** | Accessible, hands-free, brain-guided image editing |
| **Example** | LoongX — multimodal BCI + diffusion transformer |

---

# Thank You

**Vision-Brain Modeling** knowledge base

Questions?

Note:
Point audience to the docs site and LoongX paper for deeper reading.
