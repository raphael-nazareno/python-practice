# Day 3 - 30DaysOfPython Challenge

age = int(23)                  # Declare your age as integer variable.
height_m = float(1.69)           # Declare your height as a float variable.
complex = complex(25j)         # Declare a variable that store a complex number.


# Write a script that prompts the user to enter base and height of the triangle 
# and calculate an area of this triangle (area = 0.5 x b x h).
base = int(input("Enter base: "))
height = int(input("Enter height: "))

area_of_triangle = 0.5 * base * height 

print("The area of the triangle is", area_of_triangle)
print()


# Write a script that prompts the user to enter side a, side b, and side c of the triangle. 
# Calculate the perimeter of the triangle (perimeter = a + b + c).
side_a = int(input("Enter side a: "))
side_b = int(input("Enter side b: "))
side_c = int(input("Enter side c: "))

perimeter_of_triangle = side_a + side_b + side_c

print("The perimeter of the triangle is", perimeter_of_triangle )
print()


# Get length and width of a rectangle using prompt. 
# Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width)).
length = int(input("Enter length: "))
width =  int(input("Enter width: "))

area_of_rectangle = length * width
perimeter_of_rectangle = 2 * (length + width)

print("The area of the rectangle is", area_of_rectangle)
print("The perimetere of the rectangle is", perimeter_of_rectangle )


# Get radius of a circle using prompt. 
# Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radius = int(input("Enter radius: "))

area_of_circle = 3.14 * (radius**2)
circum_of_circle = 2 * 3.14 * radius 

print("The area of the circle is", area_of_circle)
print("The circumference of the circle is", circum_of_circle)



