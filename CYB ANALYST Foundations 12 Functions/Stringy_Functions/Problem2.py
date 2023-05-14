# Define a function named less_than_ten, which takes in a string and returns True if the length of the string is less than 10 and False otherwise.
# Hint: How does len() work?
# https://www.geeksforgeeks.org/python-string-length-len/

def less_than_ten(dasString):
    if len(str(dasString)) < 10:
        return True
    else:
        return False

def main():
    print(less_than_ten("ABCDEFGHI"))
    print(less_than_ten("ABCDEFGHIJ"))
    print(less_than_ten(123456789))
    print(less_than_ten(1234567890))

if __name__ == "__main__":
    main()