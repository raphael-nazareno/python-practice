# Calculate the value of y (y = x^2 + 6x + 9). Use different x values and figure out at what x value y is going to be 0.
x = 0

for x in range(-100, 100, 1):
    y_value = x**2 + 6*x + 9
    
    if y_value == 0:
        print("0 = x^2 + 6x + 9")
        print(y_value, " = (", x, ")^2 + 6(", x, ") + 9", sep="")
        print(y_value, "=", x**2, "+", 6*x, "+ 9")
        print(y_value, "=", x**2 + 6*x + 9)
        print("Therefore:")
        print("y is 0 when x is", x)
        
print()


# Find the length of 'python' and 'dragon' and make a falsy comparison statement

python_length = len("python")
dragon_length = len("dragon")

print("python > dragon:", python_length > dragon_length)
print("python = dragon:", python_length == dragon_length)
print("python < dragon:", python_length < dragon_length)
print()


# Use and operator to check if 'on' is found in both 'python' and 'dragon'
print("'on' is inside python and dragon?", 'on' in 'python' and 'on' in 'dragon') # Checking for 'on' string inside of 'python' and 'dragon'
print()


# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
is_jargon_in = 'jargon' in 'I hope this course is not full of jargon'

print("The word jargon is in this sentence:", is_jargon_in)
print()


# There is no 'on' in both dragon and python
is_on_not_in = 'on' not in "python" and 'on' not in 'dragon'

print("The word 'on' is not inside python and dragon?", is_on_not_in)
print()


# Find the length of the text python and convert the value to float and convert it to string
length_of_python = len('python')
python_float = float(length_of_python)
python_str = str(python_float)

print("What variable type is the variable 'python_str'?", type(python_str) )

# OR 

python_string = str(float(len('python')))

print(python_str, "is a", type(python_string))
print()


# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
num1 = 1

if num1 % 2 == 0:               # Modulus operator outputs the remainder of the division of two numbers
    print (num1, "is even!")    # If there is no remainder, the number is even else it's odd
else:
    print(num1, "is odd!")
print()


# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
is_equal = (7//3) == int(2.7)

print(is_equal)
print()

# Check if type of '10' is equal to type of 10
print(type(10) is type('10'))
print()

# Check if int('9.8') is equal to 10
# print(int('9.8') == 10 )   INVALID LITERAL FOR INT

# Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = int(input("Enter hours: "))
rate_per_hour = int(input("Enter rate per hour:"))

earnings = hours * rate_per_hour

print("Your weekly earnings:", earnings)
print()

# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years.
years = int(input("Enter number of years you have lived: "))

seconds = years * 365 * 24 * 60 * 60     # years * days * hours * minutes * seconds

print("You have lived for", seconds, "seconds")
print()


# Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125

a = 1
b = 0
for a in range (1,6,1):                  # When 'a' in larger or equal to 1, loop and increase by 1 until 'a' == 6.
    print()                              # Extra print() function so each loop of 'a' starts a new line.
    print(a, end=" ")                    # Output 'a' and end = " " ensures, it stays on the same line.
    for b in range(0, 4, 1 ):            # Each loop b increases by 1, 4 times.
        exponent = a ** b                # a is multipled by itself b times or a^b until b > 4.
        print(exponent, end=" ")         # end = " " ensures print() doesnt create a new line each loop but leaves a gap between each number with " ".
