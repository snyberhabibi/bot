from datetime import datetime

def create_trade_log(token_name, action, price, size, trade_id=None, status="pending", notes=None):
    """
    Create a trade log object for storing in MongoDB.

    Args:
        token_name (str): The name of the token (e.g., SOL).
        action (str): Action taken (buy or sell).
        price (float): The price of the token.
        size (float): The size of the trade (amount of tokens).
        trade_id (str, optional): Unique identifier for the trade. Default is None.
        status (str, optional): Status of the trade (e.g., pending, completed, failed). Default is "pending".
        notes (str, optional): Additional notes about the trade. Default is None.

    Returns:
        dict: A trade log schema for MongoDB.

    Raises:
        ValueError: If any of the inputs are invalid.
    """
    # Input validation
    if not isinstance(token_name, str) or not token_name.strip():
        raise ValueError("Invalid token name. Must be a non-empty string.")
    if action not in ["buy", "sell"]:
        raise ValueError("Invalid action. Must be 'buy' or 'sell'.")
    if not isinstance(price, (int, float)) or price <= 0:
        raise ValueError("Invalid price. Must be a positive number.")
    if not isinstance(size, (int, float)) or size <= 0:
        raise ValueError("Invalid size. Must be a positive number.")

    # Construct the trade log
    trade_log = {
        "token": token_name,
        "action": action,
        "price": price,
        "size": size,
        "timestamp": datetime.utcnow(),
        "trade_id": trade_id,  # Optional unique identifier
        "status": status,      # Default is "pending"
        "notes": notes,        # Optional additional notes
    }
    return trade_log
