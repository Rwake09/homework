from math import pi, tan, cos

g = 9.81
v0 = 44
theta = 80 * pi/180
x = 0.5
y0 = 1

# y = y0 + x*tan(theta) - (g*x**2)/(2*((v0 *cos(theta))**2))



y = 1 + 0.5*tan(theta) - (9.81*0.5**2)/(2*(44*cos(theta))**2)

print('height', y, 'm')
print(theta)