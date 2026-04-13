# Day 11 - 30 Days of Python Challenge

# Exercises - Level 2
# Declare a function named evens_and_odds . 
# It takes a positive integer as parameter and it counts number of evens and odds in the number.

def evens_and_odds(num):
    evens = 0
    odds = 0
    for number in range(0,num+1):
        if number % 2 !=0:
            odds += 1
        else:
            evens += 1
    return odds, evens

print(evens_and_odds(100))

# Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(num):
    fact = 1
    for number in range(1, num+1):
        fact *= number
        print(fact)
    return fact

print(factorial(5))

# Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(para):
    if not para:
        return True
    else:
        return False
    
mango = []
print(f"The list mango is empty: {is_empty(mango)}")

# Write different functions which take lists. 
# They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
lst = [1,1,2,2,3,3,3,4,4,5,5,7,7,7]

# Mean
def calculate_mean(list_of_nums):
    sum = 0
    for number in list_of_nums:
        sum += number
    mean = sum / len(list_of_nums)
    return mean

print(calculate_mean(lst))

# Median
def calculate_median(list_of_nums):
    nums = sorted(list_of_nums)
    length = len(nums)

    if length % 2 == 0:
        return (nums[(length//2)] + nums[length//2 - 1]) / 2
    else:
        return nums[length//2]
    
print(calculate_median(lst))

# Mode
def calculate_mode(list_of_nums):
    num_total = {}
    for number in list_of_nums:
        if number not in num_total:
            num_total[number] = 1
        else:
            num_total[number] += 1
    
    mode = None
    highest_count = 0

    for number, count in num_total.items():
        if count > highest_count:
            highest_count = count
            mode = number
    
    return mode

lst = [1,1,2,4]
print(calculate_mode(lst))

# Range
def calculate_range(list_of_nums):
    return max(list_of_nums) - min(list_of_nums)

lst = [1,1,2,4]
print(calculate_range(lst))

# Variance
def calculate_variance(list_of_nums):
    sum_of_squares = 0
    mean = calculate_mean(list_of_nums) 

    for number in list_of_nums:
        sum_of_squares += (number - mean)**2

    return sum_of_squares / len(list_of_nums)
    
lst = [1,2,3,4,5]
print(calculate_variance(lst))

# Standard Deviation
def calculate_std(list_of_nums):
    return (calculate_variance(list_of_nums))**0.5

lst = [1,2,3,4,5]
print(calculate_std(lst))

# Write a function called greet which takes a default argument, name. 
# If no argument is supplied it should print "Hello, Guest!", otherwise it should greet the person by name.
def greet(name=None):
    if not name:
        print("Hello, Guest!")
    else:
        print(f"Hello, {name}!")

greet()
greet("Raphael")

# Create a function called show_args to take an arbitrary number of named arguments and print their names and values
def show_args(**args):
    items = list(args.items())

    print("Received: ",end="")
    for i, (k, v) in enumerate(items):
        if i == len(items) - 1:
            print(f"{k}: {v}")
        else:
            print(f"{k}: {v}, ",end="")
        
show_args(name="Alice", age=30, city="New York")
show_args(name="Bob", pet="Fluffy, the bunny")

# OR

def show_args(**args):
    print("Received: " + ", ".join(f"{k}: {v}" for k, v in args.items()) )

show_args(name="Alice", age=30, city="New York")
show_args(name="Bob", pet="Fluffy, the bunny")


