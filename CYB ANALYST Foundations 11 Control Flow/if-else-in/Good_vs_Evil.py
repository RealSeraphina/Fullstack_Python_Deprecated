# Declare 2 variables, hero and villain and set them equal to empty strings.
# Declare 2 more variables, hero_power_level and villain_power_level and set them equal to 0.
# If hero_power_level is higher than villain_power_level, print out "<HERO> defeats <VILLAIN> in battle!" *
# If hero_power_level is lower than villain_power_level, print out "<VILLAIN> defeats <HERO> in battle!" *
# If hero_power_level is the same as villain_power_level, print out "<HERO> and <VILLAIN> are evenly matched." *
# * use the variables and string concatenation to format your strings!

def main():
    hero = "Superman"
    villain = "Doomsday"
    hero_power_level = 9001
    villain_power_level = 9001
    if hero_power_level > villain_power_level:
        print(hero + " defeats " + villain + " in battle!")
    elif hero_power_level < villain_power_level:
        print(villain + " defeats " + hero + " in battle!")
    else:
        print(hero + " and " + villain + " are evenly matched.")

if __name__ == "__main__":
    main()
