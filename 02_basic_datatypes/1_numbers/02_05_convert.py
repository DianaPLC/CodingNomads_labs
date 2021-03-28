'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''
num = 4
num_float = float(num)
print(num_float)
num_int = int(num_float)
print(num_int)
floor_result = 4//2.2
print(floor_result)

val1 = float(input("Please enter a number: "))
val2 = float(input("Please enter another number to multiply by: "))
product = val1*val2
print(product)