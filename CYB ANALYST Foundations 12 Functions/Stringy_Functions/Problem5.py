# Define a function named how_many_vowels, 
# which takes in a strings and returns the total number of vowels of the string.

def how_many_vowels(dasString):
    numVowels = 0
    for char in str(dasString).lower():
        if char in "aeiouy":
            numVowels += 1
    return numVowels    

def main():
    print(str(how_many_vowels("I love Leek Spin")))
    
if __name__ == "__main__":
    main()