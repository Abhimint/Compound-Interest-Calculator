# Compound Interest Calculator

def compound_int():
	principal = input("Enter your intial deposit in CAN: $")
	rate = input("Enter the expected interest rate: ")
	rate = rate/100
	time = input("Enter the number of years of compounding: ")
	time = time + 1
	compound = input("Enter compounding period per year: ")

	print "Year %21s" % "amount on deposit" 

	for time in range(1, time):
		formula = principal * (1.0 + rate)** time
		print "%4d%221.2f" % (time, formula)

def start():
	print "We will compund your interest"
	compound_int()

start()