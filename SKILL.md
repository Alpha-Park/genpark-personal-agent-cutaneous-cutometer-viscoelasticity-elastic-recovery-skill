---
name: genpark-personal-agent-cutaneous-cutometer-viscoelasticity-elastic-recovery-skill
description: Evaluates cutaneous mechanical deformation, viscoelastic creep, and elastic recoil ratios (R2 gross elasticity, R5 net elasticity, R6 viscoelastic ratio) via non-invasive Cutometer suction elastometry.
---

# Cutaneous Cutometer Skin Viscoelasticity & Suction Mechanical Deformation Skill

This skill computes dermatological biomechanical parameters from suction-induced skin deformation curves to quantify cutaneous aging, solar elastosis, and dermal sclerosis.

## Core Capabilities
- Evaluates immediate elastic deformation ($U_e$), delayed viscoelastic creep ($U_v$), and final distension ($U_f$).
- Computes gross elasticity ($R_2 = U_r / U_f$, normal $0.65 - 0.85$).
- Computes net elasticity ($R_5 = U_r / U_e$, normal $0.70 - 0.90$).
- Computes viscoelastic ratio ($R_6 = U_v / U_e$, normal $0.15 - 0.35$).
- Distinguishes photoaging elastosis from fibrotic dermal induration (scleroderma).

## Zero-Mock Architecture
Standard Python standard library only with zero external dependencies.
