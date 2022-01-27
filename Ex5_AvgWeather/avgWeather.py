print("Welcome to the WeatherAverager. Asks the weather for the last 3 days and gives an average temperature. \n Made by Qubisted | Advaith Sai")

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
print(str(answerfinal)+units)



