# Declare a variable character and set its value to be an empty string.
# If the value for character is "Harry", then print out "Expecto Patronum".
# If the value for character is "Hermione", then print out "It's LeviOsa".
# If the value for character is "Ron", then print out "Wicked".
# If the value for character is any other character, then print out "Why is it always you three?"


def main():
    character = ""
    if character == "Harry":
        print("Expecto Patronum")
    elif character == "Hermione":
        print("It's LeviOsa")    
    elif character == "Ron":
        print("Wicked")
    else:
        print("Why is it always you three?")
        
if __name__ == "__main__":
    main()