"""
Author: Efrain Gomez Fajardo
Teacher: Comeau, Luc
Purpose: Find the area of different shapes
"""

import math

square_length = int(input('What is the length of the square in cm? '))
square_area = square_length ** 2
print(f'The area of the square is {square_area} cm2\n\
The area of the square is {square_area / 10000} m2')
rectangle_length = int(input("What is the length of the rectangle" +
"in cm? "))
rectangle_width = int(input('What is the width of the rectangle' +
'in cm? '))
rectangle_area = rectangle_length * rectangle_width
print(f'The area of the rectangle is {rectangle_area} cm2\n' +
f'The area of the rectangle is {rectangle_area / 10000} m2')
circle_radius = int(input('What is the radius of the circle in cm? '))
circle_area = math.pi * circle_radius
print(f'The area of the circle is {circle_area:.2f} cm2 \n' +
f'The area of the circle is {circle_radius / 10000} m2')

# Asking for a single value
value = int(input('With one value, I can calculate the area' + 
'for square, and circle, and the volume of a cube and sphere: '))
print(f'The area of the square is {value ** 2}\n' +
f'The area of the circle is {math.pi * value:.2f}\n' +
f'The volume of the cube is {value ** 3}\n' +
f'The volume os the sphere is {4/3 * math.pi * value ** 3}')