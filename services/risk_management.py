class RiskManager:
    def evaluate_risk(self, entry_price, current_price, sentiment_score):
        if current_price >= entry_price * 1.3:
            return "sell"
        elif current_price <= entry_price * 0.9:
            return "sell"
        elif sentiment_score < 0:
            return "sell"
        return "hold"
