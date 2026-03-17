# Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125

a = 1
b = 0
for a in range (1,6,1):                  # When 'a' in larger or equal to 1, loop and increase by 1 until 'a' == 6.
    print()                              # Extra print() function so each loop of 'a' starts a new line.
    print(a, end=" ")                    # Output 'a' and end = " " ensures, it stays on the same line.
    for b in range(0, 4, 1 ):            # Each loop b increases by 1, 4 times.
        exponent = a ** b                # a is multipled by itself b times or a^b until b > 4.
        print(exponent, end=" ")         # end = " " ensures print() doesnt create a new line each loop but leaves a gap between each number with " ".
