# Write control flow for a string that uppercases any lowercase letters and lowercases any uppercase letters in a string, 
# and prints the newly formatted string.
# Hint: Pseudocode breakdown
# Click to toggle hint

#     Declare a variable called string and set it equal to an empty string.
#     Declare a variable called new_string and set it equal to an empty string.
#     For every character in the string,
#         if the character is lowercase, switch it to uppercase, and add it to new_string
#         if the character is uppercase, switch it to lowercase, and add it to new_string
#         if the character is anything else, add it to the new_string
#     print the new_string

# Hint: How do .upper(), .lower(), .isupper(), .islower() work?
# Click to toggle hint
# https://www.geeksforgeeks.org/isupper-islower-lower-upper-python-applications/

def main():
#     Declare a variable called string and set it equal to an empty string.
    string = "TeSt!"
#     Declare a variable called new_string and set it equal to an empty string.
    new_string = ""
#     For every character in the string,
    for char in string:
#       if the character is lowercase, switch it to uppercase, and add it to new_string
        if char.islower():
            new_string = new_string + char.upper()
#       if the character is uppercase, switch it to lowercase, and add it to new_string
        elif char.isupper():
            new_string = new_string + char.lower()
#       if the character is anything else, add it to the new_string
        else:
            new_string = new_string + char
#   print the new_string
    print(new_string)

if __name__ == "__main__":
    main()