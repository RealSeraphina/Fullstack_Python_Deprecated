# For the following exercises, you should touch a new file and use your text editor of choice to write your code.
# After you have written some code to the file, you can save it and then execute it by typing python3 <path/to/your/file>
# This time we're talking about physical cookies! Get excited because you were hired to bake for an event and you need to figure out how many cookies to bake.
#     Declare a variable for num_people for the number of people that will come to your party.
#     If the number of people attending the event is 10 or greater, you want to bake 2 cookies per person. Write some code that will assign the number of cookies to bake to a variable.
#     If the number of people attending the event is less than 10 people, you want to bake 3 cookies per person to ensure your platters look full!
#     At the end be sure to print out the number of cookies you are planning on baking!

def main():
    num_people = 10
    num_cookies = 0
    if num_people >= 10:
        num_cookies = num_people * 2
    else:
        num_cookies = num_people * 3
    print(num_cookies)

if __name__ == "__main__":
    main()