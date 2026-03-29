# Day 9 - 30 Days Of Python Challenge

# Exercises: Level 1

# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. 
# If below 18 give feedback to wait for the missing amount of years. Output:
# Enter your age: 30
# You are old enough to learn to drive.
# Output:
# Enter your age: 15
# You need 3 more years to learn to drive.

age = int(input("Enter your age: "))

if age >= 18:
    print("You are old enough to drive.")
elif age < 18:
    missing_years = 18 - age
    print(f"You need {missing_years} more years to learn to drive,")
print()


# Compare the values of my_age and your_age using if … else. 
# Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. 
# You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, 
# and a custom text if my_age = your_age. Output:
# Enter your age: 30
# You are 5 years older than me.

my_age = 23

your_age = int(input("Enter your age: "))



if your_age == my_age:
    print("OMG TWINSIES")

elif your_age > my_age:
    age_gap = your_age - my_age

    if age_gap <= 1:
        print(f"You are {age_gap} year older than me")
    else:
        print(f"You are {age_gap} years older than me")    

elif your_age < my_age:
    age_gap = my_age - your_age
    
    if age_gap <= 1:
        print(f"You are {age_gap} year younger than me")
    else:
        print(f"You are {age_gap} years younger than me")  
print()

# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, 
# if a is less b return a is smaller than b, else a is equal to b. Output:
# Enter number one: 4
# Enter number two: 3
# 4 is greater than 3

a = int(input("Enter number one: "))
b = int(input("Enter number two: "))
    
if a > b:
    print("A is greater than B.")
elif b > a:
    print("B is greater than A.")
else:
    print("A and B are equal.")
print()




