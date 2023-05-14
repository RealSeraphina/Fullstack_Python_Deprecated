# Define a function named multiple_of_3, 
# which takes one argument, an integer, 
# and returns True if the integer is a multiple of 3 and False otherwise.

def multiple_of_3(num):
    if num % 3 == 0:
        return True
    else:
        return False

def main():
    print(multiple_of_3(6))
    print(multiple_of_3(7))
    
if __name__ == "__main__":
    main()