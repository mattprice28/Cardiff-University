#Most of this is from the template, so it's not worth explaining

from map import rooms
from items import *

inventory = []

# Start game at the reception
current_room = rooms["Patient's room 4A"]
# To go along with the current_room we added current_floor
# It is used to determine which floor the user is on, so that
# the minimap can be displayed correctly.
# Floors should begin at 0 for ease of use
current_floor = 0

#An assortment of variables used for checking conditions in the events file.
#There could have been a file dedicated to these, but we felt that it would
#Be easier to put them here considering the time limit.
fourth_floor_stairs_checked = False
third_floor_stairs_checked = False
medicabinet_unlocked = False
doctor_talk = False
doctor_talk2 = False
patient_talk = False
patient_talk2 = False
researcher_talk = False
staff_room_door_open = False
toilet_door_open = False
toilet_key_got = False