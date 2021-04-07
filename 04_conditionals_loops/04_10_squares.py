'''
Write a script that prints out all the squares of numbers from 1- 50

Use a for loop that demonstrates the use of the range function.

'''
#solution for my first reading of this: print each number from 1 to 50, squared
for n in range(1,51):
    print(n*n)

#solution for my second reading (becuase the first one was trivial): print all the perfect squares between 1 and 50
import math

for n in range(1,51):
    if math.sqrt(n)%1 == 0:
        print(n)