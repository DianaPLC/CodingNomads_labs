'''

Write a loop that for a number n prints n rows of stars in a triangle shape.

For example if n is 3, you print:

*
**
***

'''

n = 5

for count in range (1,n+1):
    row = "*" * count
    print(row)
