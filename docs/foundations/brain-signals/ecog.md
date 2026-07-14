# ECoG

> Electrocorticography — invasive but high-fidelity brain recording for foundational vision neuroscience.

---

## How ECoG Works

ECoG (also called **intracranial EEG**, iEEG) places electrode grids or strips directly on the **cortical surface** or depth electrodes within brain tissue:

1. Electrodes are surgically implanted, typically during pre-surgical evaluation for epilepsy.
2. Recordings capture local field potentials (**LFPs**) from cortical columns directly beneath each electrode.
3. No skull filtering — signal quality is dramatically higher than scalp EEG.

---

## Technical Specifications

| Property | Typical Value |
|----------|--------------|
| Spatial resolution | ~1–10 mm (electrode spacing) |
| Temporal resolution | ~ms |
| Sampling rate | 1000–30,000 Hz |
| Coverage | Limited to implanted region |
| Invasiveness | Highly invasive (neurosurgery required) |

---

## Strengths

- **Highest signal quality** of all non-implanted cortical recording methods.
- Minimal noise; no skull or scalp attenuation.
- Access to **high-gamma oscillations** (70–200 Hz) — strongly correlated with spiking activity.
- Enables fine-grained spatial mapping of cortical function (e.g., face-selective electrodes).

---

## Limitations

- **Invasive** — only available in clinical contexts (epilepsy surgery workup or research implants).
- Limited cortical coverage — only regions near electrodes are sampled.
- Ethical constraints on experimental design (patient welfare is primary).
- Cannot cover subcortical structures without depth electrodes.

---

## ECoG in Vision Research

ECoG has contributed foundational knowledge to visual neuroscience:

- **Object selectivity**: Identified face-selective and body-selective patches in IT cortex.
- **High-gamma signals**: High-gamma power (70–200 Hz) tracks image category and fine-grained object features with high fidelity.
- **Temporal dynamics**: Revealed the precise temporal sequence of visual feature processing at millisecond resolution.
- **Speech/language BCIs**: ECoG-based systems have achieved real-time decoding of imagined speech, directly informing vision-brain modeling approaches.

---

## ECoG vs. Other Modalities

| Aspect | ECoG | fMRI | EEG |
|--------|------|------|-----|
| Signal quality | Excellent | Good | Fair |
| Temporal resolution | ~ms | ~s | ~ms |
| Spatial resolution | ~mm | ~1–2 mm | ~cm |
| Invasiveness | High | None | None |
| Practical for BCI | Limited (implants) | No | Yes |

---

## Representative ECoG Vision Papers

| Paper | Year | Task | Key Idea |
|-------|------|------|---------|
| Yoshor et al. | 2007 | Retinotopy | ECoG maps visual field in V1–V4 |
| Winawer et al. | 2013 | Spatial vision | High-gamma tracks spatial frequency |
| Yamins & DiCarlo | 2016 | Object representation | ECoG validates DNN hierarchy in IT |
| Chang & Anumanchipalli | 2019 | Speech decoding | ECoG → synthesized speech |
| Ruber et al. | 2022 | Face recognition | ECoG reveals temporal dynamics of FFA |
