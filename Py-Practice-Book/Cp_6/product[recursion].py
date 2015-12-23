
def product(num1, num2):
	if(1 == num2):
		return num1
	else:
		return num1+product(num1,num2-1)

print product(3,4)