a = int(input("\nEnter a number: "))
# Prints the integers from 0 to a in ascending order with no gap between outputs.
# Default is new line, end = " " creates one space, end = "" creates no space between outputs.
print("\nAll non zero integers from 0 to", a, "are:")
for i in range(1, a, + 1):
    print(i, end = " ")

# Prints the product of 'a' multiplied by 'i' as long as 'i' is smaller that 13.
# Basically multiplies A by 0 - 13 and outputs in a format similar to primary school times tables.
# a x 0 = 0
# a x 1 = 1a
# ............
print("\nThe", a, "times table up to 12 are:")
for i in range (0, 13, + 1):
    product = i * a
    print(a, "x", i, "=", product )


# The sep parameter, indicates what value/s separate each argument in the print functions.
# Default is a singular space. In this instance it's sep = " + ", which signifies that
# each arguement is separated by a plus symbol with a space on either side.
sum = a * 6 #a+a+a+a+a+a
print(a, a, a, a, a, a, sep = " + ", end =" ")
print("=", sum)




