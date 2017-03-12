#!/usr/bin/python3
import os
import sys
import time
from game_parser import *
from items import *
from npc import *
from events import *
from map import rooms
import player
from minimap import *

def intro():
    #The intro function is the function which is run once when the game first starts.
    #It runs the animation sequence and the scrolling dialoge at the beginning of the game.
    intro_name = ["   ___               __    ___      __           _______  ___            _____ \n",
                  "  /   \   |      |  /  \  |   \    /  \  |\    |    |      |    |\    | |      \n",
                  " /     \  |      | |    | |    \  |    | | \   |    |      |    | \   | |      \n",
                  "|       | |      | |____| |___ /  |____| |  \  |    |      |    |  \  | |_____ \n",
                  " \    \/   \    /  |    | |    \  |    | |   \ |    |      |    |   \ | |      \n",
                  "  \___/\    \__/   |    | |     \ |    | |    \|    |     _|_   |    \| |_____ \n",
                  "_______________________________________________________________________________\n",
                  "                                        _____ \n",
                  "                                 /|          |\n",
                  "                                / |          |\n",
                  "                                  |     _____|\n",
                  "                                  |          |\n",
                  "                               ___|___  _____|\n\n"
                 ]
    intro_static_syringe = [
                            "                       _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n",
                            "                      / | ' | '|| ' | ' |       ||         |\n",
                            "              _ _ _ _/       o ||_ _ _ _ _ _ _ _||_ _ _ _ _|\n",
                            "             '       \         ||               ||         |\n",
                            "                      \_ _ _ _ ||_ _ _ _ _ _ _ _||_ _      |\n\n"
                           ]

    intro_anim_syringe = [
                           ("                       _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n"
                            "                      / | ' ||| | ' | ' |       ||       |\n"
                            "              _ _ _ _/     o ||_ _ _ _ _ _ _ _ _||_ _ _ _|\n"
                            "             o       \       ||                 ||       |\n"
                            "                      \_ _ _ ||_ _ _ _ _ _ _ _ _||_ _    |\n\n"),

                           ("                       _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n"
                            "                      / | '|| ' | ' | ' |       ||     |\n"
                            "              _ _ _ _/   o ||_ _ _ _ _ _ _ _ _ _||_ _ _|\n"
                            "             O       \     ||                   ||     |\n"
                            "                      \_ _ ||_ _ _ _ _ _ _ _ _ _||_ _  |\n\n"),

                           ("                       _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n"
                            "                      / ||| | ' | ' | ' |       ||   |\n"
                            "              _ _ _ _/ o ||_ _ _ _ _ _ _ _ _ _ _||_ _|\n"
                            "                     \   ||                     ||   |\n"
                            "             O        \_ ||_ _ _ _ _ _ _ _ _ _ _||_ _|\n\n"),

                           ("                       _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n"
                            "                      / | '|| ' | ' | ' |       ||     |\n"
                            "              _ _ _ _/-----||_ _ _ _ _ _ _ _ _ _||_ _ _|\n"
                            "                     \   o ||                   ||     |\n"
                            "                      \_ _ ||_ _ _ _ _ _ _ _ _ _||_ _  |\n\n"
                            "             O                                          \n"),

                           ("                       _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n"
                            "                      / | ' ||| | ' | ' |       ||       |\n"
                            "              _ _ _ _/       ||_ _ _ _ _ _ _ _ _||_ _ _ _|\n"
                            "                     \-------||                 ||       |\n"
                            "                      \_ _o_ ||_ _ _ _ _ _ _ _ _||_ _    |\n\n"
                            "                                                           \n"
                            "             O                                          \n"),

                           ("                       _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n"
                            "                      / | ' | '|| ' | ' |       ||         |\n"
                            "              _ _ _ _/         ||_ _ _ _ _ _ _ _||_ _ _ _ _|\n"
                            "                     \---------||               ||         |\n"
                            "                      \_ _ _o_ ||_ _ _ _ _ _ _ _||_ _      |\n\n"
                            "                                                            \n"
                            "                                                        \n"
                            "             O                                          \n"),

                           ("                       _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n"
                            "                      / | ' | '|| ' | ' |       ||         |\n"
                            "              _ _ _ _/         ||_ _ _ _ _ _ _ _||_ _ _ _ _|\n"
                            "                     \---------||               ||         |\n"
                            "                      \_ _ _o_ ||_ _ _ _ _ _ _ _||_ _      |\n\n"
                            "                                                            \n"
                            "                                                        \n"
                            "                                                        \n"
                            "             O                                          \n"),

                           ("                       _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n"
                            "                      / | ' | '|| ' | ' |       ||         |\n"
                            "              _ _ _ _/         ||_ _ _ _ _ _ _ _||_ _ _ _ _|\n"
                            "                     \---------||               ||         |\n"
                            "                      \_ _ _o_ ||_ _ _ _ _ _ _ _||_ _      |\n\n"
                            "                                                        \n"
                            "                                                        \n"
                            "                                                        \n"
                            "                                                        \n"
                            "             O                                          \n"),

                           ("                       _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n"
                            "                      / | ' | '|| ' | ' |       ||         |\n"
                            "              _ _ _ _/         ||_ _ _ _ _ _ _ _||_ _ _ _ _|\n"
                            "                     \---------||               ||         |\n"
                            "                      \_ _ _o_ ||_ _ _ _ _ _ _ _||_ _      |\n\n"
                            "                                                        \n"
                            "                                                        \n"
                            "                                                        \n"
                            "                                                        \n"
                            "                                                        \n"
                            "             O                                          \n"),

                           ("                       _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n"
                            "                      / | ' | '|| ' | ' |       ||         |\n"
                            "              _ _ _ _/         ||_ _ _ _ _ _ _ _||_ _ _ _ _|\n"
                            "                     \---------||               ||         |\n"
                            "                      \_ _ _o_ ||_ _ _ _ _ _ _ _||_ _      |\n\n")
                         ]
    
    intro_text = ("\"Where... Where am I? My head is pounding. What happened to me?\"\n\n"
                  "You wake up in a hospital bed, the sun is streaming through the window\nreflecting off the "
                  "clinical white of the room, hurting your eyes. You struggle\nto sit up in "
                  "the bed and take a look around, you seem to be the only inhabitant of the "
                  "room.\n\nThe other beds have been left unmade and cables and wires are left "
                  "dangling and curled up on the floor. Your strength seems to be returning "
                  "but your mind is\nstill hazy, you have no recollection of what happened or "
                  "how you ended up here.\n\nYou stand up and walk over to the window, outside "
                  "it is a beautiful day, the\nsun is shining down on the perfectly green "
                  "grass and there is not a cloud in\nthe azure sky. But then you notice "
                  "something - there is nothing else in the sky either. No planes, not even "
                  "birds. You lean in closer to the window and look\ndown to the ground. The "
                  "hospital car park is deserted apart from a few cars\nparked right up against the "
                  "building.\n\nThere are no people walking around, there are no sounds coming "
                  "from outside,\njust a heavy silence like a blanket over the world. "
                  "The window is locked. You\nturn around and notice for the first time a "
                  "message scrawled across the wall - \n\n\"Leave\".\n\nThat seems like a good idea.\n\n")
    
    for frame in intro_name:
        print(frame, end='')
        time.sleep(0.1)
        os.sys.stdout.flush()

    for frame in intro_static_syringe:
        print(frame, end='')
        time.sleep(0.1)
        os.sys.stdout.flush()

    for frame in intro_anim_syringe:
        os.system("cls" if os.name == "nt" else "clear")
        for name_frame in intro_name:
            print(name_frame, end='')
        print(frame, end='')
        time.sleep(0.1)
        os.sys.stdout.flush()

    input("                      Press enter to begin the game.\n")
    os.system("cls" if os.name == "nt" else "clear")
    for char in intro_text:
        print(char, end='')
        time.sleep(0.02)
        os.sys.stdout.flush()
    input("Press enter to continue.")
                                      

def list_of_items(items):
    """This function takes a list of items (see items.py for the definition) and
    returns a comma-separated list of item names (as a string). For example:

    >>> list_of_items([item_pen, item_handbook])
    'a pen, a student handbook'

    >>> list_of_items([item_id])
    'id card'

    >>> list_of_items([])
    ''

    >>> list_of_items([item_money, item_handbook, item_laptop])
    'money, a student handbook, laptop'

    """
    itemsString = ""
    for key in items:
        itemsString = itemsString + str(key["name"]) + ", "
    itemsString = itemsString[:-2]
    return(itemsString)


def print_inventory_items(items):
    """This function takes a list of inventory items and displays it nicely.
    The only difference is in formatting:
    print "You have ..." instead of "There is ... here.". For example:

    >>> print_inventory_items(inventory)
    You have id card, laptop, money.
    <BLANKLINE>

    """
    itemsString = list_of_items(items)
    if itemsString != "":
        print("You have " + itemsString + ".")
        print()


def print_room(room):
    """This function takes a room as an input and nicely displays its name
    and description. The room argument is a dictionary with entries "name",
    "description" etc. (see map.py for the definition). The name of the room
    is printed in all capitals and framed by blank lines. Then follows the
    description of the room and a blank line again. If there are any items
    in the room, the list of items is printed next followed by a blank line.
    For example:

    >>> print_room(rooms["Office"])
    <BLANKLINE>
    THE GENERAL OFFICE
    <BLANKLINE>
    You are standing next to the cashier's till at
    30-36 Newport Road. The cashier looks at you with hope
    in their eyes. If you go west you can return to the
    Queen's Buildings.
    <BLANKLINE>
    There is a pen here.
    <BLANKLINE>

    >>> print_room(rooms["Reception"])
    <BLANKLINE>
    RECEPTION
    <BLANKLINE>
    You are in a maze of twisty little passages, all alike.
    Next to you is the School of Computer Science and
    Informatics reception. The receptionist, Matt Strangis,
    seems to be playing an old school text-based adventure
    game on his computer. There are corridors leading to the
    south and east. The exit is to the west.
    <BLANKLINE>
    There is a pack of biscuits, a student handbook here.
    <BLANKLINE>

    >>> print_room(rooms["Robs"])
    <BLANKLINE>
    ROBS' ROOM
    <BLANKLINE>
    You are leaning agains the door of the systems managers'
    room. Inside you notice Rob Evans and Rob Davies. They
    ignore you. To the north is the reception.
    <BLANKLINE>

    Note: <BLANKLINE> here means that doctest should expect a blank line.
    """
    # Display room name
    print()
    print(room["name"].upper())
    print()
    # Display room description
    print(room["description"])
    print()


def exit_leads_to(exits, direction):
    """This function takes a dictionary of exits and a direction (a particular
    exit taken from this dictionary). It returns the name of the room into which
    this exit leads. For example:

    >>> exit_leads_to(rooms["Reception"]["exits"], "south")
    "Robs' room"
    >>> exit_leads_to(rooms["Reception"]["exits"], "east")
    "your personal tutor's office"
    >>> exit_leads_to(rooms["Tutor"]["exits"], "west")
    'Reception'
    """
    return rooms[exits[direction]]["name"]


def print_exit(direction, leads_to):
    """This function prints a line of a menu of exits. It takes a direction (the
    name of an exit) and the name of the room into which it leads (leads_to),
    and should print a menu line in the following format:

    GO <EXIT NAME UPPERCASE> to <where it leads>.

    For example:
    >>> print_exit("east", "you personal tutor's office")
    GO EAST to you personal tutor's office.
    >>> print_exit("south", "Robs' room")
    GO SOUTH to Robs' room.
    """
    print("GO " + direction.upper() + " to " + leads_to + ".")


def print_menu(exits, room_items, inv_items, room_npcs):
    """This function displays the menu of available actions to the player. The
    argument exits is a dictionary of exits as exemplified in map.py. The
    arguments room_items and inv_items are the items lying around in the room
    and carried by the player respectively. The menu should, for each exit,
    call the function print_exit() to print the information about each exit in
    the appropriate format. The room into which an exit leads is obtained
    using the function exit_leads_to(). Then, it should print a list of commands
    related to items: for each item in the room print

    "TAKE <ITEM ID> to take <item name>."

    and for each item in the inventory print

    "DROP <ITEM ID> to drop <item name>."

    For example, the menu of actions available at the Reception may look like this:

    You can:
    GO EAST to your personal tutor's office.
    GO WEST to the parking lot.
    GO SOUTH to Robs' room.
    TAKE BISCUITS to take a pack of biscuits.
    TAKE HANDBOOK to take a student handbook.
    DROP ID to drop your id card.
    DROP LAPTOP to drop your laptop.
    DROP MONEY to drop your money.
    What do you want to do?

    """
    print("You can:")
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))
    i = 0

    for key in room_items:
        if room_items[i]["type"] == "carryable":
            print("TAKE " + room_items[i]["id"].upper() + " to take " + room_items[i]["name"] + ".")
            i+= 1
    i = 0

    for key in room_items:
        print("EXAMINE " + room_items[i]["id"].upper())
        i += 1
    i = 0

    for key in inv_items:
        print("EXAMINE " + inv_items[i]["id"].upper())
        i += 1
    i = 0

    #Extra options added for examining and talking to npc's

    for key in room_npcs:
        print("EXAMINE the " + room_npcs[i]["id"].upper())
        i += 1
    i = 0

    for key in room_npcs:
        print("TALK to the " + room_npcs[i]["id"].upper())
        i += 1    

    print("What do you want to do?")


def is_valid_exit(exits, chosen_exit):
    """This function checks, given a dictionary "exits" (see map.py) and
    a players's choice "chosen_exit" whether the player has chosen a valid exit.
    It returns True if the exit is valid, and False otherwise. Assume that
    the name of the exit has been normalised by the function normalise_input().
    For example:

    >>> is_valid_exit(rooms["Reception"]["exits"], "south")
    True
    >>> is_valid_exit(rooms["Reception"]["exits"], "up")
    False
    >>> is_valid_exit(rooms["Parking"]["exits"], "west")
    False
    >>> is_valid_exit(rooms["Parking"]["exits"], "east")
    True
    """
    return chosen_exit in exits

#The check events function, explained in detail on the events.py file.
def check_events(passedValue):
    for key in player.current_room["events"]:
        #The string of the event found in map.py is ran as a function 
        eventFunction = globals()[key]
        eventFunction(passedValue)


def execute_go(direction):
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."
    """
    if is_valid_exit(player.current_room["exits"], direction) == True:
        room_id = ""+ player.current_room["exits"][direction] +""
        player.current_room = rooms[room_id]
        #check_events is now run after each command
        check_events(direction)
    else:
        print("You cannot go there.")
        input("Press enter to continue.")


def execute_take(item_id):
    """This function takes an item_id as an argument and moves this item from the
    list of items in the current room to the player's inventory. However, if
    there is no such item in the room, this function prints
    "You cannot take that."
    """
    listCopy = player.current_room["items"]
    item_changed = False
    for index in listCopy:
        if index["id"] == item_id:
            player.current_room["items"].remove(index)
            player.inventory.append(index)

            item_changed = True

    if item_changed == False:
        print("You cannot take that.")
        input("Press enter to continue.")

#New command - examine, prints the description of the item/npc chosen and then runs check_events 
def execute_examine(person_or_item):
    """
    """
    invListCopy = player.inventory
    roomListCopy = player.current_room["items"]
    npcListCopy = player.current_room["npc"]
    a = False
    for index in roomListCopy:
        if index["id"] == person_or_item:
            print("")
            print(index["description"])
            print()
            check_events(person_or_item)
            a = True

    for index in npcListCopy:
        if index["id"] == person_or_item:
            print("")
            print(index["description"])
            print()
            a = True

    for index in invListCopy:
        if index["id"] == person_or_item:
            print("")
            print(index["description"])
            print()
            check_events(person_or_item)
            a = True

    if a == False:
        print("Please enter something that is in the room or in your inventory.")
        
    input("Press enter to continue.") 

#New command - talk, prints a header with the npc name, and their greeting. Then runs check_events
def execute_talk(npc_chosen):
    """This function prints the greeting of the chosen npc. Should start an 
    event?
    """
    listCopy = player.current_room["npc"]
    item_changed = False
    for index in listCopy:
        if index["id"] == npc_chosen:
            print(index["name"])
            print("--------")
            print(index["greeting"])
            item_changed = True
            check_events(npc_chosen)
            input("Press enter to continue.")

    if item_changed == False:
        print("Please enter a person that is in the room.")
        input("Press enter to continue.")


def execute_command(command):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, or execute_drop, supplying the second word as the argument.

    """
    if len(command) != 0:
        if command[0] == "go":
            if len(command) > 1:
                execute_go(command[1])
            else:
                print("Go where?")
                input("Press enter to continue.")

        elif command[0] == "take":
            if len(command) > 1:
                execute_take(command[1])
            else:
                print("Take what?")
                input("Press enter to continue.")

        elif command[0] == "examine":
            if len(command) > 1:
                execute_examine(command[1])
            else:
                print("Examine what?")
                input("Press enter to continue.")

        elif command[0] == "talk":
            if len(command) > 1:
                execute_talk(command[1])
            else:
                print("Talk to who?")
                input("Press enter to continue.")

        elif command[0] == "give":
            if len(command) > 2:
                execute_give(command[1], command[2])
            elif len(command) > 1 and command[1] not in player.inventory:
                print("Give " + command[1] + " to who?")
                input("Press enter to continue.")
            else:
                print("Give what? and to who?")
                input("Press enter to continue.")
        elif command[0] == "restart":
            restart_program()

        else:
            print("This makes no sense.")
            input("Press enter to continue.")
    else:
        print("Please enter a command.")
        input("Press enter to continue.")


def menu(exits, room_items, inv_items, room_npcs):
    """This function, given a dictionary of possible exits from a room, and a list
    of items found in the room and carried by the player, prints the menu of
    actions using print_menu() function. It then prompts the player to type an
    action. The players's input is normalised using the normalise_input()
    function before being returned.

    """

    # Display menu
    print_menu(exits, room_items, inv_items, room_npcs)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


def move(exits, direction):
    """This function returns the room into which the player will move if, from a
    dictionary "exits" of avaiable exits, they choose to move towards the exit
    with the name given by "direction". For example:

    >>> move(rooms["Reception"]["exits"], "south") == rooms["Robs"]
    True
    >>> move(rooms["Reception"]["exits"], "east") == rooms["Tutor"]
    True
    >>> move(rooms["Reception"]["exits"], "west") == rooms["Office"]
    False
    """

    # Next room to go to
    return rooms[exits[direction]]


# This is the entry point of our program
def main():
    # Main game loop
    introRun = False

    while True:
        # Clears the console on both Windows & Unix systems
        os.system("mode con lines=75")
        os.system("cls" if os.name == "nt" else "clear")

        #Small check to decide whether the intro should run or not. Only triggers on first launch.
        if introRun == False:
            intro()
            introRun = True
        else:
            # Display game status (room description, inventory etc.)
            for room in floors[player.current_floor]:
                if player.current_room["id"] == room["id"]:
                    room["entered"] = True
            print_map(player.current_floor)
            print_room(player.current_room)
            print_inventory_items(player.inventory)
            check_events("")
            player.current_room["entered"] = "True"
            # Show the menu with possible actions and ask the player
            command = menu(player.current_room["exits"], player.current_room["items"], player.inventory, player.current_room["npc"])

            # Breaks out of the game loop, therefore quitting the game
            if len(command) == 1:
                if command[0] == "quit":
                    print("You have quit the game.")
                    break

            # Execute the player's command
            execute_command(command)

#Function which just restarts the program from the beginning.
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)



# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()