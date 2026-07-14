# fNIRS

> Functional Near-Infrared Spectroscopy — portable hemodynamic imaging for naturalistic and wearable brain decoding.

---

## How fNIRS Works

fNIRS measures **changes in blood oxygenation** by detecting how near-infrared light is absorbed as it passes through the scalp and cortex:

1. Light sources emit near-infrared wavelengths (~650–950 nm) into the head.
2. Photodetectors record the light that scatters back after passing through tissue.
3. **Oxyhemoglobin (HbO)** and **deoxyhemoglobin (HbR)** have distinct absorption spectra.
4. Neural activity increases local metabolic demand, producing hemodynamic changes similar to the BOLD signal in fMRI.

Because fNIRS relies on the same neurovascular coupling as fMRI, it captures a related but more localized hemodynamic response.

---

## Technical Specifications

| Property | Typical Value |
|----------|--------------|
| Spatial resolution | ~1–3 cm (continuous-wave); ~1 cm (high-density systems) |
| Temporal resolution | ~0.1–10 Hz (sampling rate dependent) |
| Hemodynamic lag | ~4–6 s after stimulus |
| Penetration depth | ~1–3 cm (cortical surface) |
| Number of channels | 8–100+ (source-detector pairs) |
| Cost | $10,000–$200,000 |
| Portability | High (wearable systems available) |

---

## Strengths

- **Non-invasive** and safe for repeated, long-duration sessions.
- **Portable and wearable** — compatible with naturalistic tasks and real-world use.
- **Lower cost** than fMRI or MEG.
- Tolerates moderate head movement better than many fMRI setups.
- Sensitive to **superficial cortical hemodynamics** with good temporal sampling relative to fMRI.
- Suitable for populations where MRI is difficult (infants, clinical bedside monitoring).

---

## Limitations

- **Limited depth** — primarily measures superficial cortex; subcortical activity is not accessible.
- **Lower spatial resolution** than fMRI or ECoG.
- **Hemodynamic lag** — indirect and slow proxy for neural activity.
- Susceptible to motion, hair, skin, and systemic physiological artifacts (heartbeat, respiration).
- **Sparse coverage** — only sampled regions between source-detector pairs are measured.
- Less established than fMRI or EEG for large-scale visual decoding benchmarks.

---

## Key fNIRS Datasets for Brain Decoding

| Dataset | Subjects | Stimuli | Channels | Notes |
|---------|----------|---------|----------|-------|
| **OpenNeuro fNIRS collections** | Various | Cognitive/motor tasks | 8–50+ | Public repository; limited natural-image decoding |
| **Mental imagery fNIRS** | Various | Imagined movement/objects | 16–32 | Common BCI paradigm; semantic labels only |
| **Visual perception fNIRS** | Various | Simple shapes/categories | 20–40 | Smaller scale than THINGS or NSD |

fNIRS remains less common than fMRI or EEG for natural-image brain decoding, but wearable hemodynamic sensing is an active area for lightweight BCIs.

---

## fNIRS in Brain Decoding Pipelines

### Preprocessing

- **Optical density conversion**: Transform raw light intensity into attenuation changes.
- **Motion correction**: Spline interpolation, wavelet filtering, or PCA-based artifact removal.
- **Hemodynamic separation**: Extract HbO and HbR time series via modified Beer-Lambert law.
- **Filtering**: Band-pass filtering to remove drift and cardiac/respiratory noise.

### Feature Extraction and Modeling

- **HRF modeling**: Convolve stimulus onsets with a hemodynamic response function, similar to fMRI GLM.
- **Windowed features**: Mean HbO/HbR amplitude in task-relevant time windows.
- **Learned encoders**: MLPs, CNNs, or RNNs on channel time series for classification or embedding prediction.

Because fNIRS and fMRI both measure hemodynamics, many fMRI decoding ideas transfer conceptually — though fNIRS typically offers fewer channels and lower spatial precision.

---

## fNIRS vs. fMRI

| Aspect | fNIRS | fMRI |
|--------|-------|------|
| Signal type | Hemodynamic (HbO/HbR) | Hemodynamic (BOLD) |
| Spatial resolution | ~cm | ~mm |
| Temporal resolution | ~0.1–10 Hz | ~0.3–1 Hz (TR) |
| Coverage | Superficial cortex only | Whole brain |
| Cost | Moderate | Very high |
| Portability | High | None (fixed scanner) |
| Naturalistic use | Strong | Limited (scanner environment) |

---

## Representative fNIRS Papers

| Paper | Year | Task | Key Idea |
|-------|------|------|---------|
| Cui et al. | 2011 | Review | Foundational overview of fNIRS for brain-computer interfaces |
| Naseer & Hong | 2015 | Classification | Motor imagery decoding with fNIRS |
| Shin et al. | 2018 | Classification | Deep learning for fNIRS-based BCI |
| Koo et al. | 2021 | Mental imagery | fNIRS decoding of visual imagery categories |
| Hu et al. | 2023 | Representation | fNIRS feature learning for cognitive state decoding |
