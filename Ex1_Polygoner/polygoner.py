number_names = ("zero-invalid", "one-invalid", "two-invalid", "tri", "tetra",
                "penta", "hexa", "hepta", "octa", "nona", "deca", "hendeca", "dodeca", "Triskaideca", "Tetradeca",)

print("Welcome to the Polygoner. Give it a number of sides, between 3-12 and get the polygon's name \n Made by Qubisted | Advaith Sai")
def get_polygon_name():
    number = input("How many sides does your mystery polygon have? > ")

    answer = number_names[int(number)]
    print("It is a/an "+answer+"gon!")
    goAgain()

def goAgain():
    answer = str(input("Want to go again? y/n > "))
    if answer == "y":
        get_polygon_name()
    else:
        print("Bye!")
        quit()

get_polygon_name()



