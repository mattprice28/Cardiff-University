"""
Does it work on files where no error checking is needed on the fields

>>> sumRows("rows1.csv") == {'tim': 36.0, 'bob': 11.0, 'anna': 54.0}
True

Does it ignore headers if requested?

>>> sumRows("rows1.csv", header=True) == {'tim': 36.0, 'anna': 54.0}
True

Is it returning the right type of result?
>>> type(sumRows("rows1.csv"))
<class 'dict'>

Does it work on files with empty fields or fields which aren't numbers?

>>> sumRows("rows2.csv") == {'tim': 24.0, 'bob': 11.0, 'anna': 13.0}
True

Does it sum columns correctly?
>>> sumColumns("columns.csv") == {'': 0, 'tim': 5.0, 'bob': 41.0, 'anna': 55.0}
True
"""

# *** DO NOT CHANGE CODE ABOVE THIS LINE ***
# *** DO NOT ADD ANY COMMENTS OF YOUR OWN IN THE SUBMITTED SOLUTION ***

def sumRows(filename, header=False):
	import csv
	with open(filename, "r") as f:
		reader = csv.reader(f)
		result = {}
		if header == True:
			next(reader)
			for row in reader:
				key = row[0]
				result[key] = float(row[1]), float(row[2]), float(row[3])
		else:
			for row in reader:
				key = row[0]
				try:
					result[key] = float(row[1]), float(row[2]), float(row[3])
				except ValueError:
					result[key] = float(row[1]), row[2], float(row[3])
		sums = {k: sum(i for i in v if isinstance(i, float)) for k, v in result.items()}
	return(sums) 		     	

def sumColumns(filename):
	import csv
	with open(filename, "r") as f:
		reader = csv.reader(f)
		result = {}
		numbers = []
		rownum = 0
		for row in reader:
			if rownum == 0:
				header = row
			else:
				colnum = 0
				for col in row:
					numbers.append(float(col))
					colnum+=1
			rownum+=1
	result[header[0]] = numbers[0], numbers[3], numbers[6]
	result[header[1]] = numbers[1], numbers[4], numbers[7]
	result[header[2]] = numbers[2], numbers[5], numbers[8]
	sums = {k: sum(i for i in v if isinstance(i, float)) for k, v in result.items()}
	sums[''] = 0
	return(sums)