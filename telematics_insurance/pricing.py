def adjust_premium(total_risk, base_premium=100, risk_unit=5):
    return base_premium + total_risk * risk_unit 