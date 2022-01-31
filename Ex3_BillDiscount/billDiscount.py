print("Welcome to the Bill Disount. Gives a discount on your bill based upon the bill amount. \n Made by Qubisted | Advaith Sai")


def get_amount():
    bill = int(input("What is your bill amount? > "))

    if bill >= 2000:
        discount = (10*bill)/100
        finalBill = (bill-discount)
        print("\n Please enjoy a discount of 10%, saving you "+str(discount),"rupees. \n Final bill amount is: "+str(finalBill))
        goAgain()

    elif bill >= 1501 and bill < 2000:
        discount = (8*bill)/100
        finalBill = (bill-discount)
        print("\n Please enjoy a discount of 8%, saving you "+str(discount),"rupees. \n Final bill amount is: "+str(finalBill))
        goAgain()

    elif bill >= 1000 and bill <= 1500:
        discount = (5*bill)/100
        finalBill = (bill-discount)
        print("\n Please enjoy a discount of 5%, saving you "+str(discount),"rupees. \n Final bill amount is: "+str(finalBill))
        goAgain()

    elif bill < 1000:
        print("\n Sorry, no discount. \n Final bill amount is: "+str(bill))
        goAgain()


def goAgain():
    answer = str(input("Want to go again? y/n > "))
    if answer == "y":
        get_amount()
    else:
        print("Bye!")
        quit()

get_amount()