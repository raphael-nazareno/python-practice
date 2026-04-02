# Day 10 - 30 Days of Python Challenge

# Exercises: Level 1
# Iterate 0 to 10 using for loop, do the same using while loop.
numbers = [0,1,2,3,4,5,6,7,8,9,10]
print("0-10 with for loop:")
for number in numbers:
    print(number, end=" ")

print("\n0-10 with while loop:",)
count = 0
while count < 11:
    print(count, end=" ")
    count = count + 1


# Iterate 0 to 10 using for loop, do the same using while loop.
print("\n10-0 with for loop:")
for numbers in range(10,-1,-1):
    print(numbers, end= " ")

print("\n10-0 with while loop:")
count = 10
while count > -1:
    print(count, end=" ")
    count = count -1


# Write a loop that makes seven calls to print(), so we get on the output the following triangle:
  #
  ##
  ###
  ####
  #####
  ######
  #######

print("\nHash triangle:")
count = 0
hash_text = "#"
while count < 8:
    print(hash_text)
    hash_text = hash_text + "#"
    count = count + 1


# Use nested loops to create the following:
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #

for hash_row in range(8):
    for hash_column in range(8):
        print("#",end =" ")
    print()
        


print()

# Goal: Alternate symbols in a grid
# Requirements:

# Grid size: 8 × 8
# Use two symbols: # and .
# Alternate horizontally AND vertically
# First row starts with #
# Pattern must continue correctly across all rows

# Solution 1
checkers = ["#","."]

for row in range(8):
    for column in range(4):
        for square in checkers:
            print(square,end=" ")
    print()
    checkers.reverse()
    
# Solution 2
print()
for row in range(8):
    for column in range(8):
        if (row + column) % 2 == 0:
            print ("#", end =" ")
        else:
            print(".",end =" ")
    
    print()

# Solution 3
print()

symbols = ["#","."]

rows = 8
cols = 8

for row in range(rows):
    for col in range(cols):
        print(symbols[(row + col) % 2],end =" ")
    print()


# Print the following pattern:
''' 
0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100
'''
print()

mutiple1 = 0
mutiple2 = 0

for timetable in range(11):
    print(f"{mutiple1} x {mutiple2} = {mutiple1 * mutiple2}")
    mutiple1 += 1
    mutiple2 += 1



# Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
print()

lst = ['Python', 'Numpy','Pandas','Django', 'Flask']

for item in lst:
    print(item)


# Use for loop to iterate from 0 to 100 and print only even numbers
print()
for even in range(0,101,2):
    print(even,end =" ")

# Use for loop to iterate from 0 to 100 and print only odd numbers
print()
for odd in range(1,101,2):
    print(odd,end =" ")

    
    


