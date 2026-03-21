arithemetic_operators = ["product", "sum", "difference", "quotient", "power"]
operator = {"product": "x", "sum": "+", "difference":"-", "quotient": "/", 
            "power":"^"
}

while True:
    a = int(input("Enter a number: " )) # Asks user to input a number and stores number as 'a'.
    if type(a) == int:
        print(f"You have entered: ({a})")
        break
    else:
        print("Error! Invalid input! Please enter a valid integer.")

while True:
    b = int(input("\nEnter another number: ")) # Asks user to input another number and stores a 'b' .
    if type(b) == int:
        print(f"You have entered: ({a}) and ({b})")
        break
    else:
        print("Error! Invalid input! Please enter a valid integer.")

while True:
    operation = input("\nWhich do you want to calculate? (product, sum, difference, quotient or power?)\n").strip() # Asks user to choose which operation to perform on their previous inputs.
    if operation in arithemetic_operators:
        break
    else:
        print("Error! Invalid input! Please enter a valid operation.")

while True:
    confirmation = input(f"\nYou want to calculate {a}{operator[operation]}{b}. Confirm (y/n): ")
    if confirmation == 'y':
        break
    elif confirmation == 'n':
        print("kill yourself")
        break
    else:
        print("Error! Invalid input! Please enter either y or n.")




# Equations for each type of operation assigned as a a variable.
product = a * b
sum = a + b
difference = a - b
quotient = a / b
power = a ** b

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
elif operation == "power":
    calulation = power

# Prints out the solution of the User's inputted numbers with thier operation of choice.
print(f"\n{a}{operator[operation]}{b} = {calulation}")
