'''
CLASSES AND INHERITANCE
=======================

1) Define an empty Movie class.

2) Add a dunder init method that takes two arguments "year" and "title"

3) Create a sub-class called "RomCom" that inherits from the Movie class

4) Create another sub-class of the Movie class called "ActionMovie"
    that overwrites the dunder init method of Movie and adds another
    instance variable called "pg" that is set by default to the number 13.

5) EXTRA: If you finish early, use the time to practice flushing out these
    classes and white-boarding code. What attributes could a Movie class
    contain? What methods? What tricks can you use through inheritance?
    Any class attributes you could add?

'''

# Movie class: takes "year" and "title"
class Movie:
    '''define movies by year and title'''

    def __init__(self,year,title):
        self.year = year
        self.title = title
    
    def __repr__(self):
        return f"Movie title {self.title}, released {self.year}."

    def __str__(self):
        return f"The movie '{self.title}' came out in {self.year}."

# RomCom class: inherits from Movie
class RomCom(Movie):
    pass

# ActionMovie class: inherits from Movie and adds attribute "pg" that defaults to 13
class ActionMovie(Movie):
    '''define movies by year, title, and rating'''

    def __init__(self,year,title,rating=13):
        super().__init__(year,title)
        self.pg = rating
    
    def __repr__(self):
        return f"{super().__repr__()} rating {self.pg}."
    
    def __str__(self):
        return f"{super().__str__()} It is rated PG{self.pg}."
    
#for testing:

movie = Movie(2002, "Catch Me if You Can")
print(movie)
romcom = RomCom(1999, "10 Things I Hate About You")
print(romcom)
action = ActionMovie(2018, "Black Panther")
print(action)
