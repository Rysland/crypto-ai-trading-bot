import requests
import pandas as pd

def get_historical_data(symbol='BTCUSDT', interval='1h', limit=1000):
    url = f'https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}'
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', '_', '_', '_', '_', '_'])
    df['close'] = df['close'].astype(float)
    return df[['timestamp', 'close']]

if __name__ == "__main__":
    data = get_historical_data()
    print(data.head())
