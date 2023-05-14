# Declare a variable called num. Print out the number of times you can divide num in half until it is less than or equal to 1.
# Tip: Remember the difference between nums and floats.
# Try this for all different values of num:
# num = 2
# EXPECTED: 1
# num = 200
# EXPECTED: 8

def main():
    num = 200
    divCount = 0
    while num >= 1:
        num = num / 2
        divCount = divCount + 1
    print(str(divCount))

if __name__ == "__main__":
    main()