import sys
import time

print("Welcome to the DiviCheck. Checks if a number is divisible by 5 and 11 \n Made by Qubisted | Advaith Sai")

def check():
    number = int(input("Enter any positive integer > "))

    if((number % 5 == 0) and (number % 11 == 0)):
        print("The number "+str(number)+" is divisible by 5 and 11")
    else:
        print("The number "+str(number)+" is not divisible by 5 and 11")
    goAgain()
    
def goAgain():
    answer = str(input("Want to go again? y/n > "))
    if answer == "y":
        check()
    else:
        print("Bye!")
        time.sleep(3)
        sys.exit()
        

check()
