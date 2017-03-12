#!/usr/bin/python

import datetime
import cgi, cgitb
form = cgi.FieldStorage()
#year = form.getvalue("year")
output1 = "unchecked"
output2 = "unchecked"
output3 = "checked"
year = input("Enter Year:")
y = int(year)

a = y % 19
b = y // 100
c = y % 100
d = b // 4
e = b % 4
g = (8 * b + 13) // 25
h = (19 * a + b - d - g + 15) % 30
j = c // 4
k = c % 4
m = (a + 11 * h) // 319
r = (2 * e + 2 * j - k - h + m + 32) % 7
n = (h - m + r + 90) // 25
p = (h - m + r + n + 19) % 32

#return datetime.date(year=y, month=n, day=p)
if n ==1:
	m = "January"
elif n == 2:
	m = "February" 
elif n == 3:
	m = "March"
elif n == 4:
	m = "April" 
elif n == 5:
	m = "May"
elif n == 6:
	m = "June" 
elif n == 7:
	m = "July" 
elif n == 8:
	m = "August"
elif n == 9:
	m = "September" 
elif n == 10:
	m = "October"
elif n == 11:
	m = "November"
elif n == 12:
	m = "December"

if p == 1 or p == 21 or p == 31:
	r = "st"
elif p == 2 or p == 22:
	r = "nd"
elif p == 3 or p == 23:
	r = "rd"
else:
	r = "th"

print("Content-Type: text/html; charset=utf-8")
print ()
print ("<!DOCTYPE html>")
print ("<html>")
print ("<head> <title> When is Easter? </title> </head>")
print("<h1>When is Easter?</h1>")
print ("<body>")
if output1 == "checked":
	print ("<p>")
	print ("Easter is on " + str(p) + "/" + str(n) + "/" + str(y))
	print ("</p>")
elif output2 == "checked":
	print ("<p>")
	print ("Easter is on " + str(p) + "<sup>" + r + "</sup>" + " " + m + " " + str(y))
	print ("</p>")
elif output3 == "checked":
	print ("<p>")
	print ("Easter is on " + str(p) + "<sup>" + r + "</sup>" + " " + m + " " + str(y))
	print ("Easter is on " + str(p) + "/" + str(n) + "/" + str(y))
	print ("</p>")
print ("</body>")
print ("</html>")
