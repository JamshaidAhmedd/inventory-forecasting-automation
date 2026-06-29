import pandas as pd
from velocity_model import calculate_velocity
from alerts.stockout_alert import check_stockouts

def run_pipeline(orders_csv="../mock-data/shopify-orders.csv"):
    print("[Pipeline] Loading order data...")
    df = pd.read_csv(orders_csv)
    velocities = calculate_velocity(df)
    print(f"[Pipeline] Calculated velocity for {len(velocities)} SKUs")
    check_stockouts(velocities)

if __name__ == "__main__":
    run_pipeline()
