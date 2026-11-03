"""
MCP Server implementation for Cutaneous Cutometer Skin Viscoelasticity Skill.
Exposes standard FastMCP-compatible tools for skin biomechanical deformation and elasticity profiling.
"""

import sys
import json
from typing import Dict, Any, Optional
from client import CutometerViscoelasticityClient


def evaluate_skin_viscoelasticity(
    immediate_extensibility_ue_mm: float,
    viscoelastic_creep_uv_mm: float,
    elastic_recovery_ur_mm: float,
    suction_pressure_mbar: Optional[float] = 450.0,
    anatomical_site: Optional[str] = "Volar Forearm",
    patient_age_years: Optional[int] = 40
) -> str:
    """
    Evaluates cutaneous suction deformation, gross elasticity (R2), net elasticity (R5), and viscoelastic ratio (R6).
    Returns structured analysis of dermal elastic matrix integrity.
    """
    client = CutometerViscoelasticityClient()
    result = client.evaluate_elasticity(
        immediate_extensibility_ue_mm=immediate_extensibility_ue_mm,
        viscoelastic_creep_uv_mm=viscoelastic_creep_uv_mm,
        elastic_recovery_ur_mm=elastic_recovery_ur_mm,
        suction_pressure_mbar=suction_pressure_mbar,
        anatomical_site=anatomical_site,
        patient_age_years=patient_age_years
    )
    return json.dumps(result, indent=2)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--tools":
        tools = [
            {
                "name": "evaluate_skin_viscoelasticity",
                "description": "Calculates Cutometer skin deformation metrics (Ue, Uv, Uf, Ur) and elasticity ratios (R2 gross elasticity, R5 net elasticity, R6 viscoelastic ratio) to assess skin photoaging and dermal sclerosis.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "immediate_extensibility_ue_mm": {"type": "number", "description": "Immediate elastic distension in mm (normal: 0.10 - 0.35 mm)"},
                        "viscoelastic_creep_uv_mm": {"type": "number", "description": "Delayed viscoelastic creep in mm (normal: 0.03 - 0.12 mm)"},
                        "elastic_recovery_ur_mm": {"type": "number", "description": "Immediate elastic recovery in mm (normal: 0.08 - 0.28 mm)"},
                        "suction_pressure_mbar": {"type": "number", "description": "Suction negative pressure in mbar (default: 450 mbar)"},
                        "anatomical_site": {"type": "string", "description": "Anatomical site measured (default: 'Volar Forearm')"},
                        "patient_age_years": {"type": "integer", "description": "Patient age in years (default: 40)"}
                    },
                    "required": ["immediate_extensibility_ue_mm", "viscoelastic_creep_uv_mm", "elastic_recovery_ur_mm"]
                }
            }
        ]
        print(json.dumps(tools, indent=2))
    else:
        # Simple self-test
        client = CutometerViscoelasticityClient()
        test_res = client.evaluate_elasticity(
            immediate_extensibility_ue_mm=0.22,
            viscoelastic_creep_uv_mm=0.05,
            elastic_recovery_ur_mm=0.18
        )
        print("Self-test passed:")
        print(json.dumps(test_res, indent=2))
