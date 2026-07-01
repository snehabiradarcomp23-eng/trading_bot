import os
from dotenv import load_dotenv
from binance.client import Client

load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

def get_client():
    print("API KEY:", API_KEY)
    print("SECRET EXISTS:", API_SECRET is not None)

    client = Client(API_KEY, API_SECRET)
    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    return client