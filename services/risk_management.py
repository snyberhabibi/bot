class RiskManager:
    def __init__(self, take_profit=1.3, stop_loss=0.9):
        """
        Initialize the RiskManager with configurable thresholds.

        Args:
            take_profit (float): Multiplier for take-profit condition (default 1.3, or 30% gain).
            stop_loss (float): Multiplier for stop-loss condition (default 0.9, or 10% loss).
        """
        if not (0 < stop_loss < 1):
            raise ValueError("Stop-loss must be a multiplier between 0 and 1.")
        if take_profit <= 1:
            raise ValueError("Take-profit must be greater than 1.")
        self.take_profit = take_profit
        self.stop_loss = stop_loss

    def evaluate_risk(self, entry_price, current_price, sentiment_score):
        """
        Evaluate the risk for a given trade based on current price, entry price, and sentiment score.

        Args:
            entry_price (float): The price at which the trade was entered.
            current_price (float): The current price of the token.
            sentiment_score (float): Sentiment score (-1 to 1) for the token.

        Returns:
            str: 'sell' if conditions indicate exiting the trade, 'hold' otherwise.
        """
        try:
            # Validate inputs
            if not all(isinstance(value, (int, float)) for value in [entry_price, current_price, sentiment_score]):
                raise ValueError("Invalid input: Prices and sentiment score must be numeric.")

            # Take-profit condition
            if current_price >= entry_price * self.take_profit:
                return "sell"

            # Stop-loss condition
            if current_price <= entry_price * self.stop_loss:
                return "sell"

            # Negative sentiment condition
            if sentiment_score < 0:
                return "sell"

            # Default to holding
            return "hold"
        except Exception as e:
            print(f"Error evaluating risk: {e}")
            return "hold"
