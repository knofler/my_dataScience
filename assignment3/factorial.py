print "Enter a number"
num = input()
fact = 1

while (num != 0) :
	for i in range(1, num+1):
		fact = fact * i
	print "factorial of " + str(num) + " is " + str(fact)	
	fact =1
	print "Enter a number"
	num = input()		

