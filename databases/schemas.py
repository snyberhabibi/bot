from datetime import datetime

def create_trade_log(token_name, action, price, size):
    """
    Create a trade log object for storing in MongoDB.
    
    Args:
        token_name (str): The name of the token (e.g., SOL).
        action (str): Action taken (buy or sell).
        price (float): The price of the token.
        size (float): The size of the trade (amount of tokens).
    
    Returns:
        dict: A trade log schema for MongoDB.
    """
    return {
        "token": token_name,
        "action": action,
        "price": price,
        "size": size,
        "timestamp": datetime.utcnow()
    }
