API_KEYS = {
    "solana_rpc": "https://api.mainnet-beta.solana.com",
    "telegram_bot_token": "7513935791:AAHhzTSNBVRxolPV9JOuC8YOndr3j1oTTL4",
    "mongo_uri": "mongodb+srv://yusuf:nCnlGqgMTG7eQYSk@cluster0.vw9ck.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
}

TRADING_PARAMS = {
    "initial_balance": 0.100,  # Starting balance in SOL
    "risk_percentage": 10,   # Max risk per trade (% of wallet)
    "take_profit": 1.3,      # Take-profit multiplier (30% profit)
    "stop_loss": 0.9,        # Stop-loss multiplier (10% loss)
}

TOKENS = [
    {"name": "TokenA", "market_address": "market-address-1"},
    {"name": "TokenB", "market_address": "market-address-2"},
]

# Logging Configuration
LOGGING_CONFIG = {
    "log_level": "INFO",  # Options: DEBUG, INFO, WARNING, ERROR
    "log_file": "bot.log",  # Log output file
}