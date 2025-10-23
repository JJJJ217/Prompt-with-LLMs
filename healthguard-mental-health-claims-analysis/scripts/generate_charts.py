from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import json

# Resolve paths relative to this script's location
SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parent
DATA_DIR = ROOT / 'data'
CHARTS_DIR = ROOT / 'charts'
IMAGES_DIR = CHARTS_DIR / 'images'
VL_DIR = CHARTS_DIR / 'vega-lite'
TABLES_DIR = CHARTS_DIR / 'tables'

IMAGES_DIR.mkdir(parents=True, exist_ok=True)
VL_DIR.mkdir(parents=True, exist_ok=True)
TABLES_DIR.mkdir(parents=True, exist_ok=True)

# Load data with correct column names
claims_data = pd.read_csv(DATA_DIR / 'claims_sample.csv', parse_dates=['ClaimDate'])
approvals_data = pd.read_csv(DATA_DIR / 'approvals_by_region_sample.csv')
demographics_data = pd.read_csv(DATA_DIR / 'demographics_sample.csv')

# Generate claims trend chart (sum of ClaimAmount by year)
def generate_claims_trend_chart():
    df = claims_data.copy()
    df['Year'] = df['ClaimDate'].dt.year
    claims_trend = df.groupby('Year', as_index=False)['ClaimAmount'].sum()
    plt.figure(figsize=(8, 5))
    plt.plot(claims_trend['Year'], claims_trend['ClaimAmount'], marker='o')
    plt.title('Mental Health Claims Trend (Total Claim Amount)')
    plt.xlabel('Year')
    plt.ylabel('Total Claim Amount')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(IMAGES_DIR / 'claims_trend.png', dpi=150)
    plt.close()
    return claims_trend

# Generate regional approval rates chart
def generate_regional_approval_rates_chart():
    df = approvals_data.copy()
    # Normalize column names
    if 'Approval Rate (%)' in df.columns:
        df = df.rename(columns={'Approval Rate (%)': 'ApprovalRate', 'Region': 'Region'})
    plt.figure(figsize=(9, 5))
    plt.bar(df['Region'], df['ApprovalRate'], color='skyblue')
    plt.title('Therapist Reimbursement Approval Rates by Region')
    plt.xlabel('Region')
    plt.ylabel('Approval Rate (%)')
    plt.xticks(rotation=40, ha='right')
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig(IMAGES_DIR / 'regional_approval_rates.png', dpi=150)
    plt.close()
    return df[['Region', 'ApprovalRate']]

# Demographics charts
def generate_demographics_charts():
    demo = demographics_data.copy()
    # Normalize column names for safety
    demo.columns = demo.columns.str.strip()
    # Treatment type by region (stacked bar)
    if {'Region', 'TreatmentType'}.issubset(demo.columns):
        counts = demo.groupby(['Region', 'TreatmentType']).size().reset_index(name='Count')
        pivot = counts.pivot(index='Region', columns='TreatmentType', values='Count').fillna(0)
        pivot.sort_index(inplace=True)
        plt.figure(figsize=(9, 5))
        pivot.plot(kind='bar', stacked=True, ax=plt.gca())
        plt.title('Demographics: Treatment Type by Region (Sample)')
        plt.xlabel('Region')
        plt.ylabel('Count')
        plt.xticks(rotation=40, ha='right')
        plt.tight_layout()
        plt.savefig(IMAGES_DIR / 'demographics_treatment_by_region.png', dpi=150)
        plt.close()

    # Age distribution (histogram)
    if 'Age' in demo.columns:
        ages = pd.to_numeric(demo['Age'], errors='coerce').dropna()
        if not ages.empty:
            plt.figure(figsize=(8, 4.5))
            plt.hist(ages, bins=8, color='slateblue', alpha=0.85, edgecolor='white')
            plt.title('Demographics: Age Distribution (Sample)')
            plt.xlabel('Age')
            plt.ylabel('Count')
            plt.tight_layout()
            plt.savefig(IMAGES_DIR / 'demographics_age_distribution.png', dpi=150)
            plt.close()

# Generate Vega-Lite specifications using correct fields
def generate_vega_lite_specifications():
    vl_claims = {
        "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
        "description": "Trend of total mental health claims amount by year.",
        "data": {
            "values": (
                claims_data.assign(Year=claims_data['ClaimDate'].dt.year)
                           .groupby('Year', as_index=False)['ClaimAmount'].sum()
                           .rename(columns={'ClaimAmount': 'TotalClaimAmount'})
                           .to_dict(orient='records')
            )
        },
        "mark": "line",
        "encoding": {
            "x": {"field": "Year", "type": "ordinal", "title": "Year"},
            "y": {"field": "TotalClaimAmount", "type": "quantitative", "title": "Total Claim Amount"}
        }
    }

    df_app = approvals_data.rename(columns={'Approval Rate (%)': 'ApprovalRate', 'Region': 'Region'})
    vl_region = {
        "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
        "description": "Approval rates of therapist reimbursement requests by region.",
        "data": {"values": df_app.to_dict(orient='records')},
        "mark": "bar",
        "encoding": {
            "x": {"field": "Region", "type": "nominal"},
            "y": {"field": "ApprovalRate", "type": "quantitative", "title": "Approval Rate (%)"}
        }
    }

    (VL_DIR / 'claims_trend.vl.json').write_text(json.dumps(vl_claims, indent=2))
    (VL_DIR / 'regional_approval_rates.vl.json').write_text(json.dumps(vl_region, indent=2))


# Generate summary tables in Markdown
def generate_summary_tables_md(claims_trend_df, approval_rates_df):
    lines = []
    lines.append('# Summary Tables')
    lines.append('')
    # Claims by Year
    lines.append('## Total Claim Amount by Year')
    lines.append('| Year | Total Claim Amount |')
    lines.append('|------|--------------------|')
    for _, r in claims_trend_df.iterrows():
        lines.append(f"| {int(r['Year'])} | {int(r['ClaimAmount'])} |")
    lines.append('')
    # Approval Rates
    lines.append('## Approval Rates by Region')
    lines.append('| Region | Approval Rate (%) |')
    lines.append('|--------|--------------------|')
    for _, r in approval_rates_df.iterrows():
        lines.append(f"| {r['Region']} | {r['ApprovalRate']} |")
    lines.append('')
    # Demographics quick view (counts by TreatmentType if present)
    demo = demographics_data.copy()
    demo.columns = demo.columns.str.strip()
    if 'TreatmentType' in demo.columns and 'Region' in demo.columns:
        counts = (demo.groupby(['Region','TreatmentType']).size()
                       .reset_index(name='Count'))
        lines.append('## Treatment Type Counts by Region (Sample)')
        lines.append('| Region | Treatment Type | Count |')
        lines.append('|--------|----------------|-------|')
        for _, r in counts.iterrows():
            lines.append(f"| {r['Region']} | {r['TreatmentType']} | {int(r['Count'])} |")
        lines.append('')

    (TABLES_DIR / 'summary_tables.md').write_text('\n'.join(lines))
    return '\n'.join(lines)


def main():
    ct = generate_claims_trend_chart()
    ar = generate_regional_approval_rates_chart()
    generate_vega_lite_specifications()
    generate_demographics_charts()
    generate_summary_tables_md(ct, ar)

if __name__ == '__main__':
    main()