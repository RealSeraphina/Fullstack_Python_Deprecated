# Define a function named even_or_odd which takes in a string 
# and returns 'odd' if the length of the string is odd, and 
# 'even' if the length of the string is even. 

def even_or_odd(dasString):
    if len(str(dasString)) % 2 == 0:
        return "even"
    else:
        return "odd"

def main():
    print(even_or_odd("EVEN"))
    print(even_or_odd("ODD"))
    
if __name__ == "__main__":
    main()