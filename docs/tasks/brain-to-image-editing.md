# Brain-to-Image Editing

---

## Definition

Learn an editing function $f: (I, B) \rightarrow I'$ that maps an observed image $I$ and brain signals $B$ recorded while the subject imagines modifications to $I$ into an edited image $I'$ matching the subject's intended changes.

<div align="center">

```mermaid
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
```

</div>

---

## Motivation

- Existing brain-to-image reconstruction methods only recover perceived or imagined images.
- Many applications require modifying an existing image rather than generating a new one.
- Reconstructing an entire image is inefficient for localized or attribute-level changes.
- Brain-to-image editing aims to decode the user's intended modifications to a reference image.

---

## Significance

- Shifts brain decoding from understanding **what a subject sees** to **how a subject wants an image to change**.
- Introduces intention-driven and interactive brain-computer interfaces.
- Enables finer-grained control than traditional reconstruction tasks.
- Establishes a foundation for brain-guided creative and assistive systems.

---

## Applications

- **Hands-Free Image Editing**: Allows users to edit images without keyboards, mice, touchscreens, or text prompts.
- **Accessibility Tools**: Provides creative interfaces for users with motor or speech impairments.
- **Brain-Guided Creative Systems**: Enables image manipulation driven directly by cognitive intent.
- **Adaptive Human-AI Interfaces**: Allows AI systems to infer user preferences from neural feedback.

---

## Challenges

- **Intent Decoding**: The model must infer the desired change rather than the current visual content.
- **Reference Preservation**: Unmodified regions of the image should remain unchanged.
- **Weak Neural Signals**: Editing intent is often subtle and difficult to measure reliably.
- **Semantic Ambiguity**: Similar neural patterns may correspond to multiple possible edits.
