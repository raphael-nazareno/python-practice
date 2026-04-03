nums = [1,3,5,7]

sum_of_nums = 0
for index, num in enumerate(nums):
    if index % 2 == 0:
        sum_of_nums += num
    else:
        sum_of_nums -= num

print(sum)

sum = 0
for index in range(len(nums)):
    if index % 2 == 0:
        sum += nums[index]
    elif index % 2 !=0:
        sum -= nums[index]
print(sum)
        
