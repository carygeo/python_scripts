hrs = raw_input("Enter Hours:")
h = float(hrs)

rt = raw_input("Enter Rate of Pay:")
r = float(rt)

if h <= 40:
	print h * r

else:
	print ((h - (h - 40)) * r) + ((h - 40) * (r*(1.5)))