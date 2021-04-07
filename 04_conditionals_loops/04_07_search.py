'''

Receive a number between 0 and 1,000,000,000 from the user.
Use while loop to find the number - when the number is found exit the loop and print the number to the console.

'''

#why on earth would i do this?
#literally just run a loop to reach a number we already have?

number = ""

while type(number) != "int":
    try:
        number = int(input("Please enter a number between 0 and 1,000,000,000: "))
        if number < 0 or number > 1000000000:
            print("Please enter a number in range.")
            continue
        break
    except ValueError:
        print("Please enter an integer.")

number_check = 0

while number_check != number:
    number_check += 1

print(number_check)