#print "pass" if the percentage is 50 or above.
#print "fail" if the percentage is below  50.
#print "invalid" if the percentage is outside the range of 0 to 100.

perc = 70
print("invalid" if perc< 0 or perc > 100 else "pass" if perc>=50 else "fail")

