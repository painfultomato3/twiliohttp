from calctotalbtc import gettotalbtc
from linkgen import getsquarelink
from getpayments import getpayments
from deletelinks import linkdelete
import sys, time

usdamount = sys.argv[1]

#======================== Get Total BTC To Be Sent =====================

totalbtc = gettotalbtc(usdamount)

print(f'Total BTC To Be Sent: {totalbtc}')

#======================== Get Square Link ==============================

linkinfo = getsquarelink(usdamount + '00')

print(linkinfo[1])


#======================== Function to check for payment. Timeout After 10 minutes ==============================


starttime = int(time.time())

while True:

	currentime = time.time()
	time.sleep(10)

	#======================== Get Square PAYMENTS ==============================

	begintime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(starttime)).split(' ')
	begintime = begintime[0] + 'T' + begintime[1] + 'Z'

	payments = getpayments(int(usdamount), begintime)


	if payments == 0:

		print('No Payments Yet')

	elif payments == 1:

		print('Too Many Results')

	else:

		status = payments[0]['status']
		total_money = payments[0]['total_money']['amount']
		approved_money = payments[0]['approved_money']['amount']

		if int(total_money) == int(approved_money) and status == 'COMPLETED':

			print('Card Was Charged')

			break

	if starttime + 600 < currentime:				#10 Minute Delay

		print('Ten Minutes Passed')
		print('Deleting URL')

		delete = linkdelete(linkinfo[0])

		print(delete)

		break














