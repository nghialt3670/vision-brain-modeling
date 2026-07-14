# Brain-to-Image Editing

## Decoding visual intent — not just visual content

<div class="hero-line"></div>

**Weekly research-direction report**

Note:
Welcome. This talk introduces brain-to-image editing: a setting where neural signals guide changes to an existing image rather than merely reconstructing what someone saw.

---

## Roadmap

<div class="roadmap">
  <div><b>01</b><span>Foundations</span><small>Signals, encoding &amp; decoding</small></div>
  <div><b>02</b><span>Related tasks</span><small>Reconstruction &amp; generation</small></div>
  <div><b>03</b><span>The problem</span><small>Brain-to-image editing</small></div>
  <div><b>04</b><span>Current state</span><small>LoongX case study</small></div>
  <div><b>05</b><span>Next steps</span><small>Research direction</small></div>
</div>

---

# 01 — Foundations

## What do brain signals let us model?

---

## Vision–Brain Modeling

<div class="split">
<div>

### A translation problem

Connect **neural activity** to meaningful visual representations.

</div>
<div class="signal-stack">
  <div><b>Encoding</b><span>image → predicted brain response</span></div>
  <div><b>Decoding</b><span>brain response → image, concept, or intent</span></div>
</div>
</div>

<p class="caption">This report focuses on decoding intent for brain-to-image editing.</p>

Note:
Encoding and decoding are the two established modelling directions. This report focuses on decoding intent.

---

## What can we measure?

| Modality | Measures | Spatial | Temporal | Cost | Invasiveness |
|---|---|---|---|---|---|
| **fMRI** | Blood oxygen changes (BOLD) | High | Low | Very high | Non-invasive |
| **EEG** | Electrical activity | Low | High | Low | Non-invasive |
| **MEG** | Magnetic fields | High | High | Very high | Non-invasive |
| **fNIRS** | Blood oxygen changes | Medium | Low | Moderate | Non-invasive |
| **PPG** | Blood volume pulse | None (peripheral) | High | Very low | Non-invasive |
| **ECoG** | Electrical activity on cortex | Very high | Very high | Very high | Invasive |

<p class="caption">Measurement choices determine the information available for decoding, as well as practical constraints on deployment.</p>

---

# 02 — Related tasks

## What has brain-to-image modelling already solved?

---

## Two established tasks

<div class="task-grid">
  <div class="task-card blue">
    <h3>Reconstruction</h3>
    <p class="formula">$f: B \rightarrow \hat{I}$</p>
    <p>Recover the image a person was shown.</p>
    <small>Ground truth exists → direct evaluation</small>
  </div>
  <div class="task-card purple">
    <h3>Generation</h3>
    <p class="formula">$f: B \rightarrow \hat{I}$</p>
    <p>Visualize imagery, dreams, or concepts.</p>
    <small>No single ground truth → ambiguous evaluation</small>
  </div>
</div>

---

## Reconstruction and generation

<div class="related-task-diagrams">
  <div>
    <h3>Reconstruction</h3>
<pre class="mermaid">
graph TD
    I["I — Visual Stimulus"] -->|presented to| U["U — Subject"]
    U -->|produces| B["B — Brain Signals"]
    B -->|input to| F["f — Reconstruction Function"]
    F -->|predicts| IP["I' — Reconstructed Image"]

    style I fill:#1565c0,color:#fff,stroke:#0d47a1,stroke-width:2px
    style U fill:#6a1b9a,color:#fff,stroke:#4a148c,stroke-width:2px
    style B fill:#2e7d32,color:#fff,stroke:#1b5e20,stroke-width:2px
    style F fill:#37474f,color:#fff,stroke:#263238,stroke-width:2px
    style IP fill:#bf360c,color:#fff,stroke:#7f0000,stroke-width:2px
</pre>
  </div>
  <div>
    <h3>Generation</h3>
<pre class="mermaid">
graph TD
    U["U — Subject"] -->|imagines or dreams| B["B — Brain Signals"]
    B -->|input to| F["f — Generation Function"]
    F -->|predicts| IP["I' — Generated Image"]

    style U fill:#6a1b9a,color:#fff,stroke:#4a148c,stroke-width:2px
    style B fill:#2e7d32,color:#fff,stroke:#1b5e20,stroke-width:2px
    style F fill:#37474f,color:#fff,stroke:#263238,stroke-width:2px
    style IP fill:#bf360c,color:#fff,stroke:#7f0000,stroke-width:2px
</pre>
  </div>
</div>

<p class="caption">Both tasks decode content from brain activity; editing introduces a reference image and decodes intended change.</p>

---

# 03 — Brain-to-image editing problem

## From recovering content to decoding change

---

## The central idea

> **Can a system infer how you want an image to change—directly from brain activity?**

<div class="three-cards">
  <div><strong>See</strong><br><span>an image</span></div>
  <div><strong>Imagine</strong><br><span>an edit</span></div>
  <div><strong>Create</strong><br><span>the revised image</span></div>
</div>

<p class="caption">The reference image provides context; neural signals communicate intent.</p>

---

## Editing changes the question

<div class="quote-stage">
  <p class="muted">Reconstruction &amp; generation ask</p>
  <h3>“What is in the subject’s mind?”</h3>
  <div class="arrow-down">↓</div>
  <p class="accent">Editing asks</p>
  <h2>“How should <em>this image</em> change?”</h2>
</div>

---

## Brain-to-image editing

<div class="editing-layout">
<div class="editing-copy">

### Definition

<p class="big-formula">f: (I, B) → I′</p>

Learn an editing function that maps an observed image <i>I</i> and brain signals <i>B</i>—recorded while the subject imagines modifications to <i>I</i>—into an edited image <i>I′</i> matching the subject’s intended changes.

<div class="io-points">
  <div><b>Input</b><span>Reference image + imagined edit signals</span></div>
  <div><b>Output</b><span>Intended edit with reference preservation</span></div>
</div>

</div>
<div class="editing-diagram">

<pre class="mermaid">
graph TD
    I["I — Observed Image"] -->|presented to| U["U — Subject"]
    U -->|imagines modifications| B["B — Brain Signals"]

    I -->|input to| F["f — Editing Function"]
    B -->|input to| F

    F -->|predicts| IP["I' — Edited Image"]

    style I fill:#1565c0,color:#fff,stroke:#0d47a1,stroke-width:2px
    style U fill:#6a1b9a,color:#fff,stroke:#4a148c,stroke-width:2px
    style B fill:#2e7d32,color:#fff,stroke:#1b5e20,stroke-width:2px
    style F fill:#37474f,color:#fff,stroke:#263238,stroke-width:2px
    style IP fill:#bf360c,color:#fff,stroke:#7f0000,stroke-width:2px
</pre>

</div>
</div>

---

## What makes the task hard?

<div class="challenge-grid">
  <div><b>01</b><h3>Decode change</h3><p>Infer the intended transformation, not just perceived content.</p></div>
  <div><b>02</b><h3>Preserve identity</h3><p>Keep everything outside the intended edit stable.</p></div>
  <div><b>03</b><h3>Handle ambiguity</h3><p>One neural pattern can support many plausible edits.</p></div>
  <div><b>04</b><h3>Work with noise</h3><p>Edit intent is subtle in low-signal neural measurements.</p></div>
</div>

---

## The non-negotiable constraint

### Change what matters. Preserve what does not.

<div class="preserve">
  <div><span class="dot edit"></span><b>Edited region</b><small>must follow decoded intent</small></div>
  <div><span class="dot keep"></span><b>Reference region</b><small>must remain recognizable and stable</small></div>
</div>

<p class="caption">Editing quality is a balance: semantic alignment × reference preservation.</p>

---

## Why this matters

<div class="impact-grid">
  <div><span>⌁</span><h3>Accessibility</h3><p>Creative control without a keyboard, mouse, or speech.</p></div>
  <div><span>✦</span><h3>Co-creation</h3><p>Make generative tools respond to subtle, pre-verbal intent.</p></div>
  <div><span>↻</span><h3>Adaptive AI</h3><p>Use neural feedback to refine outputs in an interaction loop.</p></div>
</div>

---

# 04 — Current state

## A first multimodal editing system

---

## Case study: LoongX

<p class="eyebrow">ZHOU ET AL. · NEURIPS 2025</p>

### Neural-driven image editing with multimodal signals

> A diffusion-transformer editor conditioned on brain and body signals—not text prompts alone.

[arXiv:2507.05397](https://arxiv.org/abs/2507.05397)

Note:
Position LoongX as a concrete implementation of f(I,B) → I′. It combines multiple signals, including optional speech, rather than assuming a single brain modality carries all intent.

---

## LoongX: from signals to an edit

<pre class="mermaid">
flowchart LR
    subgraph S["Multimodal signals"]
      direction TB
      GAP[" "]:::spacer
      E[EEG] ~~~ N[fNIRS] ~~~ P[PPG] ~~~ M[Motion] ~~~ V[Speech]
      GAP ~~~ E
    end
    S --> C["CS3 encoders"] --> G["Dynamic gated fusion"] --> D["DiT editor"] --> O["Edited image I′"]
    I["Reference image I"] --> D
    classDef signal fill:#2563eb,color:#fff,stroke:#1d4ed8
    classDef image fill:#0891b2,color:#fff,stroke:#0e7490
    classDef encoder fill:#0f766e,color:#fff,stroke:#115e59
    classDef fusion fill:#7c3aed,color:#fff,stroke:#6d28d9
    classDef editor fill:#be123c,color:#fff,stroke:#9f1239
    classDef output fill:#ea580c,color:#fff,stroke:#c2410c
    classDef spacer fill:transparent,stroke:transparent,color:transparent
    class E,N,P,M,V signal
    class I image
    class C encoder
    class G fusion
    class D editor
    class O output
    style S fill:#eff6ff,stroke:#60a5fa,color:#1d4ed8,stroke-width:2px
</pre>

<p class="caption"><b>CS3</b> models each modality at multiple scales · <b>gated fusion</b> weights their contributions · <b>DiT</b> generates the edit.</p>

---

## Different signals, complementary clues

| Signal | Primary role |
|---|---|
| **EEG + fNIRS** | Semantic intention and neural representation |
| **PPG + motion** | Engagement and behavioral context |
| **Speech (optional)** | Explicit semantic guidance |

<p class="caption">Fusion is useful because intent is distributed: no single signal is sufficient in every moment.</p>

---

## L-Mind dataset

<div class="stat-row">
  <div><strong>~24K</strong><span>image–edit pairs</span></div>
  <div><strong>12</strong><span>subjects</span></div>
  <div><strong>5</strong><span>signal modalities</span></div>
  <div><strong>1</strong><span>editing task</span></div>
</div>

<p class="caption">Subjects view a source image and imagine its intended transformation.</p>

---

## What the results suggest

| Metric | Text baseline | Neural only | Neural + speech |
|---|---:|---:|---:|
| **CLIP-I** · image alignment | 0.6558 | **0.6605** | — |
| **DINO** · visual similarity | 0.4636 | **0.4812** | — |
| **CLIP-T** · text alignment | 0.2549 | — | **0.2588** |

> **Takeaway:** neural signals can contribute useful editing guidance—and speech adds complementary information.

---

# 05 — Next steps

## From ideation to a focused research plan

---

## Current limitations

<div class="limit-list">
  <div><b>Fine-grained intent</b><span>Abstract or precise instructions remain difficult.</span></div>
  <div><b>Hardware burden</b><span>Reliable sensing is still specialized and inconvenient.</span></div>
  <div><b>Generalization</b><span>Performance on unseen users and edit types is uncertain.</span></div>
  <div><b>Interpretability</b><span>It is hard to diagnose why a decoded edit was wrong.</span></div>
</div>

---

## Next steps for this research direction

<div class="future-path">
  <div><b>01 · Build foundations</b><span>Strengthen neural-science knowledge and deep-learning fundamentals, with emphasis on generative image models.</span></div>
  <div><b>02 · Map the literature</b><span>Review editing papers alongside reconstruction and generation: tasks, datasets, protocols, and evaluation.</span></div>
  <div><b>03 · Synthesize approaches</b><span>Document recurring representations, conditioning strategies, model designs, and limitations; then identify a tractable research gap.</span></div>
</div>

<p class="caption">Near-term deliverable: a structured research map that connects foundations, papers, common approaches, and open questions.</p>

---

# Closing summary

## Research direction: brain-to-image editing

<div class="summary-stack">
  <div><b>Problem:</b> decode an intended modification from brain signals while preserving the reference image.</div>
  <div><b>Current state:</b> multimodal work such as LoongX demonstrates early feasibility, but robust editing remains open.</div>
  <div><b>Immediate priority:</b> strengthen foundations, review related-task literature, and map common approaches before defining a focused research question.</div>
</div>

<p class="subtitle">Discussion</p>

Note:
Close by restating that this is an ideation-stage direction. Invite discussion on the most promising foundational topics, papers, and possible research gaps.
