# Day 5 - 30 Days of Python Challenge

# Exercises - Level 2

# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
ages.sort()
print(f"{ages}, {min(ages)}, {max(ages)}")

# Add the min age and the max age again to the list
ages.append(min(ages))
ages.append(max(ages))
print(ages)

# Find the median age (one middle item or two middle items divided by two)
ages.sort()
length = len(ages)
if length % 2 == 0:
    median = (ages[int(length / 2)] + ages [int(length / 2) + 1]) / 2
elif length % 2 != 0:
    median = (ages[int(length // 2)])

print(median)

# Find the average age (sum of all items divided by their number )
average = sum(ages) / length
print(average)

# Find the range of the ages (max minus min)
range = max(ages) - min(ages)
print(range)

# Compare the value of (min - average) and (max - average), use abs() method
min_deviation = abs(min(ages) - average)
max_deviation = abs(max(ages) - average)

print(f"{min_deviation}, {max_deviation}")

