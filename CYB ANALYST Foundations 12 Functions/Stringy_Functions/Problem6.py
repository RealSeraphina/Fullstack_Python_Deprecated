# Define a function named three_es, which takes in one argument, 
# a string, and returns True if the string contains at least 
# 3 e's and False otherwise. Don't forget to account for capitalization.

def three_es(dasString):
    eCount = 0
    for char in str(dasString).lower():
        if char == "e":
            eCount += 1
    if eCount >= 3:
        return True
    else:
        return False

def main():
    print(three_es("Leek only has two e chars but this string has 3"))
    
if __name__ == "__main__":
    main()