player = {"Name" : "Matt", "Health" : 100, "Mana" : 250, "Experience" : 0 }
Items = ["Phone","Wallet","Keys","Mage's Staff"]

#print("The player has: " + str(Inventory))
#print("Player stats: " + str(player))
Alive = True
if player["Health"] <= 0:
    Alive = False
    print("Player is Dead")
else:
    print ("Player is Alive")
Items.append ("Sword of Azeroth")
#print("The player has: " + str(Items))
def print_player(player):
    print("Player Stats:")
    for char in player:
        print(str(char) + " = " + str(player[char]))
print_player(player)

def Inventory():
    print("The player is holding")
    print(str(Items))
Inventory()