# Day 11 - 30 Days of Python Challenge

# Exercises - Level 3

import keyword

# Write a function called is_prime, which checks if a number is prime.
def is_prime(num):
    for number in range(2,int(num**.5)+1):
        if num % number == 0:
            return False
        
    return True

print(is_prime(7))

# Write a functions which checks if all items are unique in the list.
def is_unique(lst):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] == lst[j]:
                return False
    return True

lst = [1,2,3,4]
print(is_unique(lst))


# Write a function which checks if all the items of the list are of the same data type.
def is_same_data_type(lst):
    return all(type(item) == type(lst[0]) for item in lst)

lst = [1, 2.2]
print(is_same_data_type(lst))

# OR 
def is_same_data_type(lst):
    first_type = type(lst[0])
    for item in lst:
        if type(item) != first_type:
            return False
    return True

lst = [1, 2.2]
print(is_same_data_type(lst))


# Write a function which check if provided variable is a valid python variable
def is_valid_variable(vari):
    return vari.isidentifier() and not keyword.iskeyword(vari)

print(is_valid_variable("while"))

# 