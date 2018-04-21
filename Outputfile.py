principal = 200000 	# initial amount
rate = 0.03			# Interest rate
numyears = 10		# Number of years
year = 8

f = open("out","w") 	# Open file for writing
while year <= numyears:
	principal = principal * (1 + rate)
	print >>f,"%3d %0.2f" % (year,principal)
	# print("%3d %0.2f" % (year,principal),file=f) # Python3
	year += 1
f.close()


