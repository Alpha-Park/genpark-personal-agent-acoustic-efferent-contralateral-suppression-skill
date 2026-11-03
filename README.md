# Acoustic MOC Efferent Contralateral Suppression Skill

[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Zero Dependencies](https://img.shields.io/badge/zero--dependencies-standard--lib-brightgreen.svg)](requirements.txt)
[![MCP Protocol Ready](https://img.shields.io/badge/mcp-protocol--ready-orange.svg)](mcp_server.py)
[![OpenClaw Certified](https://img.shields.io/badge/openclaw-certified-purple.svg)](SKILL.md)

Zero-dependency sovereign personal agent skill for non-invasive evaluation of Medial Olivocochlear (MOC) Efferent Contralateral Suppression of Otoacoustic Emissions (CAS-OAE), speech-in-noise gating, and auditory protective resilience.

```mermaid
flowchart TD
    BaselineOAE["Baseline Otoacoustic Emission Recording (DPOAE / TEOAE)"] --> NoiseCondition["Contralateral Broadband Noise Stimulation (60-65 dB SPL)"]
    NoiseCondition --> SOC_MOC["Superior Olivary Complex Medial Olivocochlear Bundle Activation"]
    SOC_MOC --> OHCDamp["Cochlear Outer Hair Cell Somatic Electromotility Damping"]
    OHCDamp --> DeltaAmp["Contralateral Suppression Magnitude (Delta Amp in dB)"]
    DeltaAmp --> AuditoryGating["Auditory Speech-in-Noise Gating & Acoustic Guarding Engine"]
    AuditoryGating --> Agent["OpenClaw / Hermes Personal Agent Sound Shaping"]
```

## Features
- **Deterministic Math**: Pure Python standard library implementation with zero external dependencies.
- **Auditory Neurophysiology Standards**: Formulates contralateral acoustic stimulation suppression, baseline signal-to-noise gating, and MOC gain reduction.
- **Cocktail Party Problem & Listening Fatigue**: Identifies subclinical central auditory processing deficits in noisy environments.
- **Model Context Protocol (MCP)**: Native JSON-RPC tool integration for LLMs and autonomous agents.

## Quickstart

```python
from client import AcousticEfferentSuppressionClient

client = AcousticEfferentSuppressionClient()
result = client.evaluate_contralateral_suppression(
    baseline_oae_amplitude_db_spl=11.2,
    noise_conditioned_oae_amplitude_db_spl=9.4,
    contralateral_noise_db_spl=65.0
)
print("Suppression Magnitude:", result["suppression_magnitude_db"], "dB")
print("Efferent Score:", result["efferent_gating_score"])
print("Classification:", result["classification"])
```

## License
Apache-2.0
