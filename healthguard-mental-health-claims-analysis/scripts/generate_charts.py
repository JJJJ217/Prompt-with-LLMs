import pandas as pd
import matplotlib.pyplot as plt
import json

# Load data
claims_data = pd.read_csv('../data/claims_sample.csv')
demographics_data = pd.read_csv('../data/demographics_sample.csv')
approvals_data = pd.read_csv('../data/approvals_by_region_sample.csv')

# Generate claims trend chart
def generate_claims_trend_chart():
    claims_trend = claims_data.groupby('year')['claim_amount'].sum().reset_index()
    plt.figure(figsize=(10, 6))
    plt.plot(claims_trend['year'], claims_trend['claim_amount'], marker='o')
    plt.title('Mental Health Claims Trend (2023-2025)')
    plt.xlabel('Year')
    plt.ylabel('Total Claim Amount')
    plt.grid()
    plt.savefig('../charts/claims_trend.png')
    plt.close()

# Generate regional approval rates chart
def generate_regional_approval_rates_chart():
    approval_rates = approvals_data.groupby('region')['approval_rate'].mean().reset_index()
    plt.figure(figsize=(10, 6))
    plt.bar(approval_rates['region'], approval_rates['approval_rate'], color='skyblue')
    plt.title('Therapist Reimbursement Approval Rates by Region')
    plt.xlabel('Region')
    plt.ylabel('Approval Rate (%)')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.savefig('../charts/regional_approval_rates.png')
    plt.close()

# Generate Vega-Lite specifications
def generate_vega_lite_specifications():
    claims_trend_spec = {
        "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
        "description": "A chart showing the trend of mental health claims over time.",
        "data": {
            "values": claims_data.to_dict(orient='records')
        },
        "mark": "line",
        "encoding": {
            "x": {"field": "year", "type": "temporal"},
            "y": {"field": "claim_amount", "type": "quantitative"}
        }
    }
    
    regional_approval_spec = {
        "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
        "description": "A chart showing the approval rates of therapist reimbursement requests by region.",
        "data": {
            "values": approvals_data.to_dict(orient='records')
        },
        "mark": "bar",
        "encoding": {
            "x": {"field": "region", "type": "nominal"},
            "y": {"field": "approval_rate", "type": "quantitative"}
        }
    }
    
    with open('../charts/vega-lite/claims_trend.vl.json', 'w') as f:
        json.dump(claims_trend_spec, f)
    
    with open('../charts/vega-lite/regional_approval_rates.vl.json', 'w') as f:
        json.dump(regional_approval_spec, f)

# Main function to generate all charts
def main():
    generate_claims_trend_chart()
    generate_regional_approval_rates_chart()
    generate_vega_lite_specifications()

if __name__ == "__main__":
    main()