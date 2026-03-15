a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

sum = a + b
difference = a - b
product = a * b

int_divide = a // b
float_divide = a / b

print("\nThe sum of " + str(a) + " and " + str(b) + " is:\n" + str(sum))
print("The difference of " + str(a) + " and " + str(b) + " is:\n" + str(difference))
print("The product of " + str(a) + " and " + str(b) + " is:\n" + str(product))
print("The integer division of " + str(a) + " and " + str(b) + " is:\n" + str(int_divide))
print("The float division of " + str(a) + " and " + str(b) + " is:\n" + str(float_divide))

print("")
# Loop to print squares of numbers from 0 to a-1
print("The square of all non zero integers less than " + str(a) + " is: ")
i=0
for i in range(0, a, 1):
    square = i * i
    print(str(i) + "^2 = " + str(square))

print("")
# Loop to print all non zero integers less than a
print("Each none zero integer less than " + str(a) + " is: ")
l = ""
for i in range(0, a+1):
    l += str(i) + ""
print(l)