'''
Write the necessary code to print out the result of the following:

	2 + 4 + 6 + 8 + 9 + 10 + 12 + 14 + 16 + 18

'''

x = 2
res = x
while x < 18:
    x += 2
    res += x
print(res+9)
