numgrade = int(input("Enter number of grade: "))
x = []
for i in range(0,numgrade,1):
	mygrade = int(input("Enter Grade: "))
	x.append(mygrade)
for i in range(0,numgrade,1):
	print(x[i])
