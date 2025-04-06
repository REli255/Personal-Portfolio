# Eli Robison, Personal Portfolio

"""
OVERVIEW:
Create a user interface for your projects that shows of the programming projects you are most proud of (NOTE: you can keep this in the same repository IF you are using all of the projects from this class OR you can create a new repository called "personal_portfolio"). This program will in many ways serve as a programming resume for you so please make sure to make the user interfaces VERY intuitive.

REQUIREMENTS:
Introduction:
    Brief explanation of what your portfolio is 

    How to use it (keep it short but informative)

Menu: 

    Create an easy-to-use menu

    Include at least 6 projects you're proud of

    Can be from this class or others

    Example: A numbered list or clickable buttons for each project

Project Descriptions: For each project, include:

    What the project does

    How you found the programming process

    What you learned

    Your role (if it was a group project)

    Note: This information should appear before the code runs

Working Projects: 

    Make sure all projects actually work when selected
"""

# statements to import functions
from average_grade.main_a import grades
from character_creator.main_c import select
from Graded_Quiz.main_g import quiz
from Random_Password_Generator.main_R import password_management
from Rock_Paper_Scissors.main_r import battle
from Tic_Tac_Toe_game.main_t import game

# function with the user interface
def main():
    choice = input("""1. Get change for a amount of money
    2. 
    3. 
    4. 
    5. 
    6. 
    7. End
    Enter the number of the thing you would like to do: """)
    if choice == "1":
        grades()
    elif choice == "2":
        select()
    elif choice == "3":
        quiz()
    elif choice == "4":
        password_management()
    elif choice == "5":
        battle()
    elif choice == "6":
        game()
    elif choice == "7":
        return "end"
    else:
        print("that is not an option")

# loop that makes sure the program continues until the user is done 
while True:
    end = main()
    if end == "end":
        print("thank you for using this program")
        break