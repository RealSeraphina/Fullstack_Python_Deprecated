# Declare two variables num_1 and num_2. Count down from num_1 to num_2 by 1 (inclusively). When you're done, print out "Blast Off!". 
# Assume num_1 is greater than num_2.
# num_1 = 5
# num_2 = 2
# EXPECTED
# 5
# 4
# 3
# 2
# Blast Off!
# num_1 = 3
# num_2 = 1
# EXPECTED
# 3
# 2
# 1
# Blast Off!

def main():
    num_1 = 3
    num_2 = 1
    while num_1 >= num_2:
        print(str(num_1))
        num_1 = num_1 - 1
    print("Blast Off!")
if __name__ == "__main__":
    main()