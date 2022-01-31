print("Welcome to the WeatherAverager. Asks the weather for the last 3 days and gives an average temperature. \n Made by Qubisted | Advaith Sai")
def get_weather():
    units = str(input("Celsius or Fahrenheit? C/F > "))
    day1 = float(input('What was the temperature day before yesterday? > ')) 
    day2 = float(input('What was the temperature yesterday? > ')) 
    day3 = float(input('What is the temperature today? > '))

    if units == "C":
        units = " °C"

    elif units == "F":
        units = " °F"

    answer1 = day1+day2+day3
    answerfinal = answer1/3
    formatAnswerFinal = "{:.2f}".format(answerfinal)
    print("Your average temperature is:",(str(formatAnswerFinal))+units)
    goAgain()

def goAgain():
    answer = str(input("Want to go again? y/n > "))
    if answer == "y":
        get_weather()
    else:
        print("Bye!")
        quit()

get_weather()


