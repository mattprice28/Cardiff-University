# This is the same as the template, except for one small difference
# The 'type' property has been added which determines whether an item can be
# picked up or not.

static_item_cabinet = {
	"id": "cabinet",

	"name": "a cabinet",

	"description":
		"You open the cabinet to look at it's contents.",

	"type": "static"
}

static_item_shelf = {
	"id": "shelf",

	"name": "a shelf",

	"description":
		"You climb on a box to look on top of a high shelf.",

	"type": "static"
}

static_item_vent = {
	"id": "vent",

	"name": "a vent",

	"description":
		"There is a vent on the wall.",

	"type": "static"
}

static_item_medicine_cabinet = {
	"id": "medicabinet",

	"name": "a medicine cabinet",

	"description":
		"You move close to the medicine cabinet to investigate.",

	"type": "static"
}

static_item_tray = {
	"id": "tray",

	"name": "tray",

	"description": "",

	"type": "static"
}

static_item_alarm = {
	"id": "alarm",

	"name": "an alarm system",

	"description": "",

	"type": "static"
}

item_screwdriver = {
	"id": "screwdriver",

	"name": "screwdriver",

	"description":
		"This screwdriver will be useful if anything needs to be opened.",

	"type": "carryable"
}

item_id = {
	"id": "id",

	"name": "id badge",

	"description":
		"This ID belonged to a Dr Martin Jones. This may be very useful.",

	"type": "carryable"
}

item_paper = {
	"id": "paper",

	"name": "Slip of paper with code on",

	"description":
		"This piece of paper has some numbers and letters written on it. Probably doesn't mean anything.",

	"type": "carryable"
}

item_riddle = {
	"id": "riddle",

	"name": "a slip of paper with riddle on",

	"description":  "One wire leads to salvation\n"
					"One wire seals you in\n"
					"One wire gives you a shock\n"
					"The last doesn't do anything\n"
					"The open and close are neighbours\n"
					"So are the blank and the zing\n"
					"The exit is close to the centre\n"
					"To the left of the one with nothing",

	"type": "carryable"
}

item_riddleitems = {
	"id": "riddleitems",

	"name": "items for riddle",

	"description": "",

	"type": "carryable"
}

item_bandage = {
	"id": "bandage",

	"name": "Bandage",

	"description":
		"It's not cleanest of bandages but it may be useful.",

	"type": "carryable"
}

item_key = {
	"id": "key",

	"name": "a key",

	"description":
		"A key which can be used to open doors.",

	"type": "carryable"
}

item_medicine = {
	"id": "medicine",

	"name": "medicine",

	"description":
		"The label on the medicine reads 'Neurological Medicine'.",

	"type": "carryable"
}

item_keycard = {
	"id": "keycard",

	"name": "a keycard",

	"description":
		"This keycard might open something important.",

	"type": "carryable"
}

item_wirepaper = {
	"id": "wirepaper",

	"name": "Slip of paper with wire combination on it",

	"description":
		"There seems to be a diagram of a wire combination drawn on it.",

	"type": "carryable"
}

item_scalpel = {
	"id": "scalpel",

	"name": "a scalpel",

	"description":
		"Maybe this scalpel can be used to cut something open.",

	"type": "carryable"
}

item_toiletkey = {
	"id": "toilet key",

	"name": "key for the toilet",

	"description":
		"This key looks different compared to the other keys found. It is probably used for something else.",

	"type": "carryable"
}

static_item_leaflet = {
	"id": "leaflet",

	"name": "Leaflet",

	"description":
		"A leaflet with some information regarding the outbreak.\n"
		"\"It still isn't known where the virus came from, or how it spreads and "
		"all we \ncan do is to try and stop it from reaching any further. The hospital "
		"is on \nmaximum security lockdown and all patients and non-essential staff have "
		"been \nevacuated until further notice.\"",

	"type": "static"
}

static_item_officememo = {
	"id": "memo",

	"name": "Office memo",

	"description":
		"A note from a lab assistant to a doctor.\n"
		"\"Do you have any more samples we can use down here? "
		"We're running out and we aren't getting any closer to finding a solution.\"",

	"type": "static"
}

static_item_lettertodoctorswife = {
	"id": "letter",

	"name": "Letter to doctor's wife",

	"description":
		"A letter a doctor wrote for his wife.\n"
		"\"To my sweetheart,\n"
		"I'm sorry that you have to find out this way, but I won't be coming home. "
		"Our research has led us nowhere and we have all been exposed - even now my "
		"memories are becoming hazy. This virus is unstoppable - get out of the country "
		"as quickly as you can. Our only hope now is to contain it. I just hope this "
		"letter reaches you in time.\n"
		"I love you.\n\n"
		"- Martin",

	"type": "static"
}

static_item_researchnotes = {
	"id": "notes",

	"name": "Research notes",

	"description":
		"Some notes that have been left in the lab.\n"
		"\"Finally we have made a breakthrough. The virus doesn't affect everybody equally - "
		"more than 85%% of those with the virus die within 72 hours, however the lucky few only suffer "
		"memory loss but otherwise seem unaffected. We still don't know how long the memories will take "
		"to return, if ever. All we know is that these people are our only hope. We need to find out "
		"what is different about them. Then, and only then will we be able to find a cure.",

	"type": "static"
}

#A few more variables used in the events file
room1_cabinet_opened = False
shelf_checked = False
vent_opened = False
tray_checked = False