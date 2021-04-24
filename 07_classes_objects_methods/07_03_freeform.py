'''
- Write a script with three classes that model everyday objects.
- Each class should have an __init__ method that sets at least three attributes
- Include a __str__ method in each class that prints out the attributes
    in a nicely formatted string.
- Overload the __add__ method in one of the classes so that it's possible
    to add attributes of two instances of that class using the + operator.
- Create at least two instances of each class.
- Once the objects are created, change some of their attribute values.

Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, card games, sports teams, trees, people etc...

'''

#animals: name, kingdom, discovery status
class Animal:
    '''Store the name, kingdom, and endangered status of an animal. Allow changing endangered status.'''

    def __init__(self,name,kingdom,status):
        self.name = name
        self.kingdom = kingdom
        self.endangered = status

    def __repr__(self):
        return f"Name: {self.name}\nKingdom: {self.kingdom}\nEndangered: {self.endangered}"

    def __str__(self):
        is_isnot = "is"
        if not self.endangered:
            is_isnot += " not"
        return f"The {self.name} is a {self.kingdom}. It {is_isnot} endangered."

    def change_status(self):
        if self.endangered:
            self.endangered = False
            print(f"The {self.name} is no longer endangered.")
        else:
            self.endangered = True
            print(f"The {self.name} has become endangered.")

#mammals: subclass of animals; allow "addition" to create hybrids
class Mammal(Animal):
    '''Create a subclass of Animal which allows hybridization'''

    def __init__(self,name,status,hybrid):
        self.name = name
        self.kingdom = "Mammal"
        self.endangered = status
        self.ishybrid = hybrid
    
    def __repr__(self):
        return f"{super().__repr__()}\nHybrid status: {self.ishybrid}"

    def __str__(self):
        is_isnot = "is"
        if not self.ishybrid:
            is_isnot += " not"
        return f"{super().__str__()} It {is_isnot} a hybrid."
    
    def __add__(self,other):
        start = self.name[0]
        end = other.name[1:]
        name = start + end
        return Mammal(name,True,True)
    
    def __radd__(self,other):
        print(f"Does not produce viable offspring with {self.name}.")

#zoo: contain animals and revenue
class Zoo:
    '''Define a zoo containing an animal library and an annual revenue. Allow gaining and losing animals, and zoo mergers'''

    def __init__(self,name,animals,revenue):
        self.name = name
        self.animals = animals
        self.revenue = revenue
    
    def __repr__(self):
        result = f"Zoo {self.name} has annual revenue {self.revenue}. It contains:"
        for animal,count in self.animals.items():
            result += f"\n\n{animal.__repr__()}\nCount: {count}"
        return result
    
    def __str__(self):
        result = f"The {self.name} makes ${self.revenue:,} per year. It has the following animals:"
        for animal,count in self.animals.items():
            result += f"\n{count} {animal.name}"
            if count > 1:
                result += "s"
        return result
    
    def __add__(self,other):
        '''Produce a merger of two zoos'''
        name_start = self.name.replace("Zoo","")
        new_name = name_start + other.name
        new_animals = self.animals.copy()
        for animal,count in other.animals.items():
            if new_animals.get(animal) != None:
                new_animals[animal] += count
            else:
                new_animals[animal] = count
        new_revenue = self.revenue + other.revenue
        return Zoo(new_name,new_animals,new_revenue)
    
    def gain(self,animal):
        '''add an animal to the zoo's list'''
        if self.animals.get(animal) != None:
            self.animals[animal] += 1
        else:
            self.animals[animal] = 1
    
    def lose(self,animal):
        '''remove an animal from the zoo's list'''
        if self.animals[animal] > 1:
            self.animals[animal] -= 1
        else:
            del self.animals[animal]

#Create animals an mammals
turtle = Animal("Turtle","Reptile",False)
print(turtle)
salmon = Animal("Salmon","Fish",False)
print(salmon)
mistfrog = Animal("Mountain Mistfrog","Amphibian",True)
print(mistfrog)
tiger = Mammal("Tiger",True,False)
print(tiger)
lion = Mammal("Lion",False,False)
print(lion)
mule = Mammal("Mule",False,True)
print(mule)

#Change endangered status of an animal
salmon.change_status()
print(salmon)

#Try to make hybrids of animals
liger = lion + tiger
print(liger)
siger = salmon + tiger

#Create zoos
zoo1_animals = {
    turtle: 5,
    mistfrog: 2,
    tiger: 1,
    lion: 6,
    liger: 1
}

zoo2_animals = {
    turtle: 1,
    salmon: 20,
    tiger: 2,
    mule: 2
}

zoo1 = Zoo("Philadelphia Zoo",zoo1_animals,20000000)
print(zoo1)
zoo2 = Zoo("Brandywine Zoo",zoo2_animals,800000)
print(zoo2)

#Merge zoos
zoo3 = zoo1 + zoo2
print(zoo3)

#Gain and lose animals
zoo3.gain(mistfrog)
print(zoo3)
zoo3.lose(salmon)
print(zoo3)
zoo3.lose(liger)
print(zoo3)