arr = [2,3,6,6,5]

new_arr = list(set(arr)) # set removes any duplicates
new_arr.remove(max(new_arr))

print(max(new_arr))