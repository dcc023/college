#Assignment 0: Favorite programming language
#by: Dylan Campbell
#-------------------------
# HOW-TO
#-------------------------
# Requirements:
#  * Python 3 or greater
#  * a command line
# 
# Instructions:
#  * Save this file
#  * In your CLI, move to the containing directory, i.e cd
#  * Type "python3 hw0.py" without the quotes.
#  * The file should execute and give you an input prompt
#  * Obey the program from there
#


#functions
def yes():
    print("\n-------------------------------------")
    print(" KNOWN LANGUAGES")
    print("-------------------------------------")
    print("Java")
    print("Javascript")
    print("Python")
    print("C++")
    print("C")
    print("")
    input_var = input("Want to know why Python is my favorite language?\nyes/no: ")
    if input_var.lower() in ('yes','y'):
        print("\n  Python cuts out a lot of the syntactic clutter that most other languages force upon you.  No semi colons, no brackets, etc. Its nice to be able to just write the code in a simple to read fashion. I really enjoy some of the built-ins as well, like dictionaries. Shoutout to Dr. Ben Choi for showing me the light.\n")



#main
input_var = input("\nWelcome!\nWould you like to see a list of my known programming languages?\nyes/no: ")

if input_var.lower() in ('yes','y'):
    yes()
else:
    input_var = input("Last chance!\nyes/no: ")
    if input_var.lower() in ('yes','y'):
        yes()



    
    
    
