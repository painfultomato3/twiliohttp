from test import main
import time

resp = main('AddOrder', "BTCUSD", "0.01", "sell")

print(resp.json())