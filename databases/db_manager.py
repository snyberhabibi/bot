from pymongo import MongoClient, errors
from datetime import datetime

class DBManager:
    def __init__(self, mongo_uri, db_name="trading_bot"):
        """
        Initialize the MongoDB client and database.

        Args:
            mongo_uri (str): The URI for connecting to the MongoDB database.
            db_name (str): The name of the database. Default is 'trading_bot'.
        """
        if not mongo_uri:
            raise ValueError("MongoDB URI is required.")
        
        try:
            self.client = MongoClient(mongo_uri, serverSelectionTimeoutMS=5000)  # 5-second timeout
            self.db = self.client[db_name]
            self.trades = self.db["trades"]
        except errors.ConnectionError as e:
            print(f"Error connecting to MongoDB: {e}")
            raise

    def log_trade(self, token, action, price, size):
        """
        Log a trade into the 'trades' collection.

        Args:
            token (str): The name of the token being traded.
            action (str): The action performed ('buy' or 'sell').
            price (float): The price at which the trade occurred.
            size (float): The size of the trade.

        Returns:
            dict: The result of the insertion.
        """
        if not all([token, action, isinstance(price, (int, float)), isinstance(size, (int, float))]):
            raise ValueError("Invalid inputs for logging trade.")

        try:
            trade = {
                "token": token,
                "action": action,
                "price": price,
                "size": size,
                "timestamp": datetime.utcnow(),
            }
            result = self.trades.insert_one(trade)
            print(f"Trade logged: {trade}")
            return {"status": "success", "inserted_id": result.inserted_id}
        except Exception as e:
            print(f"Error logging trade: {e}")
            return {"status": "failure", "error": str(e)}

    def get_all_trades(self):
        """
        Retrieve all trades from the 'trades' collection.

        Returns:
            list: A list of all trades.
        """
        try:
            trades = list(self.trades.find({}, {"_id": 0}))  # Exclude MongoDB's internal '_id' field
            print(f"Retrieved {len(trades)} trades.")
            return trades
        except Exception as e:
            print(f"Error retrieving trades: {e}")
            return []

    def get_trades_by_token(self, token):
        """
        Retrieve all trades for a specific token.

        Args:
            token (str): The name of the token to filter by.

        Returns:
            list: A list of trades for the specified token.
        """
        try:
            trades = list(self.trades.find({"token": token}, {"_id": 0}))
            print(f"Retrieved {len(trades)} trades for token '{token}'.")
            return trades
        except Exception as e:
            print(f"Error retrieving trades for token '{token}': {e}")
            return []

    def delete_all_trades(self):
        """
        Delete all trades from the 'trades' collection.

        Returns:
            dict: The result of the deletion operation.
        """
        try:
            result = self.trades.delete_many({})
            print(f"Deleted {result.deleted_count} trades.")
            return {"status": "success", "deleted_count": result.deleted_count}
        except Exception as e:
            print(f"Error deleting trades: {e}")
            return {"status": "failure", "error": str(e)}
