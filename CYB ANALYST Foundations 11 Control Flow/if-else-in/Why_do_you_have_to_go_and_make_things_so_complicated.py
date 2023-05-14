# Declare two variables you and u in your code and set their values to be strings.
# If the value in you is equal to "fall" and the value in u is equal to "crawl" then print out: "and you break".
# If the value in you is equal to "take" and u is equal to "get" then print out: "you turn it into".
# Finally, if both of these conditions fail, print: "No, no, no".


def main():
    you = ""
    u = ""
    if you == "fall" and u == "crawl":
        print("and you break")
    elif you == "take" and u == "get":
        print("you turn it into")
    else:
        print("No, no, no")
if __name__ == "__main__":
    main()