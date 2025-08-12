# Day3 of 30 Days of Python
import math
age = 18
height = 5.833
complex = 5+2j

triangle_base = int(input("Enter the base of the triangle: "))
triangle_height = int(input("Enter the height of the triangle: "))
triange_area = 0.5*triangle_base*height

# print(triangle_area)

side_a = int(input("Enter side a: "))
side_b = int(input("Enter side b: "))
side_c = int(input("Enter side c: "))
triangle_perimeter = side_a+side_b+side_c

# print(triangle_perimeter)

rect_length = int(input("Enter the length of the rect: "))
rect_width = int(input("Enter the width of the rect: "))
rect_area = rect_length*rect_width
rect_perimeter = 2*(rect_length+rect_width)

circle_radius = float(input("enter radius: "))
circle_area = math.pi*(circle_radius**2)

# y = 2x-2

slope_line = 2
yintercept = -2

# (2,2), (6,10)

points = [(2,2),(6,10)]

slope_points = (points[1][1]-points[0][1])/(points[1][0]-points[0][0])

print(slope_line==slope_points)

print(len('Python')>len('dragon'))

print('on' in 'python' and 'on' in 'dragon')

print(int(9.8)==10)
