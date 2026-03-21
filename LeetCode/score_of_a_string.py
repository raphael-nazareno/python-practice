s = "zaz"

length = len(s)
my_dict = {x: s[x] for x in range(length)}

keys = list(my_dict.keys())

absolute = 0

for i in range(len(keys) - 1):
    current_key = keys[i]
    next_key = keys[i + 1]
    differ = absolute + abs(ord(my_dict[current_key]) - ord(my_dict[next_key])) #ord() Converts string into ASCII
    absolute = differ

print(absolute)

    
    



    


    



