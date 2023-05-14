# Declare a variable dino and set it to an empty string and declare a variable chance and set it equal to 0.
# If the value for dino is set to "Brachiosaurus", then set chance to 90.
# If the value for dino is set to "Triceratops", then set chance to 65.
# If the value for dino is set to "Velociraptor", then set chance to 10.
# If the value for dino is set to "Tyrannosaurus", then set chance to 0.
# Finally, print out the string "Your chance of surviving a <DINO> attack is <CHANCE>%" using the dino and chance variables and string concatenation.

def main():
    dino = "Velociraptor"
    chance = 0
    if dino == "Brachiosaurus":
        chance = 90
    elif dino == "Triceratops":
        chance = 65
    elif dino == "Velociraptor":
        chance = 10
    elif dino == "Tyrannosaurus":
        chance = 0
    print("Your chance of surviving a " + dino + " attack is " + str(chance) + "%")

if __name__ == "__main__":
    main()
