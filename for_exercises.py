# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for x in areas:
	print(x)

# Change for loop to use enumerate()
for index, a in enumerate(areas) :
    print("room " + str(index+1) + ": " + str(a))