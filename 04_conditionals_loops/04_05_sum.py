'''
Take two numbers from the user, one representing the start and one the end of a sequence.
Using a loop, sum all numbers from the first number through to the second number.

For example, if a user enters 1 and 100, the sequence would be all integer numbers from 1 to 100.
The output of your calculation should therefore look like this:

The sum is: 5050
'''

def getIntInput(var_name):
    result = ""
    while type(result) != "int":
        try:
            result = int(input(f"Please enter the {var_name} value to add: "))
            break
        except ValueError:
            print("Please enter an integer.")
    return result

first = getIntInput("first")
last = getIntInput("last")
sum = 0 

for n in range(first,last+1):
    sum += n

print("The sum is: ",sum)