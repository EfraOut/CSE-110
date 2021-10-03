"""
Author: Efrain Gomez Fajardo
Teacher: Comeau, Luc
Purpose: Find the area of different shapes
"""

import math

square_lenght = int(input('What is the length of the square in cm? '))
square_area = square_lenght ** 2
print(f'The area of the square is {square_area} cm2\nThe area of the square is {square_area / 10000} m2')
rectangule_length = int(input('What is the length of the rectangule in cm? '))
rectangule_width = int(input('What is the width of the rectangle in cm? '))
rectangule_area = rectangule_length * rectangule_width
print(f'The area of the rectangule is {rectangule_area} cm2\nThe area of the rectangule is {rectangule_area / 10000} m2')
circule_radius = int(input('What is the radius of the circle in cm? '))
circule_area = math.pi * circule_radius
print(f'The area of the circule is {circule_area:.2f} cm2 \nThe area of the circule is {circule_radius / 10000} m2')

# Asking for a single value
value = int(input('With one value, I can calculate the area for square, and circle, and the volume of a cube and sphere: '))
print(f'The area of the square is {value ** 2}\nThe area of the circule is {math.pi * value:.2f}\nThe volume of the cube is {value ** 3}\nThe volume os the shpere is {4/3 * math.pi * value ** 3}')