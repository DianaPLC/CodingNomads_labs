'''
Build on your previous freeform exercise.

Create subclasses of two of the existing classes. Create a subclass of
one of those so that the hierarchy is at least three levels.

Build these classes out like we did in the previous exercises.

If you cannot think of a way to build on your freeform exercise,
you can start from scratch here.

We encourage you to be creative and try to think of an example of
your own for this exercise but if you are stuck, some ideas include:

- A Vehicle superclass, with Truck and Motorcycle subclasses.
- A Restaurant superclass, with Gourmet and FastFood subclasses.

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

#bovid: subclass of mammal with added attribute "domesticated"
class Bovid(Mammal):
    '''Subclass of Mammal that includes a marker for domestication'''

    def __init__(self,name,status,hybrid,domestic):
        super().__init__(name,status,hybrid)
        self.domestic = domestic
    
    def __repr__(self):
        return f"{super().__repr__()}\nDomesticated: {self.domestic}"

    def __str__(self):
        is_isnot = "is"
        if not self.domestic:
            is_isnot += " not"
        return f"{super().__str__()} It {is_isnot} domesticated."
    
    def domesticate(self):
        if self.domestic:
            print(f"{self.name} is already domesticated.")
        else:
            self.domestic = True
            print(f"{self.name} has been domesticated.")

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

#Exhibit sublcass of Zoo, defines an area in the zoo
class Exhibit(Zoo):
    '''A subclass of Zoo that defines an area within a zoo'''

    def __init__(self,name,animals,revenue,terrain,manager):
        super().__init__(name,animals,revenue)
        self.terrain = terrain
        self.manager = manager
    
    def __repr__(self):
        result = f"Exhibit {self.name} has annual revenue {self.revenue}.\nTerrain type: {self.terrain}\nManager: {self.manager}\nAnimals:"
        for animal,count in self.animals.items():
            result += f"\n\n{animal.__repr__()}\nCount: {count}"
        return result
    
    def __str__(self):
        result = f"The {self.name} exhibit is a {self.terrain} area managed by {self.manager}. It makes ${self.revenue:,} per year.\nIt has the following animals:"
        for animal,count in self.animals.items():
            result += f"\n{count} {animal.name}"
            if count > 1:
                result += "s"
        return result

#for testing:
cow = Bovid("Cow",False,False,True)
print(cow)
buffalo = Bovid("Buffalo",False,False,False)
print(buffalo)

cow.domesticate()
buffalo.domesticate()
print(buffalo)

ex = Exhibit("Herds",{cow:4,buffalo:10},1000,"Prairie","Bill")
print(ex)

ex.lose(cow)
print(ex)