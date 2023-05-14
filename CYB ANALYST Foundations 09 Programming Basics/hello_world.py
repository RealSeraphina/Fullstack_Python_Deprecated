# Hello World
# It is time to create your very first Python Script!
# The history of a programmer's first program being the string 'Hello World!' is well known, and we are excited for you to begin your own journey into programming with this time honored tradition.
# hello_world.py
#     Create a new file called hello_world.py
#     Edit your new file (preferably using VIM) so that the first line prints out the string 'Hello World!'
#     On the second line of your script, create your first variable called name and assign it the value of your first name
#     On the third line, use concatenation to print out the phrase 'My name is <NAME> and I will be a Python Master!' using the variable name in place of <NAME>
#     Using the python3 interpreter, run your new script!

# Hint: Click here for hints
#     How do we create a new python file in linux? Ex: touch planet.py (Note that "planet.py" is the name of the file, so you'll want to change this!)
#     Use the print() function and put what you would like to print out in between the parens, (). Ex: print('hi there')
#     Use the assignment operator, =, to create your variable. Ex: planet = 'earth'
#     Use the concatenation operator, +, to concatenate your string, and use the print() you learned earlier to print it out. Ex: print('I live on planet ' + planet)
#     Save your python script, and run it on the CMD line using the python3 command and then the name of your new script. Ex: python3 planet.py

def main():
    print("Hello World!")
    name = "Seraphina"
    print("My name is " + name + " and I will be a Python Master!")
if __name__ == "__main__":
    main()
