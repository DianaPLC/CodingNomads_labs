'''

Write a script that completes the following tasks.

'''

# define a function that determines whether the number is divisible by 4 or 7 and returns a boolean
def divisible_4or7(n: int) -> bool:
    """take an int input and return a bool indicating if the int is divisible by 4 or 7"""
    
    if n%4 == 0 or n%7 == 0:
        return True
    else:
        return False

# define a function that determines whether a number is divisible by both 4 and 7 and returns a boolean
def divisible_4and7(n: int) -> bool:
    """take an int input and return a bool indicating if the int is divisible by 4 and 7"""
    
    if n%4 == 0 and n%7 == 0:
        return True
    else:
        return False

# take in a number from the user between 1 and 1,000,000,000
user_number = ""
while type(user_number) != "int":
    try:
        user_number = int(input("Please enter an integer between 1 and 1,000,000,000: "))
        if user_number < 1 or user_number > 1000000000:
            print("That number is not in range.")
            continue
        break
    except ValueError:
        print("That isn't an integer.")


# call your functions, passing in the user input as the arguments, and set their output equal to new variables 
is_divisible_4or7 = divisible_4or7(user_number)
is_divisible_4and7 = divisible_4and7(user_number)

# print your new variables to display the results
print("divisible by either: ",is_divisible_4or7)
print("divisible by both: ",is_divisible_4and7)