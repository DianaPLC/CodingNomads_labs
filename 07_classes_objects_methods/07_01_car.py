'''
Write a class to model a car. The class should:

1. Set the attributes model, year, and max_speed in the __init__() method.
2. Have a method that increases the max_speed of the car by 5 when called.
3. Have a method that prints the details of the car.

Create at least two different objects of this Car class and demonstrate
changing the objects attributes.

'''

class Car:
    '''Define a car with descriptive and motion attributes, and define operations on speed.'''

    def __init__(self,model,year,max_speed):
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def __repr__(self):
        return f"{self.year} {self.model}. Max speed: {self.max_speed}"

    def __str__(self):
        return f"This is a {self.year} {self.model}. Its maximum speed is {self.max_speed}"

    def raise_max(self):
        '''Increase max_speed attribute by 5'''
        self.max_speed += 5
        print(f"The {self.year} {self.model} now has a maximum speed of {self.max_speed}")
    
#Create two Car instances
c1 = Car("Volvo",2005,80)
print(c1)
c2 = Car("Honda",2014,90)
print(c2)

#Increase speed for each
c1.raise_max()
c2.raise_max()