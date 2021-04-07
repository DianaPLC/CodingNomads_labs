'''
Print out every prime number between 1 and 100.

'''
for number in range(1,101):
    to_print = True
    for divisor in range(2,number):
        if number % divisor == 0:
            to_print = False
    if to_print == True:
        print(number)