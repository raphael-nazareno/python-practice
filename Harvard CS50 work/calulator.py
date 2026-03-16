# Asks user to input a number and stores number as 'a'.
a = int(input("Enter a number: " ))
print("You have entered: (", a, ")")

# Asks user to input another number and stores a 'b' .
b = int(input("\nEnter another number: "))
print("You have entered: (", a, "and", b, ")")

# Asks user to choose which operation to perform on their previous inputs.
operation = input("\nWhich do you want to calculate? \n(product, sum, difference or quotient) ").strip()

# Equations for each type of operation assigned as a a variable.
product = a * b
sum = a + b
difference = a - b
quotient = a / b

# Initialised the 'calulation' variable so the program has a basis of what it should be.
calulation = 0

# Conditions for the program evaluate the equation depending on the the user's choice of operation.
if operation == "product":
    calulation = product
elif operation == "sum":
    calulation = sum
elif operation == "difference":
    calulation = difference
elif operation == "quotient":
    calulation = quotient

# Prints out the solution of the User's inputted numbers with thier operation of choice.
print("\nThe", operation, "of", a, "and", b, "is", calulation, "!")
