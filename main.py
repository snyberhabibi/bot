import json
from config.settings import API_KEYS, TRADING_PARAMS, TOKENS
from services.solana_service import SolanaService
from services.sentiment_service import SentimentAnalyzer
from solana.keypair import Keypair

# Step 1: Load Wallet Keypair from keypair.json
try:
    with open("keypair.json", "r") as f:
        private_key = json.load(f)  # Load the private key from the file
        wallet = Keypair.from_secret_key(bytes(private_key))  # Create a Keypair object
except FileNotFoundError:
    print("Error: keypair.json not found. Make sure the file is in the same directory as main.py.")
    exit(1)
except Exception as e:
    print(f"Error loading keypair.json: {e}")
    exit(1)

# Step 2: Initialize Services
solana = SolanaService(API_KEYS["solana_rpc"], wallet)  # Pass the wallet to the Solana service
sentiment = SentimentAnalyzer("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")  # OpenAI API key

# Step 3: Define the Main Bot Logic
def run_bot():
    print(f"Starting bot with wallet: {wallet.public_key}")

    for token in TOKENS:
        print(f"Processing token: {token['name']}")

        # Step 3a: Perform Sentiment Analysis
        sentiment_score = sentiment.analyze_sentiment([f"{token['name']} is trending"])
        print(f"Sentiment for {token['name']}: {sentiment_score}")

        # Step 3b: Fetch Wallet Balance
        wallet_balance = solana.get_balance()
        print(f"Wallet Balance: {wallet_balance} SOL")

        # Placeholder for trade logic
        if sentiment_score > 0.2:  # Only trade if sentiment is positive
            print(f"Positive sentiment detected for {token['name']}. Preparing to trade.")
        else:
            print(f"Skipping {token['name']} due to low sentiment.")

    print("Bot run completed.")

# Step 4: Run the Bot
if __name__ == "__main__":
    run_bot()
