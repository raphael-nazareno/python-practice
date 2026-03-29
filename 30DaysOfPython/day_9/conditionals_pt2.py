# Exercises: Level 2

# Write a code which gives grade to students according to theirs scores:
'''
90-100, A
80-89, B
70-79, C
60-69, D
0-59, F
'''

score = int(input("Enter your score: "))

if score <= 59:
    grade = "F"
elif score <= 69:
    grade = "D"
elif score <= 79:
    grade = "C"
elif score <= 89:
    grade = "B"
else:
    grade = "A"

print(f"With a score of {score}, your final grade is {grade}.")
print()


# Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. 
# If the user input is: September, October or November, the season is Autumn. 
# December, January or February, the season is Winter. 
# March, April or May, the season is Spring 
# June, July or August, the season is Summer

seasons_of_months = {"Winter": ["December", "January", "February"],
                     "Autumn": ["September", "October", "November"],
                     "Spring": ["March", "April", "May"],
                     "Summer": ["June", "July", "August"]
}

user_month = input("Enter a month: ")

if user_month in seasons_of_months["Winter"]:
    print(f"The season in {user_month} is Winter!")
elif user_month in seasons_of_months["Autumn"]:
    print(f"The season in {user_month} is Autumn!")
elif user_month in seasons_of_months["Spring"]:
    print(f"The season in {user_month} is Spring!")
elif user_month in seasons_of_months["Summer"]:
    print(f"The season in {user_month} is Summer!")
print()


# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. 
# If the fruit exists print('That fruit already exist in the list')
fruits = ['banana', 'orange', 'mango', 'lemon']

user_fruit = input("Enter a fruit: ").lower()

if user_fruit in fruits:
    print(f"{user_fruit} already exists in the list!")
elif user_fruit not in fruits:
    fruits.append(user_fruit)
    print(f"{user_fruit} is added to the list!")
    print(fruits)


