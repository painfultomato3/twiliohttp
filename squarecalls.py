from squareheaders import client
import random

def squarecall(param1, param2, usdamount = 0.00, linkid = '', begintime = ''):

	if param1 == 'checkout':

		if param2 == 'delete_payment_link':

			res = client.checkout.delete_payment_link(id = linkid)

			if res.is_success():

				return 'Link Deleted'

		elif param2 == 'create_payment_link':

			res = client.checkout.create_payment_link(body = {"idempotency_key": str(random.getrandbits(32)),"quick_pay": {"name": "Auto Detailing","price_money": {"amount": int(usdamount),"currency": "USD"},"location_id": "L4ZKD8B38BHWE"},"checkout_options": {"custom_fields": [{"title": "Wallet Address"}],"ask_for_shipping_address": True,"accepted_payment_methods": {"apple_pay": True,"google_pay": True}}})

			return res.body

	elif param1 == 'payments':

		if param2 == 'list_payments':

			res = client.payments.list_payments(total = usdamount, begin_time = begintime)

			return res.body['payments']


def getsquarelink(amount):

	res = squarecall('checkout', 'create_payment_link', amount)

	return [res['payment_link']['id'], res['payment_link']['url']]



def deletesquarelink(linkid):

	res = squarecall('checkout', 'delete_payment_link', '', linkid)

	return res

def getsquarepayments(amount, beingtime):

	res = squarecall('payments', 'list_payments', amount, '', begintime)

	return res


#=============== TIMEOUT LOOP =====================






