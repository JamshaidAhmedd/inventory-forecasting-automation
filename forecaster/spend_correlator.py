BASELINE_DAILY_SPEND = 500.0

def get_spend_multiplier(current_daily_spend):
    ratio = current_daily_spend / BASELINE_DAILY_SPEND
    if ratio > 1.5:
        return 1.3
    elif ratio < 0.5:
        return 0.7
    return 1.0
