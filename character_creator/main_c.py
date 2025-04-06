# Eli Robison, Character Creator

# lists of posible classes and races
races = ["human", "elf", "goblin", "orc"]
classes = ["berserker", "fighter", "ranger", "wizard"]

# function that lets the user make a new character
def select():
    name = input("enter the name of your character: ")
    xp = 0

    # function that controls the traits of the selected race
    def race_selection():
        race = input("select the race of your character (1=human, 2=elf, 3=goblin, 4=orc): ")
        if race == "1":
            race = races[0]
            health = 22
            strength = 11
            speed = 11
            defense = 5.5
        elif race == "2":
            race = races[1]
            health = 24
            strength = 10
            speed = 12
            defense = 5.5
        elif race == "3":
            race = races[2]
            health = 28
            strength = 11
            speed = 14
            defense = 5
        elif race == "4":
            race = races[3]
            health = 26
            strength = 14
            speed = 8
            defense = 4.5
        else:
            print("that is not an option")
            print("enter the number to the left of the class you want to use")
            race_selection()
        return race, health, strength, speed, defense
    race, health, strength, speed, defense = race_selection()

    # function that controls the traits of the selected class
    def class_selection(health, strength, speed, defense):
        job = input("select the class of your character (1=berserker, 2=fighter, 3=ranger, 4=wizard): ")
        if job == "1":
            job = classes[0]
            health += 4
            strength += 4
            speed -= 1
            defense -= 1
        elif job == "2":
            job = classes[1]
            health += 2
            strength += 1
            speed += 1
            defense += 1
        elif job == "3":
            job = classes[2]
            health += 0
            strength -= 1
            speed += 4
            defense += 1
        elif job == "4":
            job = classes[3]
            health += 2
            strength -= 1
            speed -= 1
            defense += 5
        else:
            print("that is not an option")
            print("enter the number to the left of the class you want to use")
            class_selection()
        return job, health, strength, speed, defense
    job, health, strength, speed, defense = class_selection(health, strength, speed, defense)
    
    print(name, "is a", race, job, "with", health, "health,", strength, "strength,", speed, "speed and", defense, "defense")