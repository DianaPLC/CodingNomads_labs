'''
Write the necessary code calculate the volume and surface area
of a cylinder with a radius of 3.14 and a height of 5. Print out the result.


'''

import math

height = 5
radius = 3.14

end_area = math.pi*(radius**2)
surface_area = (math.pi*2*radius*height) + (2*end_area)
volume = end_area*height

print("volume: ", volume, "surface area: ", surface_area)
