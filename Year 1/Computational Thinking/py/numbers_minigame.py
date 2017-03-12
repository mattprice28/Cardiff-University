a=3
b=4
c=3
unlocked=False
options = ['1','2','3']
print()
print("There are 3 numbers on a screen infront of you: 3 4 3")
print("A message reads 'Make all numbers equal to 3'")
print("Each button will increase its own number by 1")
print("While also decreasing all adjacent numbers by 1")

while unlocked==False:
	if a==3 and b==3 and c==3:
	    unlocked=True
	    print("You opened the medicine cabinet!")
	    #inventory.append("Medicine")
	else:
		print()
		print(a, b, c)
		print()
		print("There are 3 buttons 1, 2 and 3")
		print()
		userInput = str(input("Please choose a button :"))
		print()
		if userInput not in options:
			print()
			print("Please choose a valid button")
			print()
		elif userInput == '1':
			a = a + 1
			b = b - 1
		elif userInput == '2':
			a = a - 1
			b = b + 1
			c = c - 1
		elif userInput == '3':
			b = b - 1
			c = c + 1	

    
