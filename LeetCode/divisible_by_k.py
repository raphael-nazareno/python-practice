k = 6
operations = 0
i = 0

nums = [3,2] 

print(sum(nums)%k)           # the remainder of sum(nums)/k would be the operations needed to be divisible by k

for i in range (0,len(nums),1):      # when the index is empty or num[i] = 0, it moves on to the next index 
    while sum(nums) % k != 0:        # the script keep repeating until the sum of the array is divisible by k
            nums[i] = nums[i] - 1    # subtracts -1 from the array
            operations += 1

print(operations)


