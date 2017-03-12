def randomResults():

	import random

	student = {}

	allResults = []

	year = [1, 2, 3]

	course = ["Comp Sci", "Comp Sci Specialist","BIS", "Software Eng", "Joints"]

	answer = [1, 2, 3, 4]

	for x in range(0,20):
			
		student = {"year":random.choice(year), "course":random.choice(course), "Activist": random.choice(answer), "Theorist": random.choice(answer), "Pragmatist": random.choice(answer), "Reflector": random.choice(answer), "Visual": random.choice(answer), "Audio": random.choice(answer), "Reading": random.choice(answer), "Kinesthetic": random.choice(answer)}

		allResults.append(student)

	print(allResults)

		 
