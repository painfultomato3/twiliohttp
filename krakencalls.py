from krakenheaders import kraken_request, api_key, api_sec
import time

def krakencall(param1, asset = "", key = "", amount = 0.00):

		resp = kraken_request('/0/private/' + param1, {"nonce": str(int(1000*time.time())), "asset": asset, "key": key, "amount": float(amount), "type": key, "volume": float(amount), "pair": asset, "ordertype": "market"}, api_key, api_sec)

		return resp.json()


def krakengetbalance():

	resp = krakencall('TradeBalance', 'BTC')

	return resp['result']['eb'] 



def krakenwithdrawal():

	resp = krakencall('Withdraw', 'BTC', 'localcoinswap', '0.01')

	return resp


def krakenbuysell(param = 'buy', volume = '1.68'):

	resp = krakencall('AddOrder', 'BTCUSD', param, volume)

	return resp

