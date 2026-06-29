import anthropic
import os

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
ALERT_THRESHOLD_DAYS = int(os.environ.get("STOCKOUT_ALERT_DAYS", 14))

def check_stockouts(velocities, inventory=None):
    if inventory is None:
        inventory = {"SKN-SERUM-30ML": 143, "SKN-TONER-200ML": 890}
    for item in velocities:
        sku = item["sku"]
        daily_velocity = item["daily_velocity"]
        stock = inventory.get(sku, 0)
        if daily_velocity > 0:
            days_remaining = stock / daily_velocity
            if days_remaining < ALERT_THRESHOLD_DAYS:
                recommendation = get_claude_recommendation(sku, stock, daily_velocity, days_remaining)
                print(f"\n[ALERT] SKU: {sku}")
                print(f"Projected stockout in: {days_remaining:.0f} days")
                print(f"Current stock: {stock} units")
                print(f"Daily velocity: {daily_velocity:.1f} units/day")
                print(f"\nRecommendation:\n{recommendation}")

def get_claude_recommendation(sku, stock, velocity, days_remaining):
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=512,
        messages=[{
            "role": "user",
            "content": f"SKU {sku} will stock out in {days_remaining:.0f} days. Current stock: {stock}. Daily velocity: {velocity:.1f}/day. Recommend ad spend adjustment and reorder quantity."
        }]
    )
    return message.content[0].text
