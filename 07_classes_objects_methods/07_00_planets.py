'''
Create a Planet class that models attributes and methods of
a planet object.

Use the appropriate dunder method to get informative output with print()

'''

class Planet():
    '''Define planets in systems'''

    def __init__(self,name,system,kind,temp):
        self.name = name
        self.system = system
        self.type = kind.lower()
        self.temp = temp
    
    def __repr__(self):
        return f"Planet name: {self.name}; System: {self.system}; Type: {self.type}; Temperature: {self.temp}."
    
    def __str__(self):
        return f"{self.name} is a {self.type} planet with average temperature {self.temp} degrees celcius. It's in the {self.system} system."

    def is_habitable(self):
        """Return True if the planet may be habitable based on type and temp; False otherwise"""
        if self.type == "rocky" and (-40 < self.temp < 50):
            print(f"{self.name} is habitable.")
            return True
        else:
            print(f"{self.name} is not habitable.")
            return False

#for testing:
p = Planet("Mars", "Solar", "Rocky", -30)
print(p)
p.is_habitable()