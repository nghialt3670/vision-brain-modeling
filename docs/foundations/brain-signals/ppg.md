# PPG

> Photoplethysmography — wearable peripheral sensing of blood volume pulse for physiological state and multimodal BCI fusion.

---

## How PPG Works

PPG measures **changes in blood volume** in peripheral tissue by detecting how light is absorbed as it passes through the skin:

1. A light-emitting diode (LED) illuminates the skin (typically at the wrist, finger, or earlobe).
2. A photodetector records reflected or transmitted light intensity.
3. Each **cardiac cycle** changes local blood volume, producing a pulsatile waveform.
4. Derived features — heart rate, heart rate variability (HRV), and pulse amplitude — reflect autonomic and cognitive state.

Unlike fNIRS or fMRI, PPG does not directly measure cortical activity. It captures **peripheral autonomic responses** that often co-vary with attention, effort, and engagement during visual and cognitive tasks.

---

## Technical Specifications

| Property | Typical Value |
|----------|--------------|
| Spatial resolution | N/A (single peripheral site) |
| Temporal resolution | ~ms (raw waveform); ~1 Hz (derived HR) |
| Sampling rate | 25–512 Hz (device dependent) |
| Common sites | Wrist, finger, earlobe, forehead |
| Channels | 1–4 (typical in wearable BCIs) |
| Cost | $50–$500 (consumer); integrated in many wearables |
| Portability | Very high |

---

## Strengths

- **Extremely low cost** and widely available in consumer wearables.
- **Continuous, unobtrusive monitoring** during long sessions.
- **High temporal resolution** for cardiac rhythm and HRV features.
- Robust marker of **arousal, stress, and cognitive load**.
- Easy to synchronize with EEG, fNIRS, and behavioral recordings.
- Useful for **multimodal fusion** when neural signals alone are ambiguous.

---

## Limitations

- **Not a direct brain signal** — measures peripheral hemodynamics, not cortical activity.
- **No spatial information** about neural processing.
- Susceptible to motion, pressure, temperature, and ambient light artifacts.
- Skin tone and sensor placement affect signal quality.
- Limited specificity — similar PPG patterns can reflect many cognitive states.
- Rarely sufficient alone for fine-grained visual decoding or image editing.

---

## Key PPG Datasets for Brain Decoding

| Dataset | Subjects | Stimuli | Channels | Notes |
|---------|----------|---------|----------|-------|
| **[LoongX](../resources/datasets/loongx.md)** | 12 | ~24,000 image-edit pairs | 1 (wrist) | Multimodal EEG + fNIRS + PPG for brain-driven editing |
| **OpenNeuro / wearables** | Various | Cognitive tasks | 1 | Often paired with EEG; limited visual-decoding benchmarks |
| **Consumer wearable studies** | Various | Rest / task blocks | 1 | HRV and engagement labels; not image reconstruction |

PPG is most relevant in **multimodal BCI** settings where physiological state complements neural intent signals.

---

## PPG in Brain Decoding Pipelines

### Preprocessing

- **Band-pass filtering**: Remove motion drift and high-frequency noise (typical range ~0.5–8 Hz for pulse extraction).
- **Peak detection**: Identify systolic peaks to compute inter-beat intervals and heart rate.
- **Artifact rejection**: Discard segments corrupted by motion or poor skin contact.

### Feature Extraction

- **Heart rate (HR)** and **heart rate variability (HRV)**: Time-domain (RMSSD, SDNN) and frequency-domain (LF/HF ratio) features.
- **Pulse amplitude**: Proxy for vascular tone and arousal.
- **Windowed statistics**: Mean, variance, and slope over task-aligned epochs.

### Role in Multimodal Fusion

In systems such as [LoongX](../../works/papers/zhou-et-al-2026.md), PPG is encoded alongside EEG and fNIRS to capture **user engagement and physiological state** — complementing semantic intent from neural signals rather than replacing them.

---

## PPG vs. fNIRS

| Aspect | PPG | fNIRS |
|--------|-----|-------|
| Measurement site | Peripheral (wrist, finger) | Head (cortical surface) |
| Signal type | Blood volume pulse | Cortical HbO/HbR |
| Spatial resolution | None | ~cm |
| Neural specificity | Low (autonomic proxy) | Medium (local hemodynamics) |
| Cost | Very low | Moderate |
| Primary use in BCI | Arousal / engagement | Spatial intent / cognitive load |

---

## Representative PPG Papers

| Paper | Year | Task | Key Idea |
|-------|------|------|---------|
| Allen | 2007 | Review | Photoplethysmography and its application in clinical physiological measurement |
| Scholkmann et al. | 2014 | Review | fNIRS and PPG for neuroimaging and BCI |
| Zhou et al. (LoongX) | 2025 | Image editing | Multimodal EEG/fNIRS/PPG fusion for brain-driven editing |
| Plews et al. | 2013 | HRV analysis | Heart rate variability as marker of autonomic state |
| Elgendi et al. | 2019 | Review | PPG signal analysis for healthcare applications |
