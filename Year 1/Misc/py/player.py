fighter={}
fighter["name"] = "Jin"
fighter["health"] = "100"
fighter["energy"] = "80"
fighter["experience"] = "70"
fighter["alive"] = True
fighter["inventory"] = ["Sword","Shield","Water","Food"]
fighter["inventory"].append("Sword of Azeroth")
for char in fighter():
	print("health is:"),print(fighter["health"])
	print("name is:"),print(fighter["name"])
	print("energy is"),print(fighter["energy"])
	print("experience is:"),print(fighter["experience"])
	print("Is he alive ?"),print(fighter["alive"])
	print("The items he has in his possession are :"),print(fighter["inventory"])


