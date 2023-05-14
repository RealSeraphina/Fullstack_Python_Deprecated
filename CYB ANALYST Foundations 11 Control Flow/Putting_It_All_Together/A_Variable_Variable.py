# Write control flow that has a variable called variable that can accept a str, an int or a float. Then print out each character or digit on a new line.
# Hint: Pseudocode breakdown

#     Declare a variable called variable
#     if the type of variable is not a string
#         reassign variable to variable cast as a string
#     for every character in variable
#         print out each character

# Hint: How does type() work?
# https://www.w3schools.com/python/ref_func_type.asp

def main():
#   Declare a variable called variable
    variable = 1234567890
#   if the type of variable is not a string
    if type(variable) != type(""):
#       reassign variable to variable cast as a string
        variable = str(variable)
#   for every character in variable
    for char in variable:
#       print out each character    
        print(char)

if __name__ == "__main__":
    main()