"""
Acoustic Medial Olivocochlear (MOC) Efferent Contralateral Suppression Engine.
Provides deterministic, zero-dependency modeling of Contralateral Acoustic Stimulation (CAS) OAE suppression,
efferent attenuation magnitude (dB), auditory speech-in-noise gating, and acoustic trauma protection.
"""

from typing import Dict, Any, List, Optional


class AcousticEfferentSuppressionClient:
    """
    Deterministic client for calculating Medial Olivocochlear (MOC) Efferent Contralateral Suppression.
    Assesses superior olivary complex uncrossed/crossed olivocochlear bundle feedback,
    cochlear outer hair cell (OHC) electromotile gain damping, and central auditory processing integrity.
    """

    def __init__(self):
        pass

    def evaluate_contralateral_suppression(
        self,
        baseline_oae_amplitude_db_spl: float,
        noise_conditioned_oae_amplitude_db_spl: float,
        contralateral_noise_db_spl: float = 65.0,
        test_frequency_hz: int = 2000
    ) -> Dict[str, Any]:
        """
        Calculates MOC efferent suppression magnitude: Delta_Amp = Amp_baseline - Amp_conditioned.
        Normative values (with 60-65 dB SPL contralateral broadband noise):
        - Baseline OAE: 3.0 - 18.0 dB SPL
        - Suppression Magnitude: 1.0 - 2.8 dB
        - Suppression < 0.6 dB suggests efferent auditory processing deficit
        """
        if contralateral_noise_db_spl <= 0:
            return {"error": "Contralateral noise level must be positive"}

        # Suppression magnitude (dB)
        suppression_db = round(baseline_oae_amplitude_db_spl - noise_conditioned_oae_amplitude_db_spl, 2)

        # MOC Efferent Gating Score (0 - 100)
        score = 80.0
        if 1.0 <= suppression_db <= 2.5:
            score += 15.0
        elif 0.6 <= suppression_db < 1.0 or 2.5 < suppression_db <= 3.2:
            score += 5.0
        elif suppression_db < 0.2:
            score -= 30.0  # Absent efferent suppression
        elif suppression_db < 0.5:
            score -= 15.0
        elif suppression_db < 0:
            score -= 35.0  # Paradoxical efferent enhancement

        if baseline_oae_amplitude_db_spl >= 6.0:
            score += 5.0
        elif baseline_oae_amplitude_db_spl < 2.0:
            score -= 10.0

        efferent_score = round(min(100.0, max(5.0, score)), 1)

        if efferent_score >= 85.0 and suppression_db >= 1.0:
            tier = "OPTIMAL_MOC_EFFERENT_SUPPRESSION"
            interp = f"Robust medial olivocochlear suppression ({suppression_db} dB attenuation at {test_frequency_hz} Hz); intact superior olivary complex efferent feedback loop."
            guidance = "Superior speech-in-noise perception and native cochlear protection against environmental acoustic overexposure."
        elif suppression_db < 0.5:
            tier = "REDUCED_OR_ABSENT_EFFERENT_INHIBITION"
            interp = f"Blunted efferent suppression ({suppression_db} dB < 0.6 dB); reflects weakened medial olivocochlear bundle damping onto cochlear outer hair cells."
            guidance = "Efferent auditory vulnerability. Susceptible to cocktail party speech-in-noise exhaustion; use directional noise-cancelling audio."
        else:
            tier = "MODERATE_EFFERENT_ATTENUATION"
            interp = f"Moderate efferent suppression magnitude ({suppression_db} dB); acceptable cochlear gain control."
            guidance = "Satisfactory olivocochlear tone. Maintain routine hearing hygiene in loud open-plan workspaces."

        return {
            "test_frequency_hz": test_frequency_hz,
            "baseline_oae_amplitude_db_spl": baseline_oae_amplitude_db_spl,
            "noise_conditioned_oae_amplitude_db_spl": noise_conditioned_oae_amplitude_db_spl,
            "contralateral_noise_db_spl": contralateral_noise_db_spl,
            "suppression_magnitude_db": suppression_db,
            "efferent_gating_score": efferent_score,
            "classification": tier,
            "physiological_interpretation": interp,
            "actionable_guidance": guidance
        }
