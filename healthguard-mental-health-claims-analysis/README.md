# HealthGuard Mental Health Claims Analysis

## Overview
The HealthGuard Mental Health Claims Analysis project aims to investigate the increasing trends in mental health claims and provide strategic recommendations based on comprehensive data analysis. The project addresses key issues such as rising claims, regional disparities in approval rates, and ethical considerations surrounding the use of behavioral health data.

## Project Structure
- **docs/**: Contains the main documentation files including the business report, appendix with supporting data, and the prompt used for generating insights.
  - `report.md`: A formal business report summarizing findings and recommendations.
  - `appendix.md`: Supporting data, charts, and visuals relevant to the analysis.
  - `prompt.md`: The prompt used to generate the analysis from a language model.
  
- **data/**: Sample datasets used for analysis.
  - `claims_sample.csv`: Sample dataset of mental health claims.
  - `demographics_sample.csv`: Sample dataset of patient demographics.
  - `approvals_by_region_sample.csv`: Sample dataset showing approval rates by region.

- **charts/**: Contains visualizations and summary tables.
  - **vega-lite/**: Vega-Lite specifications for visualizing data trends.
    - `claims_trend.vl.json`: Visualization of mental health claims trends over time.
    - `regional_approval_rates.vl.json`: Visualization of approval rates by region.
  - **tables/**: Summary tables presenting key statistics.
    - `summary_tables.md`: Summary tables of findings.

- **scripts/**: Python scripts for data processing and visualization.
  - `generate_charts.py`: Script to generate charts from the provided datasets.

## Setup Instructions
1. Clone the repository to your local machine.
2. Ensure you have Python installed along with necessary libraries such as Pandas, Matplotlib, and Vega-Lite.
3. Navigate to the `scripts` directory and run `generate_charts.py` to create visualizations based on the data in the `data` directory.

## Usage
- Review the `docs/report.md` for a comprehensive analysis of mental health claims.
- Refer to `docs/appendix.md` for supporting data and visuals.
- Use `docs/prompt.md` to understand the context and questions addressed in the analysis.

## Conclusion
This project serves as a critical analysis of mental health claims for HealthGuard, providing insights and recommendations to address the challenges faced in the current healthcare landscape.