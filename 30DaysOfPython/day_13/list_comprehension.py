# Day 13 - 30 Days of Python Challenge

# Exercises - Level 1
# Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

negatives_and_zero = [number for number in numbers if number <= 0]
print(negatives_and_zero)

# Flatten the following list of lists of lists to a one dimensional list :
list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

one_list = [number for row in list_of_lists for number in row]
print(one_list)

# Using list comprehension create the following list of tuples:
'''
[(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)]
'''
exponent_table = [(i,) + tuple(i**a for a in range(6)) for i in range(11)]
print(exponent_table)

# Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]

result = [[country.upper(),country[0:3].upper(),city.upper()] 
          for row in countries
          for country,city in row]

print(result)


# Change the following list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

output = [{"country": country.upper(), "city": city.upper()} 
          for row in countries 
          for country,city in row]

print(output)

# Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Homer', 'Simpson')], [('Tyson', 'Ngo')]]

output = [" ".join(pair) for row in names for pair in row]

print(output)

# Write a lambda function which can solve a slope or y-intercept of linear functions.
slope = lambda x1,y1,x2,y2 : (y2-y1)/(x2-x1)
print(slope(7,5,3,2))

y_intercept = lambda gradient,x1,y1: y1 - gradient*x1
print(f"(0, {y_intercept(2,7,5)})")

