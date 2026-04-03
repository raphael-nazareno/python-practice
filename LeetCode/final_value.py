operations = ["--X","X++","X++"]
x = 0

for operation in operations:
    if operation == "--X" or operation == "X--":
        x -= 1
    elif operation == "++X" or operation == "X++":
        x += 1

print(x)