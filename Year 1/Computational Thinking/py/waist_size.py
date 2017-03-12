import math
h = float(input("Enter your height in cm: "))
m = float(input("Enter your weight in kg: "))

c =(2 * math.sqrt((3.14*h)/m))

print("Your waist is approximately " + str(c) + "cm")