order = [1,4,5,3,2]
friends = [2,5]
new_order = []
newer_order = []

new_order = [item for item in order if item in friends]
# creates new list, assigns all values in 'order' with 'item' and checks whether the value of an 'item'
# is in friends and adds it to the new list.    
print(new_order)


for i in order:
    if i in friends:
        newer_order.append(i)

print(newer_order)