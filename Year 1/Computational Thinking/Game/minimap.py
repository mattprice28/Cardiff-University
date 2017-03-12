import player

# Each item in the list represents a floor, which in turn contains a list of
# dictionaries that represent different rooms.

# The 'position' property contains an empty character that is replaced with
# an '@' when the player is in the room.
# The 'entered' property is set to 'True' whenever the player first enters the
# room. When 'entered' is set to true the name of the room is displayed on the minimap.
floors = [
           [
           # Floor 1 rooms
             {
               "id": 0,
               "name": "Patient Room 4A",
               "position": ' ',
               "entered": False
             },
             {
               "id": 1,
               "name": "Patient Room 4B",
               "position": ' ',
               "entered": False
             },
             {
               "id": 2,
               "name": "Corridor",
               "position": ' ',
               "entered": False
             },
             {
               "id": 3,
               "name": "Stairs",
               "position": ' ',
               "entered": True
             }
           ],

           [
           # Floor 2 rooms
             {
               "id": 0,
               "name": "Patient Room 3A",
               "position": ' ',
               "entered": False
             },
             {
               "id": 1,
               "name": "Patient Room 3B",
               "position": ' ',
               "entered": False
             },
             {
               "id": 2,
               "name": "Storage Room",
               "position": ' ',
               "entered": False
             },
             {
               "id": 3,
               "name": "Corridor",
               "position": ' ',
               "entered": False
             },
             {
               "id": 4,
               "name": "Doctor's Office",
               "position": ' ',
               "entered": False
             },
             {
               "id": 5,
               "name": "Stairs",
               "position": ' ',
               "entered": True
             }
            ],

            [
            # Floor 3 rooms
             {
               "id": 0,
               "name": "Patient Room A",
               "position": ' ',
               "entered": False
             },
             {
               "id": 1,
               "name": "Patient Room B",
               "position": ' ',
               "entered": False
             },
             {
               "id": 2,
               "name": "Patient Room C",
               "position": ' ',
               "entered": False
             },
             {
               "id": 3,
               "name": "Storage Room",
               "position": ' ',
               "entered": False
             },
             {
               "id": 4,
               "name": "North Corridor",
               "position": ' ',
               "entered": False
             },
             {
               "id": 5,
               "name": "Staff Room",
               "position": ' ',
               "entered": False
             },
             {
               "id": 6,
               "name": "Stairs",
               "position": ' ',
               "entered": True
             },
             {
               "id": 7,
               "name": "Lab",
               "position": ' ',
               "entered": False
             },
             {
               "id": 8,
               "name": "South Corridor",
               "position": ' ',
               "entered": False
             },
             {
               "id": 9,
               "name": "A&E",
               "position": ' ',
               "entered": False
             },
             {
               "id": 10,
               "name": "Toilets",
               "position": ' ',
               "entered": False
             },
             {
               "id": 11,
               "name": "Main Reception",
               "position": ' ',
               "entered": False
             }
            ]
         ]
# The 'maps' array stores the visual representation for each floor's map.
# The 'format' function is used instead of concatenating strings using the
# '+' operator because it keeps the map looking relatively clean and easy
# to understand.

# I defined the maps list inside of a function that is called every time the
# map is printed because the format function needs to be run every time to
# update the player's position.
def get_maps():
    maps = [
        # Floor 1 map
        (
        "+-----------------------------------------------------------------------------+\n"
        "|                                 MAP                                         |\n"
        "+-----------------------------------------------------------------------------+\n"
        "|                                                                             |\n"
        "|     +-----------------+     +-----------------+                             |\n"
        "|     | {0} |     | {1} |                             |\n"
        "|     |        {2}        |-----|        {3}        |                             |\n"
        "|     +-----------------+     +-----------------+                             |\n"
        "|                                       |                                     |\n"
        "|                                       |                                     |\n"
        "|                             +-----------------+                             |\n"
        "|                             |    {4}     |                             |\n"
        "|                             |        {5}        |                             |\n"
        "|                             +-----------------+                             |\n"
        "|                                       |                                     |\n"
        "|                                       |                                     |\n"
        "|                             +-----------------+                             |\n"
        "|                             |     {6}      |                             |\n"
        "|                             |      {7}          |                             |\n"
        "|                             +-----------------+                             |\n"
        "|                                                                             |\n"
        "+-----------------------------------------------------------------------------+\n"
        .format(
                 floors[0][0]["name"] if floors[0][0]["entered"] == True else ' ' * len(floors[0][0]["name"]),
                 floors[0][1]["name"] if floors[0][1]["entered"] == True else ' ' * len(floors[0][1]["name"]),
                 floors[0][0]["position"],
                 floors[0][1]["position"],
                 floors[0][2]["name"] if floors[0][2]["entered"] == True else ' ' * len(floors[0][2]["name"]),
                 floors[0][2]["position"],
                 floors[0][3]["name"] if floors[0][3]["entered"] == True else ' ' * len(floors[0][3]["name"]),
                 floors[0][3]["position"]
                )
        ),
        # Floor 2 map
        (
        "+-----------------------------------------------------------------------------+\n"
        "|                                     MAP                                     |\n"
        "+-----------------------------------------------------------------------------+\n"
        "|                                                                             |\n"
        "|     +-----------------+     +-----------------+                             |\n"
        "|     | {0} |     | {1} |                             |\n"
        "|     |        {2}        |-----|        {3}        |                             |\n"
        "|     +-----------------+     +-----------------+                             |\n"
        "|                                       |                                     |\n"
        "|                                       |                                     |\n"
        "|     +------------------+    +-----------------+    +-----------------+      |\n"
        "|     |   {4}   |    |     {5}    |    | {6} |      |\n"
        "|     |         {7}        |----|         {8}       |----|        {9}        |      |\n"
        "|     +------------------+    +-----------------+    +-----------------+      |\n"
        "|                                       |                                     |\n"
        "|                                       |                                     |\n"
        "|                             +-----------------+                             |\n"
        "|                             |      {10}     |                             |\n"
        "|                             |        {11}        |                             |\n"
        "|                             +-----------------+                             |\n"
        "|                                                                             |\n"
        "+-----------------------------------------------------------------------------+\n"
      .format(
               floors[1][0]["name"] if floors[1][0]["entered"] == True else ' ' * len(floors[1][0]["name"]),
               floors[1][1]["name"] if floors[1][1]["entered"] == True else ' ' * len(floors[1][1]["name"]),
               floors[1][0]["position"],
               floors[1][1]["position"],
               floors[1][2]["name"] if floors[1][2]["entered"] == True else ' ' * len(floors[1][2]["name"]),
               floors[1][3]["name"] if floors[1][3]["entered"] == True else ' ' * len(floors[1][3]["name"]),
               floors[1][4]["name"] if floors[1][4]["entered"] == True else ' ' * len(floors[1][4]["name"]),
               floors[1][2]["position"],
               floors[1][3]["position"],
               floors[1][4]["position"],
               floors[1][5]["name"] if floors[1][5]["entered"] == True else ' ' * len(floors[1][5]["name"]),
               floors[1][5]["position"]
              )
        ),
        # Floor 3 map
        (
        "+-----------------------------------------------------------------------------+\n"
        "|                                 MAP                                         |\n"
        "+-----------------------------------------------------------------------------+\n"
        "|     +-----------------+     +-----------------+     +-----------------+     |\n"
        "|     | {0}  |     | {1}  |     | {2}  |     |\n"
        "|     |        {3}        |-----|        {4}        |-----|        {5}        |     |\n"
        "|     +-----------------+     +-----------------+     +-----------------+     |\n"
        "|               |                       |                       |             |\n"
        "|               |                       |                       |             |\n"
        "|     +-----------------+     +-----------------+     +-----------------+     |\n"
        "|     |  {6}   |     | {7}  |     |                 |     |\n"
        "|     |        {8}        |     |        {9}        |     |                 |     |\n"
        "|     +-----------------+     +-----------------+     |                 |     |\n"
        "|                                       |             |                 |     |\n"
        "|                                       |             |   {10}    |     |\n"
        "|                                       |             |                 |     |\n"
        "|     +-----------------+     +-----------------+     |        {11}        |     |\n"
        "|     |                 |     |      {12}     |     |                 |     |\n"
        "|     |                 |     |        {13}        |     |                 |     |\n"
        "|     |                 |     +-----------------+     +-----------------+     |\n"
        "|     |                 |                                       |             |\n"
        "|     |       {14}       |                                       |             |\n"
        "|     |                 |                                       |             |\n"
        "|     |        {15}        |     +-----------------+     +-----------------+     |\n"
        "|     |                 |     | {16}  |     |                 |     |\n"
        "|     |                 |     |        {17}        |-----|                 |     |\n"
        "|     +-----------------+     +-----------------+     |                 |     |\n"
        "|               |                       |             |                 |     |\n"
        "|               |                       |             |       {18}       |     |\n"
        "|               |                       |             |                 |     |\n"
        "|     +-----------------+     +-----------------+     |        {19}        |     |\n"
        "|     |     {20}     |     | {21}  |     |                 |     |\n"
        "|     |        {22}        |-----|        {23}        |     |                 |     |\n"
        "|     +-----------------+     +-------|  |------+     +-----------------+     |\n"
        "|                                     EXIT                                    |\n"
        "+-----------------------------------------------------------------------------+\n"
        .format(
                 floors[2][0]["name"] if floors[2][0]["entered"] == True else ' ' * len(floors[2][0]["name"]),
                 floors[2][1]["name"] if floors[2][1]["entered"] == True else ' ' * len(floors[2][1]["name"]),
                 floors[2][2]["name"] if floors[2][2]["entered"] == True else ' ' * len(floors[2][2]["name"]),
                 floors[2][0]["position"],
                 floors[2][1]["position"],
                 floors[2][2]["position"],
                 floors[2][3]["name"] if floors[2][3]["entered"] == True else ' ' * len(floors[2][3]["name"]),
                 floors[2][4]["name"] if floors[2][4]["entered"] == True else ' ' * len(floors[2][4]["name"]),
                 floors[2][3]["position"],
                 floors[2][4]["position"],
                 floors[2][5]["name"] if floors[2][5]["entered"] == True else ' ' * len(floors[2][5]["name"]),
                 floors[2][5]["position"],
                 floors[2][6]["name"] if floors[2][6]["entered"] == True else ' ' * len(floors[2][6]["name"]),
                 floors[2][6]["position"],
                 floors[2][7]["name"] if floors[2][7]["entered"] == True else ' ' * len(floors[2][7]["name"]),
                 floors[2][7]["position"],
                 floors[2][8]["name"] if floors[2][8]["entered"] == True else ' ' * len(floors[2][8]["name"]),
                 floors[2][8]["position"],
                 floors[2][9]["name"] if floors[2][9]["entered"] == True else ' ' * len(floors[2][9]["name"]),
                 floors[2][9]["position"],
                 floors[2][10]["name"] if floors[2][10]["entered"] == True else ' ' * len(floors[2][10]["name"]),
                 floors[2][11]["name"] if floors[2][11]["entered"] == True else ' ' * len(floors[2][11]["name"]),
                 floors[2][10]["position"],
                 floors[2][11]["position"]
                )
        )
       ]

    return maps

def print_map(floor_number):
    # Sets the current minimap position of the player to the corresponding room.
    current_position = player.current_room["id"]

    # Sets every room's position back to ' ' so that the '@ symbol is only ever shown in one room.
    for room in floors[floor_number]:
        room["position"] = ' '

    # Sets the position of the room the player is currently in to '@'
    floors[floor_number][current_position]["position"] = '@'

    # Updates the maps and stores them in a list in the local scope of this function
    maps = get_maps()
    
    # Prints the map to the screen
    print(maps[floor_number])