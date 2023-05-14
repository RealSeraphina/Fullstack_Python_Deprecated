# Define a function named odd_or_even which takes in an integer 
# and returns 'odd' if the number is odd, and 'even' if the number is even.
# Hint: How does % (modulus) work?
# https://linuxize.com/post/python-modulo-operator/

def odd_or_even(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"
    return "0xDEADBFF"

def main():
    print(odd_or_even(0))
    print(odd_or_even(1))
    print(odd_or_even(2))
    print(odd_or_even(3))
    print(odd_or_even(4))
    print(odd_or_even(5))
    

if __name__ == "__main__":
    main()