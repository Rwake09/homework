# imported tan, cos and pi from the math module

from math import pi, tan, cos

# created a set of variables for each of the parameters inputted
barrel_height = 1
distance_travelled = 0.5
intial_velocity = 44
acceleration = 9.81
theta = 80 * pi/180

#  created the equation  for determining the height of the projectile at 0.5 meters ahead
a = barrel_height + distance_travelled * tan(theta) - (acceleration * distance_travelled **2) / (2*((intial_velocity *cos(theta))**2))

#  printed the variable with strings before and after so it reads "projectile is 3.81 m
print('projectile is ' + str(a) + ' m')
print(a.__round__())

