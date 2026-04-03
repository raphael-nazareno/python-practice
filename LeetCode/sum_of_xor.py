nums = [1,3]

'''
Whenever you see:
"sum over all subsets”
involving XOR / OR / AND
Ask:
“Can I count contributions per bit instead of generating subsets?”
'''
nums = [1,3]
or_total = 0
n = len(nums)

for num in nums:
    or_total |= num

sum_of_subset_xor = or_total * (2**(n-1))

print(sum_of_subset_xor)