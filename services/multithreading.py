from concurrent.futures import ThreadPoolExecutor

class TradeExecutor:
    def __init__(self, dex_service, risk_manager, notifier):
        self.dex = dex_service
        self.risk_manager = risk_manager
        self.notifier = notifier

    def execute_trade(self, token, entry_price, sentiment_score):
        market_data = self.dex.fetch_market_data(token["market_address"])
        current_price = market_data["price"]
        action = self.risk_manager.evaluate_risk(entry_price, current_price, sentiment_score)

        if action == "sell":
            result = self.dex.place_order(token["market_address"], "sell", current_price, token["size"])
            self.notifier.send_message(f"Sold {token['name']} at {current_price} SOL. Transaction: {result}")
        elif action == "buy":
            result = self.dex.place_order(token["market_address"], "buy", current_price, token["size"])
            self.notifier.send_message(f"Bought {token['name']} at {current_price} SOL. Transaction: {result}")

    def execute_all(self, tokens):
        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(self.execute_trade, token, token["entry_price"], token["sentiment_score"]) for token in tokens]
            for future in futures:
                future.result()
