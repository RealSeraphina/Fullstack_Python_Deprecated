# Create a variable with value of the string "Pneumonoultramicroscopicsilicovolcanoconiosis". Loop through the string and print out the vowels.

def main():
    marryPoppins = "Pneumonoultramicroscopicsilicovolcanoconiosis"
    for char in marryPoppins:
        if char.lower() in "aeiouy":
            print(char)
if __name__ == "__main__":
    main()