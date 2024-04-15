import cmath as np
import numpy as cp
import matplotlib.pyplot as plt
#inputs for the a,b,c coefficients
a = float(input('Enter coefficient a: '))
b = float(input('Enter coefficient b: '))
c = float(input('Enter coefficient c: '))
#Calculates the discriminant
k = b ** 2 - 4 * a * c
A, B, C = complex(a), complex(b), complex(c)
# Roots of the Quadratic to 3 decimal places.
ans = (-B - np.sqrt(B ** 2 - 4 * A * C)) / (2 * A)
ans2 = (-B + np.sqrt(B ** 2 - 4 * A * C)) / (2 * A)
print(f'{ans:.3f}')
print(f'{ans2:.3f}')
#Tells that us if there are complex solutions
if k < 0:
    print('No real solutions')
#Range for which the Quadratic function is graphed
if k >= 0:
    plt.ylim(-50, 50)
plt.xlim(-30, 30)
#Tells us wether a quadratics vertex is it's max or min based on the sign of the 'a' coefficient 
if a > 0:
    print('Minimum')
else:
    print('Maximum')
# Calculates the vertex x coordinate
V = -B / (2 * A)
#Calculates the y coordinate of the vertex using the quadratic equation and the x coordinate.
D = A * V ** 2 + B * V + C
print('Vertex:')
print(V,D)

def f(z):
    return A * z ** 2 + B * z + C
#The given range for which the function is calculated for and the scale at which it is calculated. 
x = cp.arange(-100, 100, 0.001)
plt.plot(x, f(x),label= 'Parabola')
plt.grid()

if k >= 0:
 #Verical line at x = 0 i.e  the y-axis
 plt.axvline(x=0, c="black", label="y-axis")
#Horziontal line at y = 0 i.e the x-axis
plt.axhline(y=0, c="blue", label="x-axis")

plt.legend()

plt.show()


