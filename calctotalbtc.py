from getbtcprice import priceofbtc
import math, sys

def gettotalbtc(usdamount = sys.argv[1]):

	btcprice = priceofbtc()

	fee = 1.11

	btcprice2 = round((btcprice * fee), 2)

	totalbtc = float(usdamount) / btcprice2

	final = math.floor(totalbtc * 10 ** 8) / 10 ** 8

	value = float(final) * float(btcprice)
	profit = float(usdamount) - float(value)

	return final


