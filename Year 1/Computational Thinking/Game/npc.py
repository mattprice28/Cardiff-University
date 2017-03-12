#The npc file is very similar to the items file.
#It merely hold the id, name, description and greeting(if needed) of the npc
#There are more npcs here than there are in the game, as we were unable to 
#implement the two middle floors within the time limit.

npc_doctor = {
	"id": "doctor",

	"name": "Doctor",

	"description":
		"The doctor is middle aged and graying, he looks as if he hasn't slept in a long time. "
		"He appears to be very focused on whatever it is he's doing.",

	"greeting": ""
}

npc_nurse = {
	"id": "nurse",

	"name": "Nurse",

	"description":
		"The nurse is a young girl who looks very distressed. She looks like she is sleep deprived, "
		"which seems to be a theme in this place. She is sifting though a massive pile of books and "
		"papers.",

	"greeting":
		"Erm, hi there, I heard that you weren't included in the patient evac. I suppose that you're trying "
		"to get down to the ground floor?"
}

npc_tech = {
	"id": "tech",

	"name": "Lab Tech",

	"description":
		"The lab tech appears to be in a surprisingly good state considering the current situation. His hand is "
		"bleeding from a nasty looking wound. He is trying to do work with an assortment of flasks and tubes, but "
		"the blood from his hand is dripping into them and mixing with whatever is inside.",

	"greeting":
		"h.. hi.. I thought I'd heard someone come in. As you can see I'm in quite a sticky situation here."
}

npc_cleaner = {
	"id": "cleaner",

	"name": "Cleaner",

	"description":
		"The cleaner is wondering around aimlessly. She seems out of place, as if she feels that she shouldn't be there. "
		"Having a clean working enviroment probably isn't the number one priority at this time.",

	"greeting": "Who are you?",
}

npc_patient = {
	"id": "patient",

	"name": "Patient",

	"description":
		"The patient is still wearing a hospital gown and appears to be slightly crazed. "
		"It's probably best to be careful around this one.",

	"greeting":
		""
}

npc_researcher = {
	"id": "researcher",

	"name": "Researcher",

	"description":
		"This man has a sense of wisdom, despite his lack of movement. "
		"If anybody can get you out of this place, it's probably him.",

	"greeting": ""
}

npc_receptionist = {
	"id": "receptionist",

	"name": "Receptionist",

	"description":
		"Why would this hospital need a receptionist in the middle of an epidemic?!",
	
	"greeting":
		"You look like you belong here just as much as I do. What is it you want?"
}