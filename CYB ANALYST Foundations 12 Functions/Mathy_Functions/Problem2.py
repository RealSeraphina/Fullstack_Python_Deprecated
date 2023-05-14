#Define a function named greater_than_ten, which takes in an integer 
# and returns True if the number is greater than 10 
# and False if the number is less than 10.

def greater_than_ten(num):
    if num > 10:
        return True
    elif num < 10:
        return False
    else:
        return "0xDEADBEEF"

def main():
    print(greater_than_ten(11))
    print(greater_than_ten(9))
    print(greater_than_ten(10))

if __name__ == "__main__":
    main()