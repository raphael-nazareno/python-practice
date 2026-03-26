# Day6 - 30 Days of Python

# Exercises: Level 1

# Create an empty tuple
tpl = ()

# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ("Michael", "Cera", "Jackson", "Jordan",)
sisters = ("Jessica", "Mauboy", "Alba", "Simpson")
siblings = brothers + sisters

# How many siblings do you have?
print(len(siblings))

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
siblings_list = list(siblings)
siblings_list.append("Mother1")
siblings_list.append("Mother2")

family_members = tuple(siblings_list)

# Exercises: Level 2

# Unpack siblings and parents from family_members
Michael, Cera, Jackson, Jordan, Jessica, Mauboy, Alba, Simpson, Mother1, Mother2 = family_members

print(Michael)
print(Cera)
print(Jackson)
print(Jordan)
print(Jessica)
print(Mauboy)
print(Alba)
print(Simpson)
print(Mother1)
print(Mother2)

# Create fruits, vegetables and animal products tuples. 
# Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ("Banana", "Apple", "Orange")
vegatables = ("Potatos", "Carrot", "Cucumber")
animal_products = ("Milk", "Eggs", "Cheese")

food_stuff_tp = fruits + vegatables + animal_products

# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle = len(food_stuff_lt) // 2
middle_item = food_stuff_lt[middle:middle+1]
print(middle_item)

# Slice out the first three items and the last three items from food_stuff_lt list
first_three = food_stuff_lt[0:3]
last_three = food_stuff_lt[-3:]
first_and_last = first_three + last_three
print(first_and_last)

# Delete the food_stuff_tp tuple completely
del food_stuff_tp

#Check if an item exists in tuple:
# Check if 'Estonia' is a nordic country
# Check if 'Iceland' is a nordic country

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print(f"{"Estonia" in nordic_countries} and {"Iceland" in nordic_countries}")