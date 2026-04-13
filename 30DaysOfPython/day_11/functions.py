# Day 11 - 30 Days of Python Challenge

# Exercises - Level 1
# Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_number(num1,num2):
    sum = num1 + num2
    return sum

print(add_two_number(3,4))

# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(radius):
    area = 3.14 * radius * radius
    return area

print(area_of_circle(4))

# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. 
# Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*nums):
    sum = 0
    for num in nums:
        if type(num) != int:
            print("Please only enter numbers")
            break
        else:
            sum += num
    return sum

print(add_all_nums(1,2,3,4,5))

# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. 
# Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_farenheit(celsius_temp):
    farenheit_temp = (celsius_temp * (9/5)) + 32
    return farenheit_temp

print(convert_celsius_to_farenheit(20))

# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
season_dict = { "Autumn":["March", "April","May"],
                "Winter":["June", "July", "August"],
                "Spring":["September", "October", "November"],
                "Summer":["December","January","February"] }

def check_season(month):
    for season in season_dict:
        if month in season_dict[season]:
            season_of_month = season
            print(f"{month} is in {season_of_month}!")

check_season("March")

# Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(point1, point2):
        slope = ((point1[1]) - point2[1]) / ((point1[0]) - (point2[0]))
        return slope

print(calculate_slope([1,1],[7,9]))


# Quadratic equation is calculated as follows: ax²+bx+c=0. 
# Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
def solve_quadratic_eqn(a,b,c):
    solution1 = (-b + (((b**2)-(4*a*c))**0.5)) / (2*a)
    solution2 = (-b - (((b**2)-(4*a*c))**0.5)) / (2*a)

    return solution1, solution2
    
print(solve_quadratic_eqn(a=2, b=4, c=1))


# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(lst):
    for item in lst:
        print(item)

print_list([3,4,5,6,7])


# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops)
def reverse_list1(lst):
    return lst[::-1]

print(reverse_list1([2,3,4,5,6]))

def reverse_list(array):
    reversed_array = []
    for item in array:
        reversed_array.insert(0,item)
    return reversed_array

print(reverse_list([2,3,4,5,6]))


# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalise_list_items(lst):
    newlst=[]
    for item in lst:
        item = item.upper()
        newlst.append(item)
    return newlst

print(capitalise_list_items(["hello","minecraft","a","b","c"]))

# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
food_stuff = ["Tomato", "Potato"]
def add_item(lst, item):
    lst.append(item)
    return lst

print(add_item(food_stuff, "Grape"))

# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item(lst, item):
    lst.remove(item)
    return lst

print(remove_item(food_stuff, "Grape"))

# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(num):
    sum = 0
    for numbers in range(0,num+1):
        sum += numbers
    return sum

print(sum_of_numbers(5))
print(sum_of_numbers(10))
print(sum_of_numbers(100))

# Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(num):
    sum = 0
    for number in range(0,num+1):
        if number % 2 != 0:
            sum += number
    return sum

print(sum_of_odds(5))
print(sum_of_odds(10))
print(sum_of_odds(100))

# Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that range.
def sum_of_even(num):
    sum = 0
    for number in range(0,num+1):
        if number % 2 == 0:
            sum += number
    return sum

print(sum_of_even(5))
print(sum_of_even(10))
print(sum_of_even(15))


# 
        


