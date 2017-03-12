#Modified question 1f to show changes in results if the lowest score is discarded or not
#generates a ba chart to show the difference

def raceSimulation(stats):
	import random

	x = 1
	y = 1

	for q in range(1, 99999):
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

		resultsList = list(seriesResults.items())

		b = resultsList[0]
		bScores = sorted(b[1])
		bTotal = sum(bScores[0:-1])
		bbTotal = sum(bScores)
		
		c = resultsList[1]
		cScores = sorted(c[1])
		cTotal = sum(cScores[0:-1])
		ccTotal = sum(cScores)

		d = resultsList[2]
		dScores = sorted(d[1])
		dTotal = sum(dScores[0:-1])
		ddTotal = sum(dScores)

		e = resultsList[3]
		eScores = sorted(e[1])
		eTotal = sum(eScores[0:-1])
		eeTotal = sum(eScores)

		f = resultsList[4]
		fScores = sorted(f[1])
		fTotal = sum(fScores[0:-1])
		ffTotal = sum(fScores)	

		totals = ([bTotal, cTotal, dTotal, eTotal, fTotal])
		noDiscard = ([bbTotal, ccTotal, ddTotal, eeTotal, ffTotal])

		finalResults = [resultsList[0] for (totals,resultsList) in sorted(zip(totals, resultsList))]
		finalNoDiscard = [resultsList[0] for (noDiscard,resultsList) in sorted(zip(noDiscard, resultsList))]

		if finalResults == finalNoDiscard:
			x = x + 1
		else:
			y = y + 1
			
	print("No change to results")
	print()
	print(str(x) + "/100000")
	print()
	print("Results changed")
	print()
	print(str(y) + "/100000")

	import numpy as np
	import matplotlib.pyplot as plt

	Y=[x, y]
	X=['No Change to Result', 'Change in Result']

	width = .5
	ind = np.arange(len(Y))
	plt.bar(ind, Y)
	plt.xticks(ind + width / 2, X)

	plt.show()