"""
Example usage for Cutaneous Cutometer Skin Viscoelasticity Skill.
"""

from client import CutometerViscoelasticityClient


def main():
    client = CutometerViscoelasticityClient()

    print("--- Case 1: Preserved Youthful Skin Viscoelasticity ---")
    healthy_case = client.evaluate_elasticity(
        immediate_extensibility_ue_mm=0.22,
        viscoelastic_creep_uv_mm=0.045,
        elastic_recovery_ur_mm=0.19,
        anatomical_site="Cheek",
        patient_age_years=26
    )
    print("Gross Elasticity (R2):", healthy_case["biomechanical_ratios"]["r2_gross_elasticity"])
    print("Net Elasticity (R5):", healthy_case["biomechanical_ratios"]["r5_net_elasticity"])
    print("Viscoelastic Ratio (R6):", healthy_case["biomechanical_ratios"]["r6_viscoelastic_ratio"])
    print("Biomechanical Status:", healthy_case["clinical_assessment"]["biomechanical_status"])
    print("Pathophysiology:", healthy_case["clinical_assessment"]["pathophysiology_summary"])
    print()

    print("--- Case 2: Severe Cutaneous Photoaging / Solar Elastosis ---")
    photoaged_case = client.evaluate_elasticity(
        immediate_extensibility_ue_mm=0.18,
        viscoelastic_creep_uv_mm=0.095,
        elastic_recovery_ur_mm=0.12,
        anatomical_site="Dorsal Hand",
        patient_age_years=68
    )
    print("Gross Elasticity (R2):", photoaged_case["biomechanical_ratios"]["r2_gross_elasticity"])
    print("Viscoelastic Ratio (R6):", photoaged_case["biomechanical_ratios"]["r6_viscoelastic_ratio"])
    print("Biomechanical Status:", photoaged_case["clinical_assessment"]["biomechanical_status"])
    print("Pathophysiology:", photoaged_case["clinical_assessment"]["pathophysiology_summary"])
    print()

    print("--- Case 3: Systemic Sclerosis / Severe Dermal Fibrosis ---")
    sclerosis_case = client.evaluate_elasticity(
        immediate_extensibility_ue_mm=0.065,
        viscoelastic_creep_uv_mm=0.02,
        elastic_recovery_ur_mm=0.05,
        anatomical_site="Forearm",
        patient_age_years=52
    )
    print("Final Distension (Uf):", sclerosis_case["deformation_amplitudes_mm"]["uf_final_distension"], "mm")
    print("Biomechanical Status:", sclerosis_case["clinical_assessment"]["biomechanical_status"])
    print("Pathophysiology:", sclerosis_case["clinical_assessment"]["pathophysiology_summary"])


if __name__ == "__main__":
    main()
