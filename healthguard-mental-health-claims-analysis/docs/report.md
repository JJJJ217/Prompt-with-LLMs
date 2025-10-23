# HealthGuard Mental Health Claims — One-Page Report

## Executive Summary
Claims rose ~40% (2023–2025) while 2019-era models underpriced risk. Key drivers are post‑pandemic demand, telehealth‑enabled utilization, coding/diagnosis drift, and inflation. Approval rates differ markedly (Sydney ~85% vs Regional NSW ~62%), and readmissions vary by demographic, signalling access and process variation. We propose a focused set of model, data, and governance upgrades.

## Reasoning Summary
We considered competing hypotheses: demand shift (prevalence, stigma), access via telehealth, coding/inflation drift, and regional process/access differences. Trend charts and annual totals support a sustained post‑2023 utilization rise; regional approvals and demographics visuals indicate material access/process variation. Coding mix and inflation plausibly amplify costs beyond utilization alone. We judge demand + telehealth + coding/inflation as primary drivers, with regional variation moderating realized approvals and costs. Residual uncertainty stems from sample size, missing provider/network details, and unobserved severity.

## Root Causes (condensed)
- Demand shift: higher prevalence, reduced stigma, earlier help‑seeking.
- Modality mix: telehealth increased access and encounter frequency.
- Drift and inflation: diagnosis/CPT patterns and unit costs changed.

## Data Gaps (priority)
- Structured: encounter‑level modality/CPT, treatment intensity, provider/network, inflation index, geography.
- Unstructured: de‑identified clinical notes and PROs for effectiveness signals.
- Operations: PA/denial reasons, appeal outcomes, documentation quality.

## Regional Disparities (signals)
- Access: provider density, in‑network ratio, wait times constrain approvals.
- Process: adjudication criteria and documentation standards vary.
- Case mix: severity/comorbidity differences by region/demographic.

## Ethics & Governance (essentials)
- Privacy: minimum‑necessary data; strict access controls.
- Fairness: subgroup calibration/parity checks with remediation.
- Oversight: drift monitoring, model cards, audit cadence.

## Recommendations (90–180 days)
1) Modernize models with encounter‑level, telehealth, and inflation features; add drift monitoring.
2) Expand data pipelines (claims + demographics + PA/denials + de‑identified notes + PROs).
3) Standardize regional adjudication and provider documentation; expand regional access via telehealth.
4) Implement fairness audits (calibration/parity) and governance (versioning, KPIs, transparency).

— Confidence & Evidence: Confidence 3/5; Evidence: Appendix A–D; Assumptions: de‑identified sample, 2019–2025 horizon (focus 2023–2025), illustrative metrics.