from npc import *
from items import *

#Very similar to the template, only with a few changes.
#Rooms have id's, necessary for the minimap
#'events' and 'npc' have both been added
#These work like items in that the id of the npc is stored.
#The events one is slightly different in that it stores a string of the name of it's corresponding function in events.py
#The string can then be called as a function from the check_events function in the game.py file.

fourth_floor_patient_room_4A = {
    "id": 0,

    "name": "Patient's room 4A",
    
    "description":
        "You are standing alone in a patient room, rows of empty beds "
        "line the walls, \nvarious machines are making beeping sounds "
        "and lights are blinking, nothing else makes a sound.",

    "exits": {"east": "Patient's room 4B"},
    "items": [],
    "events": [],
    "npc": []
}


fourth_floor_patient_room_4B = {
    "id": 1,

    "name": "Patient's room 4B",

    "description":
        "Another patient room, the beds are empty and an eerie silence "
        "hangs over the \nroom. There is a cabinet in the corner with the "
        "door slightly ajar.",

    "exits": {"south": "4th Floor Corridor", "west": "Patient's room 4A"},
    "items": [static_item_cabinet],
    "events": ["room1_cabinet"],
    "npc": []
}


fourth_floor_corridor = {
    "id": 2,

    "name": "4th Floor Corridor",

    "description":
        "You are stood in an empty corridor. Most of the doors are "
        "barricaded and \ncovered in signs saying 'Quarantine', better "
        "not stay here too long.",

    "exits": {"south": "4th Floor Stairs" ,"north": "Patient's room 4B"},
    "items": [],
    "events": [],
    "npc": []
}

fourth_floor_stairs = {
    "id": 3,

    "name": "4th Floor Stairs",

    "description": "",

    "exits" : {"north": "4th Floor Corridor"},
    "items": [],
    "events": ["open_fourth_floor_stairs"],
    "npc": []
}

third_floor_patients_room_3A = {
    "id": 0,

    "name": "Patient's Room 3A",

    "description":
        "You are stood in another empty patient room. You notice a large vent "
        "cover \nagainst one wall.",

    "exits": {"east": "Patient's Room 3B"},
    "items": [static_item_vent],
    "events": ["examine_vent"],
    "npc": []
}

third_floor_patients_room_3B = {
    "id": 1,

    "name": "Patient's Room 3B",

    "description":
        "You are stood in an empty patient room, the abandoned beds look "
        "like they were \nleft in a hurry; there is a leaflet on one of the beds.",

    "exits": {"west": "Patient's Room 3A", "south": "3rd Floor Corridor"},
    "items": [static_item_leaflet],
    "events": [],
    "npc": []
}

third_floor_storage_room = {
    "id": 2,

    "name": "3rd Floor Storage Room",

    "description":
        "You are stood in a storage room, cleaning supplies and tools line the "
        "shelves. \nMaybe some of these tools can be of use to you.",

    "exits": {"east": "3rd Floor Corridor"},
    "items": [static_item_shelf],
    "events": ["check_shelf_3rd_floor_supply"],
    "npc": []
}

third_floor_corridor = {
    "id": 3,

    "name": "3rd Floor Corridor",

    "description":
        "You are stood in an empty corridor. There are doors throughout "
        "the corridor \nthat lead to various rooms. Perhaps you should "
        "check them out.",

    "exits": {"south": "3rd Floor Stairs", "north": "Patient's Room 3B", "west": "3rd Floor Storage Room", "east": "3rd Floor Doctor's Office"},
    "items": [],
    "events": [],
    "npc": []
}


third_floor_doctors_office = {
    "id": 4,

    "name": "3rd Floor Doctor's Office",

    "description": 
        "You are stood in a large luxurious office, the walls are covered from "
        "floor to ceiling with rows of books and medical journals. There is a "
        "large wooden desk in the middle of the room and behind the desk a doctor "
        "is sat casually in his chair; something strange is going on here.\n"
        "You also notice a letter sitting on the doctor's desk.",
      
    "exits": {"west": "3rd Floor Corridor"},
    "items": [static_item_lettertodoctorswife],
    "events": ["doctor_talk"],
    "npc": [npc_doctor]  
}

third_floor_stairs = {
    "id": 5,

    "name": "3rd Floor Stairs",

    "description": "",
    "exits": {"north": "3rd Floor Corridor"},
    "items": [],
    "events": ["open_third_floor_stairs"],
    "npc": []
}

second_floor_corridor = {
    "id": 10,

    "name": "2nd Floor Corridor",

    "description":
        "You are stood in an empty corridor. There are doors throughout the "
        "corridor that lead to various rooms. Perhaps you should check them out.",

    "exits": {"south": "2nd Floor Stairs", "east": "2nd Floor Staff Room","north": "Patient's room 2B"},
    "items": [],
    "events": [],
    "npc": []
}

second_floor_patient_room_2B = {
    "id": 11,

    "name": "Patient's Room 2B",

    "description":
        "Yet another empty patient room. What happened here?",

    "exits": {"south": "2nd Floor Corridor", "east": "Patient's room 2C"},
    "items": [],
    "events": [],
    "npc": []
}

second_floor_patient_room_2C = {
    "id": 12,

    "name": "Patient's Room 2C",

    "description":
        "When you first step into this room a noxious smell fills your nostrils. You feel "
        "slightly disorientated, the ceiling lights flicker casting the room into "
        "strange shadows. Working your way slowly into the room you discover the source "
        "of the smell - a body in a lab coat is slumped against the staff room door. The body "
        "is completely still, a look of fear frozen on his lifeless face. You notice a small "
        "square of paper clutched in his hand.",

    "exits": {"south": "2nd Floor Staff Room", "west": "Patient's room 2B"},
    "items": [],
    "events": [],
    "npc": []
}

second_floor_staff_room = {
    "id": 13,

    "name": "2nd Floor Staff Room",

    "description":
        "You are stood in a large room. There are numerous comfortable looking "
        "chairs. A small kitchen area is located at the far end of the room where "
        "you see a nurse holding a mug in both hands; but she doesn’t drink "
        "from it, she simply looks at you with a glimmer of hope.",

    "exits": {"west": "2nd Floor Corridor", "north": "Patient's room 2C", "south": "Safe Room"},
    "items": [],
    "events": [],
    "npc": [npc_nurse]
}

second_floor_safe_room = {
    "id": 14,

    "name": "Safe Room",

    "description":
    "This is the room which the player can be safe",

    "exits": {"north": "2nd Floor Staff Room"},
    "items": [],
    "events": [],
    "npc": []
}

second_floor_stairs = {
    "id": 15,

    "name": "2nd Floor Stairs",

    "description": "",

    "items": [],
    "events": [],
    "npc": []
}

first_floor_north_corridor = {
    "name": "1st Floor North Corridor",

    "description":
    """You are stood in an empty corridor. There are doors throughout the corridor
that lead to various rooms. Perhaps you should check them out.""",

    "exits": {"west": "1st Floor Storage room", "east": "1st Floor Doctor’s Office"},
    "items": [],
    "events": [],
    "npc": []
}

first_floor_storage_room = {
    "name": "1st Floor Storage Room",
    
    "description":
    """You are stood in a storage room. There is various equipment is scattered 
around but what draws your attention is a giant hole in the wall. If you
crouch south you could crawl through that space.""",

    "exits": {"south": "1st Floor Lab"},
    "items": [],
    "events": [],
    "npc": []
}

first_floor_lab = {
    "name": "1st Floor Lab",

    "description":
    """You enter a pristinely clean lab. There are microscopes and test samples
around the room…better not touch anything. There is a lab technician stood 
staring into a microscope at a Petri dish. There is a large bloodstain on 
his lab coat, perhaps you could help him.""",

    "exits": {"south": "Toilets", "north": "1st Floor Storage Room", "east": "1st Floor South Corridor"},
    "items": [],
    "events": [],
    "npc": []
}

first_floor_south_corridor = {
    "name": "1st Floor South Corridor",

    "description":
    """You are stood in an empty corridor. There are doors throughout the corridor
that lead to various rooms. Perhaps you should check them out.""",

    "exits": {"west": "1st Floor Lab", "south": "1st Floor Reception"},
    "items": [],
    "events": [],
    "npc": []
}

first_floor_reception = {
    "name": "1st Floor Reception",

    "description":
    """You are stood on the 1st Floor Reception. There should be a receptionist behind
that desk and the room would usually be full of people but it is dauntingly
quiet and empty.""",

    "exits": {"north": "1st Floor South Corridor", "east": "1st Floor Supply Room", "west": "Toilets"},
    "items": [],
    "events": [],
    "npc": []
}

first_floor_supply_room = {
    "name": "1st Floor Supply Room",

    "description":
    """The supply room is full of cleaning tools and products. There are some brooms
and hoovers lying around. Out of the corner of your eye you notice a cleaner. 
Perhaps this cleaner could be of use.""",

    "exits": {"west": "1st Floor Reception"},
    "items": [],
    "events": [],
    "npc": [npc_cleaner]
}

first_floor_doctors_office = {
    "name": "First Floor Doctor’s Office",

    "description":
    """You are stood in what appears to be a Doctor’s office. Nothing of note catches
your attention but maybe you should look around some more.""",

    "exits": {"west": "1st Floor North Corridor"},
    "items": [],
    "events": [],
    "npc": []

}

ground_floor_patient_room_0A = {
    "id": 0,

    "name": "Patient room 0A",

    "description":
        "Another patient room. The beds are all empty and there is an eerie silence. "
        "The room is dark, although you can just barely make out a memo left on a table.",

    "exits": {"south": "Ground Floor Storage Room", "east": "Patient room 0B"},
    "items": [static_item_officememo],
    "events": [],
    "npc": []
}

ground_floor_patient_room_0B = {
    "id": 1,

    "name": "Patient room 0B",

    "description":
        "You are stood in a patient room. Apart from the empty beds that line the walls "
        "and the odd machines that are beeping, there is nothing else of interest.""",

    "exits": {"west": "Patient room 0A", "east": "Patient room 0C", "south": "Ground Floor North Corridor"},
    "items": [],
    "events": [],
    "npc": []
}

ground_floor_patient_room_0C = {
    "id": 2,

    "name": "Patient room 0C",

    "description":
    "You are in yet another patient room. There is an overturned bed which shows signs "
    "of a struggle. There is a medicine cabinet with a strange lock mechanism that draws "
    "your attention.",

    "exits": {"south": "Ground Floor Staff Room", "west": "Patient room 0B"},
    "items": [static_item_medicine_cabinet],
    "events": ["ground_floor_numbers_minigame"],
    "npc": []
}

ground_floor_storage_room = {
    "id": 3,

    "name": "Ground Floor Storage Room",

    "description":
        "A storage room with different medical tools on tabletops and wall hangings. "
        "There is a patient in the corner of the room. Perhaps they could help you? ",

    "exits": {"north": "Patient room 0A"},
    "items": [],
    "events": ["npc_patient_convo"],
    "npc": [npc_patient]
}

ground_floor_north_corridor = {
    "id": 4,

    "name": "Ground Floor North Corridor",

    "description":
        "You are stood in an empty corridor. There are doors throughout the corridor that "
        "lead to various rooms. Perhaps you should check them out.",

    "exits": {"north": "Patient room 0B"},
    "items": [],
    "events": [],
    "npc": []
}

ground_floor_staff_room = {
    "id": 5,

    "name": "Ground Floor Staff Room",

    "description":
        "This room is clearly a staff room. There is a table in the middle with a jar "
        "of coffee on it and several mugs. A researcher is hunched over in a chair "
        "staring at the wall. Perhaps you should investigate.",

    "exits": {"north": "Patient room 0C", "south": "A&E"},
    "items": [],
    "events": ["open_staff_room", "npc_researcher_convo"],
    "npc": [npc_researcher]
}

ground_floor_stairs = {
    "id": 6,

    "name": "Stairs",

    "description": "",

    "exits": {"north": "Ground Floor North Corridor"},
    "items": [],
    "events": [],
    "npc": []
}

ground_floor_lab = {
    "id": 7,

    "name": "Ground Floor Lab",

    "description":
        "You are now in the lab. Lab coats and safety goggles are hung on the north wall, "
        "chemicals are scattered across the room and a pile of research notes are spread "
        "across a nearby table. A box of cables catches your attention.",

    "exits": {"south": "Toilets"},
    "items": [static_item_researchnotes, static_item_alarm],
    "events": ["examine_alarm"],
    "npc": []
}

ground_floor_south_corridor = {
    "id": 8,

    "name": "Ground Floor South Corridor",

    "description":
        "You are stood in an empty corridor. There are doors throughout the corridor that "
        "lead to various rooms. Perhaps you should check them out.",

    "exits": {"south":"Main Reception", "east": "A&E"},
    "items": [],
    "events": [],
    "npc": []
}

ground_floor_a_and_e = {
    "id": 9,

    "name": "A&E",

    "description":
        "You are stood in the accident and emergency room. There are a few wheel chairs scattered "
        "around the room and a few of the chairs have had the stuffing ripped out of them. "
        "You notice a tray of surgical equipment scattered across the floor.",

    "exits":{"west": "Ground Floor South Corridor", "north": "Ground Floor Staff Room"},
    "items": [static_item_tray],
    "events": ["examine_tray"],
    "npc": []
}

ground_floor_toilets = {
    "id": 10,

    "name": "Toilets",

    "description":
        "A standard hospital restroom. A few cubicles and a couple of urinals adorn the walls. "
        "You notice a patch of blood in one of the cubicles... There is a door at the end of the room.",

    "exits": {"east": "Main Reception", "north": "Ground Floor Lab"},
    "items": [],
    "events": ["open_toilets"],
    "npc": []
}

ground_floor_main_reception = {
    "id": 11,

    "name": "Main Reception",

    "description":
        "You are stood in the main reception of the hospital. You notice a set of bloody footprints "
        "leading to the exit. There is a desk with a receptionist stood behind, fussing with some "
        "documents. Perhaps you should speak to her.",

    "exits": {"north": "Ground Floor South Corridor", "south": "Exit", "west": "Toilets"},
    "items": [],
    "events": ["npc_receptionist_convo"],
    "npc": [npc_receptionist]
}

exit = {
    "id": 12,
    "name": "Exit",
    "description": "",
    "exits": {"north": "Main Reception"},
    "items": [],
    "events": ["leave"],
    "npc": []

}


rooms = {
    "Patient's room 4A": fourth_floor_patient_room_4A,
    "Patient's room 4B": fourth_floor_patient_room_4B,
    "4th Floor Corridor": fourth_floor_corridor,
    "4th Floor Stairs": fourth_floor_stairs,
    "3rd Floor Corridor": third_floor_corridor,
    "Patient's Room 3B": third_floor_patients_room_3B,
    "3rd Floor Storage Room": third_floor_storage_room,
    "3rd Floor Doctor's Office": third_floor_doctors_office,
    "Patient's Room 3A": third_floor_patients_room_3A,
    "3rd Floor Stairs": third_floor_stairs,
    "2nd Floor Corridor": second_floor_corridor,
    "Patient's Room 2B": second_floor_patient_room_2B,
    "Patient's Room 2C": second_floor_patient_room_2C,
    "2nd Floor Staff Room": second_floor_staff_room,
    "Safe Room": second_floor_safe_room,
    "2nd Floor Stairs": second_floor_stairs,
    "1st Floor North Corridor": first_floor_north_corridor,
    "1st Floor Storage Room": first_floor_storage_room,
    "1st Floor Lab": first_floor_lab,
    "1st Floor South Corridor": first_floor_south_corridor,
    "1st Floor Reception": first_floor_reception,
    "1st Floor Supply Room": first_floor_supply_room,
    "1st Floor Doctor’s Office": first_floor_doctors_office,
    "Ground Floor South Corridor": ground_floor_south_corridor,
    "Ground Floor North Corridor": ground_floor_north_corridor,
    "Patient room 0B": ground_floor_patient_room_0B,
    "Patient room 0C": ground_floor_patient_room_0C,
    "Patient room 0A": ground_floor_patient_room_0A,
    "Ground Floor Storage Room": ground_floor_storage_room,
    "Ground Floor Staff Room": ground_floor_staff_room,
    "Ground Floor Stairs": ground_floor_stairs,
    "Ground Floor Lab": ground_floor_lab,
    "Toilets": ground_floor_toilets,
    "Main Reception": ground_floor_main_reception,
    "A&E": ground_floor_a_and_e,
    "Exit": exit
}
