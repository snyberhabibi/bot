from solana.rpc.api import Client

class SolanaService:
    def __init__(self, rpc_url, wallet):
        self.client = Client(rpc_url)
        self.wallet = wallet

    def get_balance(self):
        balance = self.client.get_balance(self.wallet.public_key)["result"]["value"]
        return balance / 1_000_000_000  # Convert lamports to SOL

    def execute_trade(self, market, side, price, size):
        print(f"Executing {side} order: {size} units at {price} SOL")
        return {"status": "success", "transaction_id": "12345"}
