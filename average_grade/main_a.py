# Eli Robison, average grade

def grades():
    p = int(input("enter programing grade: "))
    g = int(input("enter geography grade: "))
    a = int(input("enter advisory grade: "))
    m = int(input("enter math grade: "))
    b = int(input("enter biology grade: "))
    e = int(input("enter english grade: "))

    average = round((p+g+a+m+b+e)/6)

    name = input("enter name: ")

    print(name,"'s average grade is",average,"%")