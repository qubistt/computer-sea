
number_names = ("zero-invalid", "one-invalid", "two-invalid", "triangle", "quadrilateral",
                "pentagon", "hexagon", "heptagon", "octagon", "nonagon", "decagon", "hendecagon", "dodecagon")

print("Welcome to the Polygoner. Give it a number of sides, between 3-12 and get the polygon's name \n Made by Qubisted | Advaith Sai")

number = input("How many sides does your myster polygon have? > ")

answer = number_names[int(number)]
print(answer)


