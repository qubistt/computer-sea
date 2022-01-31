print("Welcome to the Area Tool. Choose a shape from the menu, input the lengths, and get your area! \n Made by Qubisted | Advaith Sai")
def calcArea(r):
    r = float(input('What is the radius of the circle? > '))
    PI = 3.142
    Area = PI * (r*r)
    print("The area of your given square is: %.2f" %Area)
    goAgain()

def calcRect():
    l = float(input('What is the length of the rectangle? > '))
    b = float(input('What is the breadth of the rectangle? > '))
    Area = l * b
    print("The area of your given square is: %.2f" %Area)
    goAgain()

def calcSquare():
    l = float(input('What is the length of the square? > '))
    Area = l * l
    print("The area of your given square is %.2f" %Area)
    goAgain()

def askMenu():
    menu = input("Of what shape would you like to calculate the area? \n a) Circle \n b) Rectangle \n c) Square \n Choose a, b or c > ")

    if menu == 'a':
        calcArea()

    if menu == 'b':
        calcRect()

    if menu == 'c':
        calcSquare()

def goAgain():
    answer = str(input("Want to go again? y/n > "))
    if answer == "y":
        askMenu()
    else:
        print("Bye!")
        quit()

askMenu()