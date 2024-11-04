import requests
import pandas as pd
from datetime import datetime

# Fetch Bitcoin price data from CoinGecko API
url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    btc_price = data['bitcoin']['usd']
    date_scraped = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    records = [(date_scraped, btc_price)]
    print("BTC price found:", btc_price)
else:
    print("Failed to retrieve data from API.")
    records = [(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), None)]

# Convert data to DataFrame
df = pd.DataFrame(records, columns=['date', 'btc_price'])

# Save to CSV in Downloads folder
df.to_csv('C:/Users/YAMINI/Downloads/btc_prices.csv', index=False, encoding='utf-8')
print("BTC prices scraped and saved to C:/Users/YAMINI/Downloads/btc_prices.csv")
