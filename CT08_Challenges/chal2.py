# Given an integer array `nums` and an integer `k`, return the total number of subarrays whose sum equals `k`.

# ### Example
# 1. nums = [1, 1, 1], k = 2
#    Output: 2 #[1,1], [1,1]

# 2. nums = [1, 2, 3], k = 3
#    Output: 2   # [1,2], [3]

# 3. nums = [1, -1, 0], k = 0
#    Output: 3   # [1,-1], [0], [1,-1,0]

nums = [1, -1, 0]
k = 0

out = 0

for num in range(len(nums)):
    x = nums[num]
    if x == k:
        out +=1
    for i in range(num, len(nums)):
        if i != len(nums)-1:
            x += nums[i+1]
        else:
            break
        if x == k:
            out +=1
        
print(out)
