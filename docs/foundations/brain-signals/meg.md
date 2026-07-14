# MEG

> Magnetoencephalography — high spatial and temporal resolution for non-invasive brain decoding.

---

## How MEG Works

MEG measures the **magnetic fields** produced by intraneuronal electrical currents:

1. Electrical currents in cortical pyramidal neurons generate tiny magnetic fields (~10–100 fT).
2. Superconducting quantum interference devices (**SQUIDs**) or optically pumped magnetometers (**OPMs**) detect these fields.
3. Magnetic fields pass through the skull without distortion (unlike EEG potentials).

---

## Technical Specifications

| Property | Typical Value |
|----------|--------------|
| Spatial resolution | ~mm (after source localization) |
| Temporal resolution | ~ms |
| Sampling rate | 600–2400 Hz |
| Number of sensors | 100–400 sensors |
| Cost | ~$2–5M (equipment + shielded room) |
| Portability | Fixed lab (traditional); OPM-based systems enable head movement |

---

## Strengths

- **Millisecond temporal resolution** — same as EEG.
- **Better spatial resolution** than EEG — magnetic fields are not smeared by the skull.
- Complementary to EEG (detects tangential sources EEG misses).
- Naturalistic paradigms possible (subjects can watch videos, etc.).

---

## Limitations

- Extremely expensive to install and maintain.
- Requires a **magnetically shielded room (MSR)**.
- Subjects must remain still (traditional SQUID-based systems).
- Primarily sensitive to **tangential** sources (gyral crowns may be missed).
- Less accessible than EEG for large-scale or clinical studies.

---

## Key MEG Datasets for Brain Decoding

| Dataset | Subjects | Stimuli | Sensors | Notes |
|---------|----------|---------|---------|-------|
| **THINGS-MEG** | 4 | 22,248 object images | 306 | Paired with THINGS-EEG and THINGS-fMRI |
| **MEG-MASC** | 27 | Naturalistic reading/listening | 208 | Language perception paradigm |
| **Cichy et al. MEG** | Various | Object images | 306 | Widely cited in representational similarity analysis |

---

## MEG Source Localization

Raw MEG sensor signals can be projected to cortical source space:

1. **Beamforming** (e.g., LCMV): Spatial filters that isolate sources at specific locations.
2. **Minimum norm estimation (MNE)**: Distributed source model on a cortical mesh.
3. **DICS**: Dynamic Imaging of Coherent Sources — frequency-domain beamformer.

After source localization, MEG spatial resolution approaches fMRI at millisecond timescales.

---

## MEG vs. EEG in Brain Decoding

| Aspect | MEG | EEG |
|--------|-----|-----|
| Skull distortion | None | High |
| Spatial resolution | Better (~mm after source loc.) | Worse (~cm) |
| Temporal resolution | ~ms | ~ms |
| Cost | Very high | Low |
| Portability | Low (fixed lab) | High |
| Artifact sensitivity | Motion, cardiac | Eye, muscle |

---

## Representative MEG Decoding Papers

| Paper | Year | Task | Key Idea |
|-------|------|------|---------|
| Cichy et al. | 2016 | RSA | MEG reveals temporal hierarchy of visual processing |
| Gifford et al. (THINGS-MEG) | 2022 | Classification + RSA | Large-scale MEG dataset for object decoding |
| BReAD | 2025 | Retrieval + Reconstruction | Retrieval-augmented diffusion for MEG/EEG |
