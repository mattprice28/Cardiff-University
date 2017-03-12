#Importing required files and functions.
import os

from map import *
from game import normalise_input, restart_program
import player
from items import *
import items

#These events are essentially unique pieces of dialogue or other code which are triggered when the user enters commands.
#Each event is a function which is called from the 'check_events' function in the game.py file. Events accept a parameter
#which is passed from the function of whichever command is used. When the check_events function is run, it runs all events 
#in the room (Events for a room are stored within the room property file in map.py). The beginning of each function includes a 
# starting condition which is usually 'if paramater = specific value. 
#when the check_events function is running though each function it'll only run the main code of the ones which pass the starting
#condition. Typically, this will only be one event at a time.

#Event triggered when the player opens the cabinet in the second room.
def room1_cabinet(passedValue):
    if passedValue == "cabinet": 
    #the starting condition is 'cabinet' because the word passed after using the command 'examine cabinet' would be 'cabinet'
        if items.room1_cabinet_opened == False: 
        # The event branches out and gives differing dialogue depending on various conditions such as whether the room has been entered, or whether the user has a certain item. 
            print("Inside the cabinet there is a clutter of medical forms and equpiment.")
            print("You search around and find a key beneath a pile of old tissues.")
            print("The key is attached to a small tag which reads 'stairwell key' ")
            print("You pocket the key, as it will probably come in use.")
            player.inventory.append(item_key)
            print("--------------------------------------------------------------------------------")
            print("Key added to inventory!")
            items.room1_cabinet_opened = True
            while True:
                print("")
                print("You can:")
                print("CLOSE CABINET")
                print("SEARCH FURTHER")
                print("What do you want to do?")
                userInput = str(input("> ")).lower()
                userInput = userInput.strip()
                #The user can input commands during events. The normalisation is more limited during these events, however it still works on a basic level.
                if userInput == "close cabinet":
                    print("You close the cabinet and go on.")
                    return("")
                elif userInput == "search further":
                    print("You decide to look around the cabinet a little more, you find a newspaper")
                    print("dated October 3rd 2016.")
                    while True:
                        print("--------------------------------------------------------------------------------")
                        print("Would you like to read the newspaper?")
                        print("")
                        print("Yes / No")
                        userInput = str(input("> ")).lower()
                        userInput = userInput.strip()
                        if userInput == "yes":
                            print("Details surrounding the incident are still vague, symptoms include skin ")
                            print("lesions and uncontrollable coughing fits, all medical centres in the area")
                            print("have been converted into research stations. Desperately trying to find a cure,")
                            print("a spokesperson gave this statement earlier today.")
                            print("")
                            print("'We don't know what started it, we don't know how it spreads, all we know ")
                            print("is that if you are infected it's already too late, isolate yourself, your ")
                            print("sacrifice may be the only way to save humanity'.")
                            return
                        elif userInput == "no":
                            print("")
                            print("You decide to ignore the newspaper and close the cabinet.")
                            return("")
                            # When the event reaches the end of a branch, the function will return to the main game loop.
                            # On all commands besides the 'go' command, there will be an input asking the user to 'Press enter to continue' 
                            # as soon as the event returns to the main code. This input had to be included within the event for 'go' commands.
                        else:
                            print("That is not a valid command.")
                else:
                    print("")
                    print("That is not a valid command")
        else:
            print("Unfortunately, nothing has changed since the last time...")
            print("but the newspaper is still there.")
            while True:
                print("--------------------------------------------------------------------------------")
                print("Would you like to read the newspaper?")
                print("")
                print("Yes / No")
                userInput = str(input("> ")).lower()
                userInput = userInput.strip()
                if userInput == "yes":
                    print("Details surrounding the incident are still vague, symptoms include skin ")
                    print("lesions and uncontrollable coughing fits, all medical centres in the area")
                    print("have been converted into research stations. Desperately trying to find a cure,")
                    print("a spokesperson gave this statement earlier today.")
                    print("")
                    print("'We don't know what started it, we don't know how it spreads, all we know ")
                    print("is that if you are infected it's already too late, isolate yourself, your ")
                    print("sacrifice may be the only way to save humanity'.")
                    return
                elif userInput == "no":
                    print("")
                    print("You close the cabinet and continue.")
                    return("")
                else:
                    print("That is not a valid command.")
            print("You close the cabinet in dissapointment.")
            return("")
    else:
        return("")

#####DURING THE FIRST FEW EVENTS THE STRUCTURE IS A LITTLE MESSY, AS I WAS STILL WORKING OUT THE MOST EFFECTIVE METHOD OF WRITING EVENTS#####
#####TOWARDS THE BOTTOM OF THE PAGE, THE EVENTS BECOME MUCH TIDIER AS I LEARNT HOW TO CORRECTLY BRANCH OUT DIFFERENT OPTIONS.#####
#####EACH EVENT FOLLOWS THE SAME BASIC STRUCTURE, SO I WON'T COMMENT AS MUCH ON LATER EVENTS####


#Event triggered when the user attempts to travel to the stairs on the top floor.
def open_fourth_floor_stairs(passedValue):
    #This is an example of an event triggered by a 'go' command
    #The paramater passed is the direction which the user chose to go.
    #Because of the way that the go command changes the current room, and the check_events 
    #function runs all events within a room, for some events I stored the event within 
    #the room ahead and passed the direction that was used to get there as a paramater.
    if passedValue == "south":
        itemFound = False
        for key in player.inventory:
            if key["id"] == "key":
                itemFound = True
        if itemFound == True:
            if player.fourth_floor_stairs_checked == False:
                print("You try to open the door to the stairwell, but it's locked. Maybe that key")
                print("you found earlier will come in use...")
                player.fourth_floor_stairs_checked = True 
                # There are a few variables set in the player and item files which are used to save certain things, such as whether certain rooms have beem checked
                # or if npcs have been talked to. These can then be checked during events, to determine what piece of dialogue should be shown.
                while True:
                    print("--------------------------------------------------------------------------------")
                    print("Would you like to use the key on the door?")
                    print("")
                    print("Yes / No")
                    userInput = str(input("> ")).lower()
                    userInput = userInput.strip()
                    if userInput == "yes":
                        print("")
                        print("You slide the key into the lock and turn. To your relief, the door swings "
                              "open \nwith ease. You throw the key aside as you will no longer be needing it, and "
                              "\nwalk through the door.")
                        print("--------------------------------------------------------------------------------")
                        print("Key removed from inventory")
                        player.inventory.remove(item_key)
                        print("--------------------------------------------------------------------------------")
                        print("You walk down the stairs to the third floor.")
                        #When the user opens the door, the current floor is changed so that the user starts the next level
                        player.current_room = rooms["3rd Floor Corridor"]
                        player.current_floor = 1
                        print("As you head out into the third floor corridor you notice that the next set of "
                              "\nstairs are also locked. Another hunt begins!")
                        print("")
                        #example of the 'Press enter to continue' within the event for go commands.
                        input("Press enter to continue")
                        return
                    elif userInput == "no":
                        print("Although using the key seems like a really good idea, you decide not to.")
                        #when the user does not have the key, or decides not to use it, the current room is changed back to where the user came from
                        #This is because the event triggers with a 'ghost room'. In this situation, it's the stairs.
                        #If the current room was not change, the user would move into a room with the description.
                        player.current_room = rooms["4th Floor Corridor"]
                        print("")
                        input("Press enter to continue.")
                        return
                    else:
                        print("")
                        print("That is not a valid command.")

            elif player.fourth_floor_stairs_checked == True:
                print("")
                print("You come back to the stairwell with the key in hand, ready to escape!")
                while True:
                    print("--------------------------------------------------------------------------------")
                    print("Would you like to use the key on the door?")
                    print("")
                    print("Yes / No")
                    userInput = str(input("> ")).lower()
                    userInput = userInput.strip()
                    if userInput == "yes":
                        print("")
                        print("You slide the key into the lock and turn. To your relief, the door swings "
                              "open with ease. You throw the key aside as you will no longer be needing it, "
                              "and walk through the door.")
                        print("--------------------------------------------------------------------------------")
                        print("Key removed from inventory!")
                        player.inventory.remove(item_key)
                        print("--------------------------------------------------------------------------------")
                        print("You walk down the stairs to the third floor.")
                        player.current_room = rooms["3rd Floor Corridor"]
                        player.current_floor = 1
                        print("As you head out into the third floor corridor you notice that the next set of "
                              "stairs are also locked. Another hunt begins!")
                        print("")
                        input("Press enter to continue.")
                        return
                    elif userInput == "no":
                        print("Although using the key seems like a really good idea, you decide not to.")
                        player.current_room = rooms["4th Floor Corridor"]
                        print("")
                        input("Press enter to continue.")
                        return
                    else:
                        print("")
                        print("That is not a valid command.")
        if itemFound == False:
            if player.fourth_floor_stairs_checked == False:
                print("You try to open the door to the stairwell, but it's locked. You need to get")
                print("out of this place and those stairs are your only option. Better get looking")
                print("for a key!")
                player.fourth_floor_stairs_checked = True
                player.current_room = rooms["4th Floor Corridor"]
                print("")
                input("Press enter to continue.")
            elif player.fourth_floor_stairs_checked == True:
                print("You come back to the stairwell but it is still locked. How strange.")
                player.current_room = rooms["4th Floor Corridor"]
                print("")
                input("Press enter to continue.")   
    else:
        player.current_room = rooms["4th Floor Corridor"]

#Event triggered when the user examines the shelf in the third floor storage room.
def check_shelf_3rd_floor_supply(passedValue):
    if passedValue == "shelf":
        if items.shelf_checked == False:
            print("You find a screwdriver.")
            player.inventory.append(item_screwdriver)
            print("--------------------------------------------------------------------------------")
            print("Screwdriver added to inventory!")
            items.shelf_checked = True
        else:
            #We tried to add lots of dialogue changes depending on whether the user has taken items or not. 
            print("Just a dusty shelf.")
            return("")
    else:
        return("")

#Event triggered when the user examines the vent on the third floor
def examine_vent(passedValue):
    if passedValue == "vent":
        itemFound = False
        for key in player.inventory:
            if key["id"] == "screwdriver":
                itemFound = True
        if itemFound == True:
            if player.vent_opened == False:
                print("The vent is secured with 4 screws. The screwdriver you found earlier will come \nin use...")
                print("--------------------------------------------------------------------------------")
                print("Would you like to use the screwdriver on the vent?")
                print("")
                print("Yes / No")
                userInput = str(input("> ")).lower()
                userInput = userInput.strip()
                if userInput == "yes":
                    player.vent_opened = True
                    print("You undo the screws on the vent, and it drops to the floor")
                    print("")
                    print("--------------------------------------------------------------------------------")
                    print("You find an id card inside the vent.")
                    player.inventory.append(item_id)
                elif userInput == "no":
                    print("Although using the screwdriver seems like a really good idea, you decide not to.")
                else:
                    print("That is not a valid command.")
            elif player.vent_opened == True:
                print("You are tempted to crawl through the vent to see where it goes. However")
                print("you decide it's probably not a good idea.")

        if itemFound == False:
            if player.vent_opened == False:
                print("You peer through the vent and notice a white card inside.")
                print("--------------------------------------------------------------------------------")
                print("Would you like to try and force the vent open?")
                print("")
                print("Yes / No")
                userInput = str(input("> ")).lower()
                userInput = userInput.strip()
                if userInput == "yes":
                    print("You yank on the corner of the vent but it doesn't budge. You decide to come")
                    print("back later when you have something to open the vent with.")

                elif userInput == "no":
                    print("You decide to come back later when you have something to open the vent with.")
                else:
                    print("That is not a valid command.")

    else:
        return("")

#event triggered when the user examines the medical cabinet on the ground floor
# This is quite an interesting event, as it is for the medical cabinet minigame.
# It is essentially a little puzzle program which runs within the event.
def ground_floor_numbers_minigame(passedValue):
    if passedValue == "medicabinet":
        if player.medicabinet_unlocked == True:
            print("The cabinet is still open, and nothing new has appeared. You decide to turn back..")
            return 
        print("Upon closer inspection you see that the cabinet has a small screen and "
              "some buttons.")
        while True:
            print("--------------------------------------------------------------------------------")
            print("Do you want to try and open the medical cabinet?")
            print("")
            print("Yes / No")
            userInput = str(input("> ")).lower()
            userInput = userInput.strip()
            if userInput == "yes":
                print("")  
                a=3
                b=4
                c=3
                
                options = ['1','2','3','reset','cancel']

                #Explaining how to beat the puzzle
                print()
                print("There are 3 numbers on the screen infront of you: 3 4 3")
                print("A message reads 'Make all numbers equal to 3'")
                print("Each button will increase its own number by 1")
                print("While also decreasing all adjacent numbers by 1")

                while player.medicabinet_unlocked==False:
                    if a==3 and b==3 and c==3:
                        player.medicabinet_unlocked=True
                        #The check for whether the play has beaten the game happens at the top, at the beginning of the loop
                        print("The lock clicks and the cabinet swings open!")
                        print("")
                        print("The inside of the cabinet has nearly been emptied, but you see a bottle of "
                              "medicine lying on it's side on the top shelf. The medicine could come "
                              "in handy, so you take it.")
                        print("--------------------------------------------------------------------------------")
                        print("Medicine added to inventory!")
                        player.inventory.append(item_medicine)
                        print("")  
                        return("")
                    else:
                        print()
                        print(a, b, c)
                        print()
                        print("There are five buttons: 1, 2, 3, reset and cancel")
                        print()
                        userInput = str(input("Please choose a button :"))
                        userInput = userInput.lower()
                        userInput = userInput.strip()
                        # Depending on what button the user presses (or types in) the three numbers have an effect.
                        # Having little puzzles like this keep thing interesting.
                        print()
                        if userInput not in options:
                            print()
                            print("Please choose a valid button")
                            print()
                        elif userInput == '1':
                            a = a + 1
                            b = b - 1
                        elif userInput == '2':
                            a = a - 1
                            b = b + 1
                            c = c - 1
                        elif userInput == '3':
                            b = b - 1
                            c = c + 1   
                        elif userInput == 'reset':
                            a=3
                            b=4
                            c=3
                        elif userInput == 'cancel':
                            print("You give up on the lock, and leave the cabinet.")
                            return        
            elif userInput == "no":
                print("You decide against trying to open the medical cabinet. Maybe you can come back later.")
                return
            else:
                print("")
                print("That is not a valid command.")
         
    else:
        return("")

#event triggered when the user talks to the patient on the ground floor
#This event includes multiple choice conversation. Although the general outcome is more
#or less the same every time, the dialogue can be different, which adds more depth to the game.
def npc_patient_convo(passedValue):
    if passedValue == "patient":
        while player.patient_talk == False:
            print("Hello! Hello? Could you tell me what's going on?")
            print("")
            print("1. I don't really know.. some sort of virus outbreak.")
            print("2. You don't look like a fit state, can I help?")
            print("3. You look horrific.")
            userInput = str(input("1, 2 or 3 > ")).lower()
            userInput = userInput.strip()
            if userInput == "1":
                print("")
                print("Patient")
                print("--------")
                print("Oh god, that's horrible.. How did this all happen!?")
                while True:
                    print("")
                    print("1. Is there anything I can help with?")
                    print("2. You look horrible.")
                    userInput = str(input("1 or 2 > ")).lower()
                    userInput = userInput.strip()
                    if userInput == "1":
                        print("Patient")
                        print("--------")
                        print("Actually yes, I need my medication but when everything went crazy all the Doctors "
                              "left and my medication is still locked in my room. Could you retrieve it for me? "
                              "I will give you this keycard I found earlier, I'm not too sure what door it opens.")
                        player.patient_talk = True
                        print("--------------------------------------------------------------------------------")
                        if player.medicabinet_unlocked == True:
                            give_patient_medicine()
                            player.patient_talk2 = True
                            return
                        else:    
                            print("You step away from the patient. Better find that medicine.")
                            return
                    elif userInput == "2":
                        print("")
                        print("Patient")
                        print("--------")
                        print("That wasn't very nice! Could I change your opinion with this keycard I found? "
                              "If you find my medication I'll give it to you. It's locked in a cabinet in my room.")
                        player.patient_talk = True
                        print("--------------------------------------------------------------------------------")
                        if player.medicabinet_unlocked == True:
                            give_patient_medicine()
                            player.patient_talk2 = True
                            return
                        else:    
                            print("You step away from the patient. Better find that medicine.")
                            return
                    else:
                        print("")
                        print("That is not a valid command.")
            elif userInput == "2":
                print("")
                print("Patient")
                print("--------")
                print("Actually yes, I need my medication but when everything went crazy all the Doctors "
                      "left and my medication is still locked in my room. Could you retrieve it for me? "
                      "I will give you this keycard I found earlier, I'm not too sure what door it opens.")
                patient_talk = True
                print("--------------------------------------------------------------------------------")
                if player.medicabinet_unlocked == True:
                    give_patient_medicine()
                    player.patient_talk2 = True
                    return
                else:
                    print("You step away from the patient. Better find that medicine.")
                    return
            elif userInput == "3":
                print("")
                print("Patient")
                print("--------")
                print("That wasn't very nice! Could I change your opinion with this keycard I found? "
                      "If you find my medication I'll give it to you. It's locked in a cabinet in my room.")
                player.patient_talk = True
                print("--------------------------------------------------------------------------------")
                if player.medicabinet_unlocked == True:
                    print("You found some medicine earlier, do you want to give it to him?")
                    give_patient_medicine()
                    player.patient_talk2 = True
                    return
                else:    
                    print("You step away from the patient. Better find that medicine.")
                    return
            else:
                print("")
                print("That is not a valid command.")
        while player.patient_talk == True:
            if player.patient_talk2 == False:
                print("")
                print("Patient")
                print("--------")
                print("I really need that medication. It is still locked in my room. Could you retrieve it for me?"
                      "I will give you this keycard I found earlier, I'm not too sure what door it opens.")
                print("--------------------------------------------------------------------------------")
                if player.medicabinet_unlocked == True:
                    give_patient_medicine()
                    player.patient_talk2 = True
                    return
                else:
                    print("You step away from the patient. Better find that medicine.")
                    return
            else:
                print("")
                print("Patient")
                print("--------")
                print("Thankyou for finding my medication I'm feeling much better now.")
                return


    else:
        return

#this is essentially a further extension of the last function, just to avoid text duplication.
def give_patient_medicine():
    print("You found some medicine earlier, do you want to give it to him?")
    while True:
        print("")
        print("Yes / No")
        userInput = str(input("> ")).lower()
        userInput = userInput.strip()
        if userInput == "yes":
            print("")
            print("You give the patient his medicine. He screams in happiness and")
            print("scuttles away, leaving the key card on the floor.")
            print("--------------------------------------------------------------------------------")
            print("Medicine removed from inventory!")
            print("Key card added to inventory!")
            print("--------------------------------------------------------------------------------")
            print("")
            player.inventory.remove(item_medicine)
            player.inventory.append(item_keycard)
            return
        elif userInput == "no":
            print("Stop trying to be awkward, just give him the medicine.")
            print("")
            print("You give the patient his medicine. He screams in happiness and")
            print("scuttles away, leaving the key card on the way.")
            print("--------------------------------------------------------------------------------")
            print("Medicine removed from inventory!")
            print("Key card added to inventory!")
            print("--------------------------------------------------------------------------------")
            print("")
            player.inventory.remove(item_medicine)
            player.inventory.append(item_keycard)
            return
        else:
            print("That is not a valid command.")  

#triggered when the user talks to the doctor on the third floor
def doctor_talk(passedValue):
    if passedValue == "doctor":
        itemFound = False
        for key in player.inventory:
            if key["id"] == "id":
                itemFound = True
        if itemFound == True:
            if player.doctor_talk2 == False:
                while True:
                    print("You read the name on his scrubs and you realise the id you found earlier")
                    print("belongs to the doctor. You show it to him.")
                    print('"Oh! you found my id"')
                    player.doctor_talk2 = True
                    print("--------------------------------------------------------------------------------")
                    print("Would you like to give the id to the doctor?")
                    print("")
                    print("Yes / No")
                    userInput = str(input("> ")).lower()
                    userInput = userInput.strip()
                    if userInput == "yes":
                        print("")
                        print("Thank you! I have been looking everywhere for this. Here have this")
                        print("key as a reward")
                        player.doctor_talk = True
                        print("--------------------------------------------------------------------------------")
                        print("Id removed from inventory")
                        player.inventory.remove(item_id)
                        print("Key added to inventory")
                        player.inventory.append(item_key)
                        print("--------------------------------------------------------------------------------")
                        print()
                        return
                    elif userInput == "no":
                        print()
                        print('"Wait, I will give you this key as a reward!"')
                        print("You decide to give the Id to the doctor and recieve a key. Maybe it will open the door to the stairs?")
                        print("--------------------------------------------------------------------------------")
                        print("Id removed from inventory")
                        player.inventory.remove(item_id)
                        print("Key added to inventory")
                        player.inventory.append(item_key)
                        return
                    else:
                        print("That is not a valid command.")
            itemFound2 = False
            for key in player.inventory:
                if key["id"] == "key":
                    itemFound2 = True
            if player.doctor_talk2 == True and itemFound2 == True:
                print("")
                print('"You should use the key I gave you to escape. It is not safe here."')
        if itemFound == False:
            if player.doctor_talk == False:
                print("Who are you?! What are you doing here? All patients were evacuated 3 days ago.")
                print("Nevermind, no time for introductions, perhaps you can be of use to me")
                print("I have lost my ID card somewhere on this floor, could you find it?")
                player.doctor_talk = True
                print("")
            elif player.doctor_talk == True:
                print("Oh, it's you again.")
                print("")
    else:
        return()

#triggered when the user attempts to enter the stairs on the third floor
#This is more or less a direct copy of the fourth floor stairs event.
def open_third_floor_stairs(passedValue):
    if passedValue == "south":
        itemFound = False
        for key in player.inventory:
            if key["id"] == "key":
                itemFound = True
        if itemFound == True:
            if player.third_floor_stairs_checked == False:
                print("You try to open the door to the stairwell, but it's locked. Maybe that key")
                print("you got off the doctor will come in use...")
                player.third_floor_stairs_checked = True
                while True:
                    print("--------------------------------------------------------------------------------")
                    print("Would you like to use the key on the door?")
                    print("")
                    print("Yes / No")
                    userInput = str(input("> ")).lower()
                    userInput = userInput.strip()
                    if userInput == "yes":
                        print("")
                        print("You slide the key into the lock and turn. To your relief, the door swings "
                              "open \nwith ease. You throw the key aside as you will no longer be needing it, and "
                              "\nwalk through the door.")
                        print("--------------------------------------------------------------------------------")
                        print("Key removed from inventory")
                        player.inventory.remove(item_key)

                        os.system("cls" if os.name == "nt" else "clear")
                        print("--------------------------------------------------------------------------------")
                        print("-----------------------------------NOTICE---------------------------------------")
                        print("DUE TO TIME CONSTRAINTS WE WERE UNABLE TO IMPLEMENT THE SECOND AND FIRST FLOORS ")
                        print("--------------------------------------------------------------------------------")
                        print("----------------THE GAME WILL CONTINUE FROM THE GROUND FLOOR--------------------")
                        print("--------------------------------------------------------------------------------")
                        player.current_room = rooms["Ground Floor North Corridor"]
                        player.current_floor = 2
                        print("")
                        input("Press enter to continue")
                        return
                    elif userInput == "no":
                        print("Although using the key seems like a really good idea, you decide not to.")
                        player.current_room = rooms["3rd Floor Corridor"]
                        print("")
                        input("Press enter to continue.")
                        return
                    else:
                        print("")
                        print("That is not a valid command.")

            elif player.third_floor_stairs_checked == True:
                print("")
                print("You come back to the stairwell with the key in hand, ready to escape!")
                while True:
                    print("--------------------------------------------------------------------------------")
                    print("Would you like to use the key on the door?")
                    print("")
                    print("Yes / No")
                    userInput = str(input("> ")).lower()
                    userInput = userInput.strip()
                    if userInput == "yes":
                        print("")
                        print("You slide the key into the lock and turn. To your relief, the door swings "
                              "open with ease. You throw the key aside as you will no longer be needing it, "
                              "and walk through the door.")
                        print("--------------------------------------------------------------------------------")
                        print("Key removed from inventory!")
                        player.inventory.remove(item_key)
                        print("--------------------------------------------------------------------------------")
                        print("-----------------------------------NOTICE---------------------------------------")
                        print("DUE TO TIME CONSTRAINTS WE WERE UNABLE TO IMPLEMENT THE SECOND AND FIRST FLOORS ")
                        print("--------------------------------------------------------------------------------")
                        print("----------------THE GAME WILL CONTINUE FROM THE GROUND FLOOR--------------------")
                        print("--------------------------------------------------------------------------------")
                        player.current_room = rooms["Ground Floor North Corridor"]
                        player.current_floor = 2
                        print("")
                        input("Press enter to continue.")
                        return
                    elif userInput == "no":
                        print("Although using the key seems like a really good idea, you decide not to.")
                        player.current_room = rooms["3rd Floor Corridor"]
                        print("")
                        input("Press enter to continue.")
                        return
                    else:
                        print("")
                        print("That is not a valid command.")
        if itemFound == False:
            if player.third_floor_stairs_checked == False:
                print("You try to open the door to the stairwell, but it's locked. You need to get")
                print("out of this place and those stairs are your only option. Better get looking")
                print("for a key!")
                player.third_floor_stairs_checked = True
                player.current_room = rooms["3rd Floor Corridor"]
                print("")
                input("Press enter to continue.")
            elif player.third_floor_stairs_checked == True:
                print("You come back to the stairwell but it is still locked. How strange.")
                player.current_room = rooms["3rd Floor Corridor"]
                print("")
                input("Press enter to continue.")   
    else:
        player.current_room = rooms["3rd Floor Corridor"]

#event triggered when the user checks the shelf on the third floor
def check_shelf_3rd_floor_supply(passedValue):
    if passedValue == "shelf":
        if items.shelf_checked == False:
            print("You find a screwdriver.")
            player.inventory.append(item_screwdriver)
            print("--------------------------------------------------------------------------------")
            print("Screwdriver added to inventory!")
            items.shelf_checked = True
        else:
            print("Just a dusty shelf.")
            return("")
    else:
        return("")


#triggered when the user attempts to enter the staff room on the ground floor
#Another locked room event which requires the user input within the event.
def open_staff_room(passedValue):
    if passedValue == "south":
        if player.staff_room_door_open == False:
            print("You try opening the door, but it is locked.")
            print("By the side of the door there is a slot for a keycard.")
            itemFound = False
            for key in player.inventory:
                if key["id"] == "keycard":
                    itemFound = True
            if itemFound == True:
                print("--------------------------------------------------------------------------------")
                while True:
                    print("The patient you found earlier gave you a key card,")
                    print("would you like to try it?")
                    print("")
                    print("Yes / No")
                    userInput = str(input("> ")).lower()
                    userInput = userInput.strip()
                    if userInput == "yes":
                        print("You insert the card into the reader and a little light flashes.")
                        print("You hear a click, and the door unlocks.")
                        player.staff_room_door_open = True
                        print("--------------------------------------------------------------------------------")
                        print("Key card removed from inventory!")
                        player.inventory.remove(item_keycard)
                        print("")
                        input("Press enter to continue.")
                        return
                    elif userInput == "no":
                        print("You decide not to try the keycard..")
                        print("")
                        player.current_room = rooms["Patient room 0C"]
                        input("Press enter to continue.")
                        return
                    else:
                        print("That is not a valid command.")
            elif itemFound == False:
                if player.patient_talk == False:
                    print("You should probably try and find the keycard..")
                    print("")
                    player.current_room = rooms["Patient room 0C"]
                    input("Press enter to continue.")
                    return
                elif player.patient_talk == True:
                    print("The patient in the other room mentioned a keycard..")
                    print("")
                    player.current_room = rooms["Patient room 0C"]
                    input("Press enter to continue.")
                    return
        else:
            return
    else:
        return

#triggered when the user talks to the researcher on the ground floor
def npc_researcher_convo(passedValue):
    if passedValue == "researcher":
        if player.researcher_talk == False:
            player.researcher_talk = True
            print("Ah, you're the myserious patient who just woke up? You looking to get out?")
            print("We all want to get out but the entire place is on security lockdown ever")
            print("since the accident in the lab. The only way out is through")
            print("the door in the Main Reception but that's locked to ensure nothing can")
            print("get in; or out. The only way out is to reset the alarm system ")
            print("in the lab, if you can solve this riddle you may be able to get out of ")
            print("this place.")
            print("--------------------------------------------------------------------------------")
            print("The researcher hands you a piece of paper with a riddle on it...")
            print("Riddle added to inventory!")
            player.inventory.append(item_riddle)
            print("--------------------------------------------------------------------------------")
        elif player.researcher_talk == True:
            print("Why are you still talking to me?")
            print("I gave you the riddle, now bugger off.")
            print("")
            return
    else:
        return

#triggered when the user examines the tray on the ground floor
def examine_tray(passedValue):
    if passedValue == "tray":
        if items.tray_checked == False:
            items.tray_checked = True
            print("You peer into the tray and see a small scalpel.")
            print("You figure it could come in handy, so you take it.")
            print("--------------------------------------------------------------------------------")
            print("Scalpel added to inventory!")
            player.inventory.append(item_scalpel)
            print("--------------------------------------------------------------------------------")
        elif items.tray_checked == True:
            print("Other than the scalpel, there are no more items of interest.")

#triggered when the user talks to the receptionist on the ground floor
def npc_receptionist_convo(passedValue):
    if passedValue == "receptionist":
        while True:
            if player.researcher_talk == True and player.toilet_key_got == False:
                print("")
                print("1. To get to the lab.. I think?")
                userInput = str(input("Just say 1 > ")).lower()
                userInput = userInput.strip()
                if userInput != "1":
                    print("That is not a valid command.") 
                elif userInput == "1":
                    print("")
                    print("You need to get to the lab? Well the only way in now is through the toilets ")
                    print("and I have the key. But first I need to know I can trust you, can you answer") 
                    print("some questions.")
                    print("")
                    print("How did you get here?")
                    print("")
                    while True:
                        print("1. Why does that matter? Just give me the key")
                        print("2. I don't know, I just woke up in a room on the top floor.")
                        print("3. Everything is locked, how do you think I got in?")
                        print("")
                        userInput = str(input("1, 2 or 3 > ")).lower()
                        userInput = userInput.strip()
                        if userInput == "1" or userInput == "3":
                            print("")
                            print("Please just answer the question, how did you get here?")
                        elif userInput != "1" and userInput != "2" and userInput != "3":
                            print("That is not a valid command.")
                        elif userInput == "2":
                            print("")
                            print("Ok that is what I expected, next question.")
                            print("How long have you been here?")
                            print("")
                            while True:
                                print("1. It feels like it's been hours since I woke up, but I think I was here before that, wasn't I?")
                                print("2. Look I just want to get out of here, can I just have the key?")
                                print("3. You are the receptionist, you tell me!")
                                print("")
                                userInput = str(input("1, 2 or 3 > ")).lower()
                                userInput = userInput.strip()
                                if userInput == "2" or userInput == "3":
                                    print("")
                                    print("Please, it's important you answer my questions, how long have you been here?")
                                elif userInput != "1" and userInput != "2" and userInput != "3":
                                    print("That is not a valid command.")
                                elif userInput == "1":
                                    print("")
                                    print("Good that checks out, last question.")
                                    print("What do you remember from before?")#
                                    print("")
                                    while True:
                                        print("1. The more I try and think about before, the more the memories slip away.")
                                        print("2. I've had enough of your games just give me the key!")
                                        print("3. Why is this so important, what happened here?")
                                        print("")
                                        userInput = str(input("1, 2 or 3 > ")).lower()
                                        userInput = userInput.strip()
                                        if userInput == "2" or userInput == "3":
                                            print("")
                                            print("Please stay calm, just answer the question and I will give you the key")
                                        elif userInput != "1" and userInput != "2" and userInput != "3":
                                            print("That is not a valid command.")
                                        elif userInput == "1":
                                            print("Thank you for answering the questions, you may not understand the need for them")
                                            print("straight away, but you will, eventually. Anyway here is the key.")
                                            print("--------------------------------------------------------------------------------")
                                            print("Toilet key added to inventory!")
                                            player.inventory.append(item_key)
                                            player.toilet_key_got = True
                                            return
            elif player.toilet_key_got == True:
                print("You've got the key, now get out of this place!")
                return
            else:
                print("1. I have no idea..")
                print("2. To get anywhere that's not here!")
                userInput = str(input("1 or 2 > ")).lower()
                userInput = userInput.strip()
                if userInput == "1":
                    print("")
                    print("Well what are you doing bothering me then?")
                    print("I'll cut you some slack, cause you look like you're having")
                    print("a bad day. The researcher in the staff room seems to know")
                    print("how to get out of this place.. Come back to me when you find")
                    print("out.")
                    return
                elif userInput == "2":
                    print("")
                    print("Me too.. Come back to me when you find out.")
                    return
                else:
                    print("That is not a valid command.")

#triggered when the user attempts to enter the toilets on the ground floor
def open_toilets(passedValue):
    if passedValue == "west":
        if player.toilet_door_open == False:
            print("You try opening the door, but it is locked.")
            itemFound = False
            for key in player.inventory:
                if key["id"] == "key":
                    itemFound = True
            if itemFound == True:
                print("--------------------------------------------------------------------------------")
                while True:
                    print("The receptionist gave you a key to this room,")
                    print("would you like to use it?")
                    print("")
                    print("Yes / No")
                    userInput = str(input("> ")).lower()
                    userInput = userInput.strip()
                    if userInput == "yes":
                        print("You insert the key into the lock and open the door.")
                        print("The door swings open and you walk into the bathroom.")
                        player.toilet_door_open = True
                        print("--------------------------------------------------------------------------------")
                        print("Key removed from inventory!")
                        player.inventory.remove(item_key)
                        print("")
                        input("Press enter to continue.")
                        return
                    elif userInput == "no":
                        print("You decide not to use the key")
                        print("")
                        player.current_room = rooms["Main Reception"]
                        input("Press enter to continue.")
                        return
                    else:
                        print("That is not a valid command.")
            elif itemFound == False:
                print("You should probably try and find the key..")
                print("")
                player.current_room = rooms["Main Reception"]
                input("Press enter to continue.")
                return
        else:

            return
    else:

        return

#triggered when the user examines the alarm on the ground floor.
#finishing this event causes the game to end.
#Depending on which choice the user makes, they are given a different piece of end text.
def examine_alarm(passedValue):
    if passedValue == "alarm":
        print("You approach the wirey mess with caution. It fizzles a little.")
        print("Inside the box there are four wires in a parallel alignment")
        itemFound = False
        for key in player.inventory:
           if key["id"] == "riddle":
               itemFound = True
        if itemFound == False:
            print("")
            print("You decide to back away, as this looks dangerous.")
            print("Maybe you should come back later when you have some help.")
        else:
            print("The riddle which the researcher gave you might come in handy here.")
            print("--------------------------------------------------------------------------------")
            print("One wire leads to salvation")
            print("One wire seals you in")
            print("One wire gives you a shock")
            print("The last doesn't do anything")
            print("The open and close are neighbours")
            print("So are the blank and the zing")
            print("The exit is close to the centre")
            print("To the left of the one with nothing")
            print("--------------------------------------------------------------------------------")
            print("It seems like you need to choose one of the wires to cut.")
            itemFound = False
            for key in player.inventory:
                if key["id"] == "scalpel":
                    itemFound = True
            if itemFound == False:
                print("But you don't have anything to cut it with...")
                print("Better go and find something.")
                return
            else:
                print("")
                print("You raise your scalpel ready to cut, everything depends on this.")
                print("Don't make the wrong decision.")
                while True:
                    userInput = str(input("1,2,3,4,see riddle,back > ")).lower()
                    userInput = userInput.strip()
                    if userInput == "1":
                        print("")
                        print("Suddenly a siren rings and you hear a voice over speakers.")
                        print("")
                        print("'INITIAING PERMANENT LOCKDOWN'")
                        print("")
                        print("Looks like you chose wrong...")
                        print("You'll never get out of this place.")
                        print("--------------------------------------------------------------------------------")
                        input("GAME OVER - PRESS ENTER TO RESTART")
                        restart_program()
                    elif userInput == "2":
                        print("")
                        print("Suddenly a siren rings and you hear a voice over speakers.")
                        print("")
                        print("'MAIN ENTRANCE OPENING'")
                        print("")
                        print("Looks like you chose right...")
                        print("You can finally escape this place.")
                        print("What you find may not please you.")
                        print("--------------------------------------------------------------------------------")
                        input("GAME WON - PRESS ENTER TO RESTART")
                        restart_program()
                    elif userInput == "3":
                        print("")
                        print("...")
                        print("")
                        print("Nothing happened.")
                        print("")
                        print("Looks like you chose wrong, however you are now able to work")
                        print("out the correct answer with ease.")
                        print("You can finally escape this place.")
                        print("What you find may not please you.")
                        print("--------------------------------------------------------------------------------")
                        input("GAME WON (sort of) - PRESS ENTER TO RESTART")
                        restart_program()
                    elif userInput == "4":
                        print("")
                        print("ZAP")
                        print("")
                        print("The wire let off a powerful shock which killed you.")
                        print("")
                        print("How unfortunate.")
                        print("--------------------------------------------------------------------------------")
                        input("GAME OVER - PRESS ENTER TO RESTART")
                        restart_program()
                    elif userInput == "see riddle":
                        print("--------------------------------------------------------------------------------")
                        print("One wire leads to salvation")
                        print("One wire seals you in")
                        print("One wire gives you a shock")
                        print("The last doesn't do anything")
                        print("The open and close are neighbours")
                        print("So are the blank and the zing")
                        print("The exit is close to the centre")
                        print("To the left of the one with nothing")
                        print("--------------------------------------------------------------------------------")  
                    elif userInput == "back":
                        print("")
                        print("The pressure gets to you and you decide to stop")
                        return

#triggered when the user tries to exit the building on the ground floor
def leave(passedValue):
    if passedValue == "south":
        print("You try to leave through the exit, but the door is locked shut.")
        print("There must be some way of unlocking this door.")
        player.current_room = rooms["Main Reception"]
        input("Press enter to continue.")







