# Day 2 - 30DaysOfPython Challenge


# Exercises - Level 1
print("Exercises - Level 1:\n")

# Declaring one variable per line.
first_name = "Raphael"
last_name = "Manalo"
full_name = "Raphael Julian Manalo"
country = "Australia"
city = "Melbourne"
age = "23"
year = "2026"
is_married = False
is_true = True
is_light_on = True

print(full_name)

# Declaring multiple values on one line.
first_name, last_name, full_name, = "Alessia", "Musco", "Alessia Musco"

print(full_name)


# Exercises: Level 2
print("\nExercises - Level 2:\n")

# Check data types of each variable
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print()

# Length of first_name
length = len(first_name)

print("The name", first_name, "consists of", length, "characters.")
print()

# Compare the length of your first name and your last name
longer_name = max(len(first_name), len(last_name)) # Calculates which argument has the highesst value
shorter_name = min(len(first_name), len(last_name)) # Calculates which argument has the lowest value

difference = int(longer_name) - int(shorter_name) # Difference between the highest and lowest value

print(difference, "characters is the difference between the first and last name.")
print()


num_one = 5                   # Declare 5 as num_one and 4 as num_two
num_two = 4

total = num_one + num_two           # Add num_one and num_two and assign the value to a variable total
diff = num_two - num_two            # Subtract num_two from num_one and assign the value to a variable diff
product = num_two * num_one         # Multiply num_two and num_one and assign the value to a variable product
division = num_one / num_two        # Divide num_one by num_two and assign the value to a variable division
remainder = num_two % num_one       # Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
exp =  num_one ** num_two           # Calculate num_one to the power of num_two and assign the value to a variable exp
floor_division = num_one // num_two # Find floor division of num_one by num_two and assign the value to a variable floor_division


# The radius of a circle is 30 meters.
radius = 30
area_of_circle = 3.14 * (radius**2)
circum_of_circle = 2 * 3.14 * radius

radius = int(input("Enter radius: "))
area_of_circle = 3.14 * (radius**2)
print("The area of a circle with a radius of", radius, "is", area_of_circle )
print()


# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names.
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
countryountry = input("What country are you from? ")
age = input("What is your age? ")

print(first_name, last_name, country, age)


