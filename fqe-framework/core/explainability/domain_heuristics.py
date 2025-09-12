# A sample of the 147 domain heuristics
FINANCIAL_HEURISTICS = {
    "HEURISTIC_001": {
        "description": "Transaction amount exceeds 3x the 90-day rolling average for this merchant category.",
        "condition": lambda tx, history: tx['amount'] > 3 * history.get_avg_merchant_spending(tx['merchant_category'], 90),
        "compliance_risk": "Potential fraud or error; may violate PSD2 SCA exemption rules."
    },
    "HEURISTIC_002": {
        "description": "Transaction occurs in a country not visited in the last 730 days (2 years).",
        "condition": lambda tx, history: tx['country_code'] not in history.get_countries(last_n_days=730),
        "compliance_risk": "High fraud probability; triggers mandatory STR (Suspicious Transaction Report)."
    },
    "HEURISTIC_003": {
        "description": "Rapid sequence of high-value transactions (< 5 min apart).",
        "condition": lambda tx, history: history.get_tx_count(last_n_minutes=5) >= 3 and all(amt > 1000 for amt in history.get_recent_amounts()),
        "compliance_risk": "Velocity checking failure. Potential money laundering pattern."
    },
    # ... 144 more heuristics
}