# Inventory Forecasting Automation

A demand forecasting pipeline that predicts sell-through vs stock levels using ad spend pace, with automated stockout alerts and Claude-powered spend adjustment recommendations.

## What It Does

1. **Ingests** historical sales data and current inventory from Shopify API
2. **Correlates** ad spend pace with historical sales velocity
3. **Forecasts** days-of-stock-remaining per SKU
4. **Alerts** when projected stockout is below threshold (default: 14 days)
5. **Recommends** ad spend adjustments and reorder quantities via Claude API

## Architecture

```
Shopify API (orders + inventory)
    |
    v
Python Forecaster (sales velocity x spend multiplier)
    |
    v
Alert Engine (threshold checks per SKU)
    |
    v
Claude API (recommendation generation)
    |
    v
Slack Alert / Email / CSV Report
```

## Tech Stack

- **Python 3.11** — forecasting pipeline and alert engine
- **Shopify API** — orders and inventory data
- **Claude API** (claude-sonnet-4-6) — recommendation generation
- **Node.js** — webhook listener for real-time Shopify events
- **pandas / numpy** — data processing

## Folder Structure

```
inventory-forecasting-automation/
├── forecaster/
│   ├── pipeline.py
│   ├── velocity_model.py
│   └── spend_correlator.py
├── alerts/
│   ├── stockout_alert.py
│   └── slack_notifier.py
├── mock-data/
│   └── shopify-orders.csv
├── notebooks/
│   └── forecast-demo.ipynb
├── requirements.txt
├── .env.example
└── README.md
```

## Setup

```bash
git clone https://github.com/jamshaidahmedd/inventory-forecasting-automation
cd inventory-forecasting-automation
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python forecaster/pipeline.py
```

## Sample Output

```
[ALERT] SKU: SKN-SERUM-30ML
Projected stockout in: 9 days
Current stock: 143 units
Daily velocity: 15.8 units/day

Recommendation (Claude):
Reduce Meta ad spend on this SKU by 30% immediately.
Initiate reorder for 500 units with expedited shipping.
Expected reorder arrival: 12 days — bridge gap with spend cut.
```

## License

MIT
