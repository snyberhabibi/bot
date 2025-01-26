from pymongo import MongoClient

class DBManager:
    def __init__(self, mongo_uri):
        self.client = MongoClient(mongo_uri)
        self.db = self.client['trading_bot']
        self.trades = self.db['trades']

    def log_trade(self, token, action, price, size):
        self.trades.insert_one({
            "token": token,
            "action": action,
            "price": price,
            "size": size,
            "timestamp": datetime.utcnow()
        })
