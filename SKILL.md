---
name: genpark-personal-agent-acoustic-efferent-contralateral-suppression-skill
version: 1.0.0
description: Zero-dependency sovereign personal agent skill for calculating Medial Olivocochlear (MOC) Efferent Contralateral Suppression of Otoacoustic Emissions (CAS-OAE), speech-in-noise gating, and acoustic protective resilience.
author: AlphaPark Inc.
license: Apache-2.0
tags:
  - personal-agent
  - ai-agent
  - openclaw
  - genpark
  - mcp
  - mcp-server
  - model-context-protocol
  - python
  - zero-dependency
  - wellness
  - productivity
  - production-ready
metadata:
  openclaw_compatible: true
  hermes_compatible: true
  zero_dependency: true
---

# Acoustic MOC Efferent Contralateral Suppression Skill

A sovereign personal agent capability for assessing brainstem olivocochlear efferent feedback, outer hair cell gain damping, contralateral acoustic stimulation (CAS-OAE), and speech-in-noise intelligibility.

## Core Capabilities
- **Contralateral Suppression Magnitude**: Quantifies the decibel drop ($\Delta\text{Amp} = \text{Amp}_{baseline} - \text{Amp}_{conditioned}$) in otoacoustic emission amplitude induced by contralateral broadband noise.
- **Medial Olivocochlear (MOC) Integrity**: Evaluates the integrity of the crossed and uncrossed olivocochlear bundle originating in the superior olivary complex.
- **Auditory Speech-in-Noise Gating**: Detects early loss of background noise suppression (< 0.6 dB), predisposing to cognitive listening fatigue in open offices.
- **Personalized Audio Environment Tuning**: Prescribes directional noise cancellation profiles and quiet recharge intervals.

## Fast Invocation
```python
from client import AcousticEfferentSuppressionClient

client = AcousticEfferentSuppressionClient()
res = client.evaluate_contralateral_suppression(
    baseline_oae_amplitude_db_spl=11.2,
    noise_conditioned_oae_amplitude_db_spl=9.4,
    contralateral_noise_db_spl=65.0
)
print("Suppression Magnitude:", res["suppression_magnitude_db"], "dB")
print("Efferent Score:", res["efferent_gating_score"], "/ 100")
```
