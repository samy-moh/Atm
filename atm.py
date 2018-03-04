# a reffers to amount cash withdraw
# b reffers to the Account balance

def atm_cash(a,b):
	if a <= b:
		while a > 0:
			if a >= 100:
				print 'give 100'
				a -= 100
			elif a >= 50:
				print 'give 50'
				a -= 50
			elif a >= 20:
				print 'give 20'
				a -= 20
			elif a >= 10:
				print 'give 10'
				a -= 10
			elif a >= 5:
				print 'give 5'
				a -= 5
			elif a < 5:
				print 'give 1'
				a -= 1
	else:
		print "NO SUFFICIENT FUNDS"
								
atm_cash(226,500)