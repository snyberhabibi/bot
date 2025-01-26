from concurrent.futures import ThreadPoolExecutor, as_completed

class TradeExecutor:
    def __init__(self, dex_service, risk_manager, notifier):
        """
        Initialize the TradeExecutor with required services.

        Args:
            dex_service (DexService): Service for interacting with DEX.
            risk_manager (RiskManager): Service for risk evaluation.
            notifier (Notifications): Service for sending notifications.
        """
        if not all([dex_service, risk_manager, notifier]):
            raise ValueError("DexService, RiskManager, and Notifications are required.")
        
        self.dex = dex_service
        self.risk_manager = risk_manager
        self.notifier = notifier

    def execute_trade(self, token, entry_price, sentiment_score):
        """
        Execute a single trade based on risk evaluation.

        Args:
            token (dict): Token details (name, market address, size).
            entry_price (float): Entry price of the token.
            sentiment_score (float): Sentiment score for the token.
        """
        try:
            # Fetch market data
            market_data = self.dex.fetch_market_data(token["market_address"])
            current_price = market_data.get("price")

            # Evaluate risk and determine action
            action = self.risk_manager.evaluate_risk(entry_price, current_price, sentiment_score)

            # Execute the trade if action is determined
            if action == "sell":
                result = self.dex.place_order(token["market_address"], "sell", current_price, token["size"])
                self.notifier.send_message(f"Sold {token['name']} at {current_price} SOL. Transaction: {result}")
            elif action == "buy":
                result = self.dex.place_order(token["market_address"], "buy", current_price, token["size"])
                self.notifier.send_message(f"Bought {token['name']} at {current_price} SOL. Transaction: {result}")
            else:
                print(f"Holding {token['name']} - No action taken.")
        except Exception as e:
            print(f"Error executing trade for {token['name']}: {e}")
            self.notifier.send_message(f"Error executing trade for {token['name']}: {e}")

    def execute_all(self, tokens):
        """
        Execute trades for all tokens concurrently.

        Args:
            tokens (list of dict): List of tokens with their details.
        """
        try:
            with ThreadPoolExecutor(max_workers=10) as executor:
                futures = {
                    executor.submit(self.execute_trade, token, token["entry_price"], token["sentiment_score"]): token
                    for token in tokens
                }

                for future in as_completed(futures):
                    token = futures[future]
                    try:
                        future.result()  # Wait for the thread to complete
                    except Exception as e:
                        print(f"Error in thread for {token['name']}: {e}")
                        self.notifier.send_message(f"Thread error for {token['name']}: {e}")
        except Exception as e:
            print(f"Error during trade execution: {e}")
            self.notifier.send_message(f"Error during trade execution: {e}")
