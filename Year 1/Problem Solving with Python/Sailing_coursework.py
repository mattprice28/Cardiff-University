#Question 1a.

def sumScore(a):
	b = sorted(a[1])
	c = sum(b[0:-1])
	print(c)

#Question 1b.

def orderList(a):
	
	b = a[0]
	bScores = sorted(b[1])
	bTotal = sum(bScores[0:-1])
	
	c = a[1]
	cScores = sorted(c[1])
	cTotal = sum(cScores[0:-1])

	d = a[2]
	dScores = sorted(d[1])
	dTotal = sum(dScores[0:-1])

	e = a[3]
	eScores = sorted(e[1])
	eTotal = sum(eScores[0:-1])

	f = a[4]
	fScores = sorted(f[1])
	fTotal = sum(fScores[0:-1])	

	totals = ([bTotal, cTotal, dTotal, eTotal, fTotal])

	r = [a for (totals,a) in sorted(zip(totals, a))]

	print(r)

#Question 1c.

def csvInput(filename):
	import csv
	with open(filename, "r") as f:
		reader = csv.reader(f)
		stats = {}
		next(reader)
		for row in reader:
			key = row[0]
			stats[key] = float(row[1]), float(row[2])
	print(stats)

#Question 1d.

def performance(stats):
	import random
	templist = list(stats.items())

	a = templist[0]
	aScore = a[1]
	aRandom = random.normalvariate(aScore[0], aScore[1])

	b = templist[1]
	bScore = b[1]
	bRandom = random.normalvariate(bScore[0],bScore[1])

	c = templist[2]
	cScore = c[1]
	cRandom = random.normalvariate(cScore[0],cScore[1])

	d = templist[3]
	dScore = d[1]
	dRandom = random.normalvariate(dScore[0],dScore[1])

	e = templist[4]
	eScore = e[1]
	eRandom = random.normalvariate(eScore[0],eScore[1])

	newDict = {a[0]:aRandom, b[0]:bRandom, c[0]:cRandom, d[0]:dRandom, e[0]:eRandom}

	print(newDict)

#Question 1e.

def results(newDict):
	performanceList = list(newDict.items())
	performanceList.sort(key=lambda tup: tup[1], reverse=True)
	results = [tup[0] for tup in performanceList]
	print(results)

#Question 1f.

def raceSimulation(stats):
	import random
	templist = list(stats.items())
	aRace = []
	bRace = []
	cRace = []
	dRace = []
	eRace = []

	for i in range(0, 6):

		a = templist[0]
		aScore = a[1]
		aRandom = random.normalvariate(aScore[0], aScore[1])

		b = templist[1]
		bScore = b[1]
		bRandom = random.normalvariate(bScore[0],bScore[1])

		c = templist[2]
		cScore = c[1]
		cRandom = random.normalvariate(cScore[0],cScore[1])

		d = templist[3]
		dScore = d[1]
		dRandom = random.normalvariate(dScore[0],dScore[1])

		e = templist[4]
		eScore = e[1]
		eRandom = random.normalvariate(eScore[0],eScore[1])

		newDict = {a[0]:aRandom, b[0]:bRandom, c[0]:cRandom, d[0]:dRandom, e[0]:eRandom}

		performanceList = list(newDict.items())
		performanceList.sort(key=lambda tup: tup[1], reverse=True)
		results = [tup[0] for tup in performanceList]

		aRace.append(results.index('Alice') +1)
		bRace.append(results.index('Bob') +1)
		cRace.append(results.index('Clare') +1)
		dRace.append(results.index('Dennis') +1)
		eRace.append(results.index('Eva') +1)

		seriesResults = {'Alice':aRace, 'Bob':bRace, 'Clare':cRace, 'Dennis':dRace, 'Eva':eRace}

	print()
	print("The series results are:")
	print()
	print(seriesResults)

	resultsList = list(seriesResults.items())

	b = resultsList[0]
	bScores = sorted(b[1])
	bTotal = sum(bScores[0:-1])
	
	c = resultsList[1]
	cScores = sorted(c[1])
	cTotal = sum(cScores[0:-1])

	d = resultsList[2]
	dScores = sorted(d[1])
	dTotal = sum(dScores[0:-1])

	e = resultsList[3]
	eScores = sorted(e[1])
	eTotal = sum(eScores[0:-1])

	f = resultsList[4]
	fScores = sorted(f[1])
	fTotal = sum(fScores[0:-1])	

	totals = ([bTotal, cTotal, dTotal, eTotal, fTotal])

	finalResults = [resultsList[0] for (totals,resultsList) in sorted(zip(totals, resultsList))]

	print()
	print("The final results are:")
	print()
	print(finalResults)