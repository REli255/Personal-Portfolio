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
from Random_Password_Generator.main_p import password_management
from Rock_Paper_Scissors.main_r import battle
from Tic_Tac_Toe_game.main_t import game

# function with the user interface
def main():
    # user input that lets them select a program to run
    choice = input("""1. Average Grade program
    2. Character Creator program
    3. Graded Quiz program
    4. Random Password Generator program
    5. Rock, Paper, Scissors program
    6. Tic-Tac-Toe Game program
    7. End
    Enter the number of the thing you would like to do: """)

    # conditional that runs the selected porgram after printing information about it
    if choice == "1":
        print("\nThis program lets a user enter their grades and get back the average. This was a easy project. I learned to average in code.\n")
        grades()
    elif choice == "2":
        print("\nThis program lets a user choose a name, race, and class for a character. Then it displays that character's information/stats. This is my favorite project I have made. I leaerned how to use conditonals.\n")
        select()
    elif choice == "3":
        print("\nThis program lets a user take a quiz. Then it gives them a grade. This was a easy project. I learned to check acuracy.\n")
        quiz()
    elif choice == "4":
        print("\nThis program lets a user generate a password of a specified length and containing selected character types. This was a fun project. I learned to use specified lists.\n")
        password_management()
    elif choice == "5":
        print("\nThis program lets a user play rock, paper, scissors aginst the computer. This was a challenging project. I learned how to check winning conditions and random.\n")
        battle()
    elif choice == "6":
        print("\nThis program lets a user play Tic-Tac-Toes aginst the computer. This was a challenging project. It tought me how to loop through a grid.\n")
        game()
    elif choice == "7":
        return "end"
    else:
        print("that is not an option")
        print("you must enter the number to the left of the program you want to run.")

# statement that prints the introduction
print("\nThis project is a portfolio of a few of the projects I have made in the programing classes I have taken.\nThe user must select the program they want to run by entering the number to the left of it. Then the selected program will run.\n")

# loop that makes sure the program continues until the user is done 
while True:
    end = main()
    if end == "end":
        print("thank you for using this program")
        break