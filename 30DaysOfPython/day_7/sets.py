# Day 7 - 30 Days of Python

# Exercises: Level 1

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

# Find the length of the set it_companies
print(len(it_companies))

# Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

# Insert multiple IT companies at once to the set it_companies
it_companies.update(['Meta', 'Canva', 'Atlassian'])
print(it_companies)

# Remove one of the companies from the set it_companies
it_companies.remove('Twitter')
print(it_companies)

# What is the difference between remove and discard
# Remove() will raise errors with the specified item in not found in the set, whereas discard() will not.
# Both methods function in basically the same way, however.

# Exercises: Level 2

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# Join A and B
C = A.union(B)
print(C)

# Find A intersection B
print(A.intersection(B))

# Is A subset of B
print(A.issubset(B))

# Are A and B disjoint sets
print(A.isdisjoint(B))

# Join A with B and B with A
print(f'Before: A:{A} and B:{B}')

A.update(B)
B.update(A)

print(f'After: A:{A} and B:{B}')

# What is the symmetric difference between A and B
sym_diff = A.symmetric_difference(B) # nothing since we joined both lists with the other
print(sym_diff) 

# Delete the sets completely
del A
del B


# Exercises: Level 3
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set = set(age)
set_length = len(age_set)
list_length = len(age)

if set_length > list_length:
    print(f"The set is {set_length} characters long and the list is {list_length} characters long so the set is longer!")
elif list_length > set_length:
    print(f"The list is {list_length} characters long and the set is {set_length} characters long so the list is longer!")


# Explain the difference between the following data types: string, list, tuple and set
# A string is just a collection of characters that represent anything in code, whether is be a word or number, a place, an animal
# A String is a string of character that represent something in the real world.

# A list is a collection of items that are unordered and random. The items can range from strings, ints etc, lists can be changed, modified and can have repeated items.
# A tuple is basically the same as a list but cannot be changed. In order to change or modify a tuple, one must first convert it to a list then convert it back to a tuple.
# A set is a collection or storage of items and acts a point of reference for items in a system. It doesn't represent the items themselvess but represents the existance 
# of items. With this in mind, a set unlike a list or tuple CANNOT have any duplicate items but can however be changes, modified and whatever the user sees fit.

# I am a teacher and I love to inspire and teach people. 
# How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = "I am a teacher and I love to inspire and teach people."
seperate_words = sentence.split(" ")
set_of_words = set(seperate_words)

print(set_of_words)
print(f"There are {len(set_of_words)} unique words in this sentence: '{sentence}'")


