# Day 10 - 30 Days of Python Challenge

# Exercises: Level 2
# Use for loop to iterate from 0 to 100 and print the sum of all numbers.
sum = 0
for number in range(0,101,1):
    sum += number
print(f"The sum of all numbers is {sum}.")


# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
print()
sum_of_even = 0
sum_of_odd = 0
for number in range(0,101,1):
    if number % 2 == 0:
        sum_of_even += number
    else:
        sum_of_odd += number
 
print(f"The sum of all evens is {sum_of_even}. And the sum of all odds is {sum_of_odd}.")


# Exercises: Level 3
# Loop through the countries and extract all the countries containing the word land.


# This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
print()
fruits = ['banana', 'orange', 'mango', 'lemon']

for fruit in range(3,-1,-1):
   print(fruits[fruit],end =", " )


# Go to the data folder and use the countries_data.py file.
# What are the total number of languages in the data
# Find the ten most spoken languages from the data
# Find the 10 most populated countries in the world