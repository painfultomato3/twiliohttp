import requests

resp = requests.get('https://api.kraken.com/0/public/Ticker?pair=XBTUSD')

data = resp.json()['result']['XXBTZUSD']['a'][0]

price = round(float(data), 2)

def priceofbtc():

	return price