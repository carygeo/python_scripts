scr = raw_input("What is your score (between 0.0 and 1.0)?:")

try:
	score = float(scr)

except: 
	score = -1 

if score > 1.0: print "Unacceptable score, please try again."
elif score >= 0.90: print "A"
elif score >= 0.80: print "B"
elif score >= 0.70: print "C"
elif score >= 0.60: print "D"
elif score < 0.60: print "F"

else:
	print "Unacceptable score, please try again."
    
