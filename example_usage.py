"""
Example Usage: Acoustic Medial Olivocochlear (MOC) Efferent Contralateral Suppression.
Demonstrates zero-dependency calculation of OAE suppression magnitude, auditory speech-in-noise gating, and protective scoring.
"""

from client import AcousticEfferentSuppressionClient


def main():
    client = AcousticEfferentSuppressionClient()
    print("=== Acoustic MOC Efferent Contralateral Suppression Demo ===")

    # Test Case 1: Healthy robust MOC efferent suppression
    res1 = client.evaluate_contralateral_suppression(
        baseline_oae_amplitude_db_spl=11.2,
        noise_conditioned_oae_amplitude_db_spl=9.4,
        contralateral_noise_db_spl=65.0,
        test_frequency_hz=2000
    )
    print("\nTest Case 1: Robust MOC Efferent Suppression (2 kHz)")
    print(f"  Baseline OAE: {res1['baseline_oae_amplitude_db_spl']} dB SPL | Noise-Conditioned OAE: {res1['noise_conditioned_oae_amplitude_db_spl']} dB SPL")
    print(f"  Contralateral Noise: {res1['contralateral_noise_db_spl']} dB SPL")
    print(f"  Suppression Magnitude: {res1['suppression_magnitude_db']} dB")
    print(f"  Efferent Gating Score: {res1['efferent_gating_score']} / 100")
    print(f"  Classification: {res1['classification']}")
    print(f"  Physiological Interpretation: {res1['physiological_interpretation']}")
    print(f"  Actionable Guidance: {res1['actionable_guidance']}")

    # Test Case 2: Absent efferent suppression (speech-in-noise deficit)
    res2 = client.evaluate_contralateral_suppression(
        baseline_oae_amplitude_db_spl=7.8,
        noise_conditioned_oae_amplitude_db_spl=7.6,
        contralateral_noise_db_spl=65.0,
        test_frequency_hz=2000
    )
    print("\nTest Case 2: Blunted Efferent Inhibition Pattern")
    print(f"  Suppression Magnitude: {res2['suppression_magnitude_db']} dB")
    print(f"  Efferent Gating Score: {res2['efferent_gating_score']} / 100")
    print(f"  Classification: {res2['classification']}")
    print(f"  Actionable Guidance: {res2['actionable_guidance']}")


if __name__ == "__main__":
    main()
