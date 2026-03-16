name = input("What is your name? ")

# strip() is a function (method) of str that removes whitespace from a str.
# # capitalize() is a function (method) of str that capitlises the start of a str. Use .title() for capitalisation of all words in a str
name = name.strip().capitalize()

# Combines all lines of code above into one.
name = input("What is your name? ").strip().capitalize

# The end parameter prevents the print function from moving over to the next line .
# The space in the end parameter indicate the space between the print "Hello," function and the next print statment.
# This method compared to the + way of 'adding' varibles to strings, doesn't require the space at the end of the string 
# for there to be a gap between variables in the output.

print ("Hello,", end=" ")
print (name)

# Print function using f string
print(f"Hello, {name}")