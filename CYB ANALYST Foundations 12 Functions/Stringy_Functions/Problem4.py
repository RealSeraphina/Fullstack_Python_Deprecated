# Define a function named space_count, which takes a string as an argument, 
# and returns the number of spaces in the string. Note: If there are no spaces, it should return 0.

def space_count(dasString):
    numSpaces = 0
    for char in str(dasString):
        if char == " ":
            numSpaces += 1
    return numSpaces

def main():
    print(str(space_count("ThisstringhasZEROspaces!")))
    print(str(space_count("This string has four spaces!")))
    
if __name__ == "__main__":
    main()