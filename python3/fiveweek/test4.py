
def addInterest(balances,rate):
	for i in range(len(balances)):
		balances[i]=balances[i]*(1+rate)
	# newB=balance*(1+rate)
	# balance=newB
	return balances

def test():
	amounts=[1000.0,34,2555,235]
	rate=0.05
	amounts = addInterest(amounts,rate)
	print(amounts)

test()	