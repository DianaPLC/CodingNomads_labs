'''
Fahrenheit to Celsius:

Write the necessary code to read a degree in Fahrenheit from the console
then convert it to Celsius and print it to the console.

    C = (F - 32) * (5 / 9)

Output should read like - "81.32 degrees fahrenheit = 27.4 degrees celsius"


'''
degrees_f = ""
while type(degrees_f) != "float":
    try:
        degrees_f = float(input("Enter the temperature in degrees Fahrenheit: "))
        break
    except ValueError:
        print("Please only enter a number.")

degrees_c = (degrees_f - 32) * (5/9)

print(degrees_f," degrees fahrenheit = ",degrees_c," degrees celsius")
