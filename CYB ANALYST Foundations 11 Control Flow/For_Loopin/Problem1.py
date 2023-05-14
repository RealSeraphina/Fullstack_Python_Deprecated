# Declare two variables num_1 and num_2 and make sure num_2 is greater than num_1
# Print out the sum of numbers between num_1 and num_2 including both num_1 and num_2. Use the sample values below to check your work.
# num_1 = 1
# num_2 = 3
# # EXPECTED: sum == 6
# num_1 = 5
# num_2 = 10
# # EXPECTED: sum == 45

def main():
    num_1 = 5
    num_2 = 10
    total = 0
    for num in range(num_1, num_2+1):
        total = total + num
    print(str(total))

if __name__ == "__main__":
    main()