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
print()


# Get radius of a circle using prompt. 
# Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radius = int(input("Enter radius: "))

area_of_circle = 3.14 * (radius**2)
circum_of_circle = 2 * 3.14 * radius 

print("The area of the circle is", area_of_circle)
print("The circumference of the circle is", circum_of_circle)
print()


# Calculate the slope, x-intercept and y-intercept of y = 2x -2
x1 = 1
x2 = 2
y1 = 2*(1) - 2
y2 = 2*(2) - 2

slope = (y2-y1)/(x2-x1)

x_intercept = 2 / 2
y_intercept = -2

print("The slope of the y = 2x - 2 is", slope)
print("The x-intercept is", x_intercept, "and the y-intercept is", y_intercept)
print()


# Slope is (m = y2-y1 / x2-x2). Find the slope and Euclidean distance between 
# point (2, 2) and point (6,10)

point_one = [2,2]
point_two = [6,10]

y1 = point_one[1]
y2 = point_two[1]
x1 = point_one[0]
x2 = point_two[0]

slope_one = (y2-y1)/(x2-x1)
euclidean_distance = ((x2-x1)**2 + (y2-y1)**2)**.5

print("The slope between the points (2, 2) and (6, 10) is", slope_one)
print("The Euclidean Distance between the points (2, 2) and (6, 10) is", round(euclidean_distance, 2))
print()


# Compare the previous two slopes
print("first slope:", slope, "> second slope: ", slope_one , ":", slope > slope_one)
print("first slope:", slope, "< second slope: ", slope_one , ":", slope < slope_one)
print("first slope:", slope, "!= second slope: ", slope_one , ":", slope != slope_one)
print("first slope:", slope, "== second slope: ", slope_one , ":", slope == slope_one)

