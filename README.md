# Collections Data Analyst Assignment

# Live Dashboard

[Click here to explore the Collections Performance Dashboard](https://keerthikaeaday.github.io/collections-performance-analysis/)

Explore monthly payment performance, success rates, and targeting analysis through the interactive dashboard.

## Project Overview
This project investigates collections payment performance, data quality, payment attribution, and targeting changes.

## Contents
- golden_dataset/: Cleaned datasets and the pipeline script.
- sql/collections_analysis.sql: SQL queries for payment performance and data-quality checks.
- executive_memo.md: Executive summary and recommendations.
- executive_dashboard.html: Dashboard summarising monthly performance and targeting.
- dashboard_charts.png: Dashboard visualisations.
- data_architecture.mmd: Proposed analytics architecture.
- golden_payments.csv: Cleaned payment dataset.

## Key Findings
- Payment success rate was 69.84% in January 2026.
- It peaked at 71.52% in February 2026.
- It was 70.06% in July 2026.
- The observed August rate was 67.40%, but August data is incomplete.
- Initial payment checks identified exact duplicate rows, missing payment references, and unmatched borrower IDs.

## Limitations
Payment success rate is not necessarily equivalent to debt recovery rate. The reported 11% month-on-month improvement cannot be confirmed without a validated recovery definition, denominator, and payment attribution process. Exact duplicate removal does not resolve all duplicate IDs or conflicting records.

## Recommendation
Validate the recovery metric and payment attribution rules before making the full investment decision. Use a controlled pilot to measure incremental recovery and costs before scaling an intervention.

## Reproducibility
The original notebook is 01_dataset_inspection.ipynb. The Golden Dataset pipeline is build_golden_dataset.py. Review the source paths and dependencies before rerunning the pipeline.
