import localcoinheaders

s = localcoinheaders.s 

def localcoincall(param1, param2, payload = '', method = 'get'):

	if method == 'get':

		resp = s.get("https://api.localcoinswap.com/api/v2/" + param1 + "/" + param2 + '/')

	elif method == 'post':

		resp = s.post("https://api.localcoinswap.com/api/v2/" + param1 + "/" + param2 + '/', data = payload)

	return resp.json()


def localcoingetbalance():

	resp = localcoincall('wallets', 'info/BTC')

	btcbal = resp['currency_balance']['total_balance']
	fiatbal = resp['currency_balance']['total_fiat_balance']

	return [btcbal, fiatbal]
	


def localcoingetotp():

	resp = localcoincall('wallets', 'request-withdrawal-otp', '', 'post')

	otp = input()

	return int(otp)


def localcoinwithdraw(to_address, amount):

	payload = {"otp": localcoingetotp(), "currency": 1, "to_address": to_address, "amount": amount}

	resp = localcoincall('wallets', 'custodial-withdrawal', payload, 'post')

	return resp


#localcoinwithdraw("3N8EtaBDSJFmTcqjQdWhZmP3pRmWxcQJ8m", '0.01')



