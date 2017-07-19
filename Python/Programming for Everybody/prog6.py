x=0
while x==0:
    try:
		grade=raw_input("Enter grade in number:")
		grade=float(grade)
		if grade>=9.0:
			print "A"
		elif grade>=8.0:
			print "B"
		elif grade>=7.0:
			print "C"
		elif grade>=6.0:
			print "D"
		else:
			print "F"
		x=1    
    except:
        print "Please enter only numeric values"