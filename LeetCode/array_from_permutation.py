nums = [5,0,1,2,3,4]
ans = nums.copy()

for i in range (0,len(nums),1):
    ans[i] = nums[nums[i]]
print(ans)
    
    
