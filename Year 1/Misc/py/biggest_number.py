first_number = float(input("Please enter the first number:"))
second_number = float(input("Please enter the second number:"))
third_number = float(input("Please enter the third number:"))

a = "The highest number is: "

if first_number > second_number:
    if first_number > third_number:
        print(str(a) + str(first_number))
elif second_number > third_number:
	print(str(a) + str(second_number))
else:
	print (str(a) + str(third_number))