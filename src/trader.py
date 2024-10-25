from pybit import HTTP

client = HTTP("https://api.bybit.com", api_key="YOUR_API_KEY", api_secret="YOUR_API_SECRET")

def place_order(symbol="BTCUSDT", side="Buy", qty=1):
    order = client.place_active_order(symbol=symbol, side=side, order_type="Market", qty=qty)
    return order
