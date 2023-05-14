# Define a function named how_many_legs, 
# which takes three parameters, num_cows, 
# num_chickens, and num_spiders and returns the total number of legs.

def how_many_legs(num_cows, num_chickens, num_spiders):
    total_num_legs = (num_cows * 4) + (num_chickens * 2) + (num_spiders * 8)
    return total_num_legs

def main():
    print(str(how_many_legs(0,0,0)))
    print(str(how_many_legs(1,0,0)))
    print(str(how_many_legs(0,1,0)))
    print(str(how_many_legs(0,0,1)))
    print(str(how_many_legs(1,1,0)))
    print(str(how_many_legs(0,1,1)))
    print(str(how_many_legs(1,0,1)))
    print(str(how_many_legs(1,1,1)))
    
if __name__ == "__main__":
    main()