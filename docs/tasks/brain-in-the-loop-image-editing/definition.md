# Definition

> Learn an editing function $f: (I, B) \rightarrow I'$ that maps an observed image $I$ and brain signals $B$ recorded while the subject imagines modifications to $I$ into an edited image $I'$ matching the subject's intended changes.

<div align="center">

```mermaid
graph TD
    I["I — Observed Image"] -->|presented to| U["U — Subject"]
    U -->|imagines modifications| B["B — Brain Signals"]

    I -->|input to| F["f — Editing Function"]
    B -->|input to| F

    F -->|predicts| IP["I' — Edited Image"]
    IP -->|replaces| I

    style I fill:#1565c0,color:#fff,stroke:#0d47a1,stroke-width:2px
    style U fill:#6a1b9a,color:#fff,stroke:#4a148c,stroke-width:2px
    style B fill:#2e7d32,color:#fff,stroke:#1b5e20,stroke-width:2px
    style F fill:#37474f,color:#fff,stroke:#263238,stroke-width:2px
    style IP fill:#bf360c,color:#fff,stroke:#7f0000,stroke-width:2px
```

</div>
