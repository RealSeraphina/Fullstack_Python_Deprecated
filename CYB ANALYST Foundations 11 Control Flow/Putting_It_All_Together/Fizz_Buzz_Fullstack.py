# Write control flow that prints every number from 1 up to 100 inclusively. 
# However, if the current number is evenly divisible by 3, print "Full" instead, 
# if the current number is evenly divisible by 5, print "Stack" instead, and if 
# the current number is evenly divisible by BOTH 3 and 5, print out "FullStack" instead.
# Hint: Pseudocode breakdown
#     Loop up to 100 using range
#         if the current number is divisible by both 3 and 5, print out "FullStack"
#         if the current number is divisible by 3, print out"Full"
#         if the current number is divisible by 5, print out "Stack"
#         for any other number, print out the number

# Hint: How does % (modulus) work?
# Click to toggle hint
# https://linuxize.com/post/python-modulo-operator/



def main():
#   Loop up to 100 using range
    for currNum in range(0,101):
#       if the current number is divisible by both 3 and 5, print out "FullStack"
        if currNum%3 == 0 and currNum%5 == 0:
            print("FullStack")
#       if the current number is divisible by 3, print out"Full"
        elif currNum%3 == 0:
            print("Full")
#       if the current number is divisible by 5, print out "Stack"
        elif currNum%5 == 0:
            print("Stack")
#       for any other number, print out the number
        else:
            print(str(currNum))

if __name__ == "__main__":
    main()