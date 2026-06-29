import pandas as pd
from datetime import datetime, timedelta

FORECAST_WINDOW_DAYS = 30

def calculate_velocity(df):
    df["created_at"] = pd.to_datetime(df["created_at"])
    cutoff = datetime.now() - timedelta(days=FORECAST_WINDOW_DAYS)
    recent = df[df["created_at"] >= cutoff]
    velocity = (
        recent.groupby("sku")["quantity"]
        .sum()
        .div(FORECAST_WINDOW_DAYS)
        .reset_index()
        .rename(columns={"quantity": "daily_velocity"})
    )
    return velocity.to_dict("records")
