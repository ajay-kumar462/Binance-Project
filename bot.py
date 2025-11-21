from binance.client import Client
import os

BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
BINANCE_SECRET_KEY = os.getenv("BINANCE_API_SECRET")

API_KEY = BINANCE_API_KEY
SECRET_KEY = BINANCE_SECRET_KEY

client = Client(API_KEY, SECRET_KEY, testnet=True)
print(client.futures_account_balance())

def place_market_order(symbol, side, quantity):
    try:
        order = client.futures_create_order(
            symbol="BTCUSDT",
            side="BUY",
            type="MARKET",
            quantity=0.002
        )
        print("Order Executed:")
        print(order)
    except Exception as e:
        print("Error", e)

def place_limit_order(symbol, side, quantity, price):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            timeInForce="GTC",
            quantity=quantity,
            price=price
        )
        print("Limit Order Placed:")
        print(order)
    except Exception as e:
        print("Error:", e)

def user_cli():
    print("Trading Bot")

    symbol = input("Enter symbol (e.g., BTCUSDT): ").upper()
    side = input("Enter side (BUY/SELL): ").upper()
    order_type = input("Enter order type (MARKET/LIMIT): ").upper()
    quantity = float(input("Enter quantity: "))

    if order_type == "LIMIT":
        price = input("Enter limit price: ")

    if order_type == "MARKET":
        place_market_order(symbol, side, quantity)

    elif order_type == "LIMIT":
        place_limit_order(symbol, side, quantity, price)

    else:
        print("Invalid order type.")

user_cli()