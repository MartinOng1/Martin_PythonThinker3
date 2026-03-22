# Given an integer array `nums` and an integer `target`, 
# return the indices of the two numbers such that they add up to `target`.

# You may assume exactly one valid answer exists, 
# and you may not use the same element twice.

# ### Example
# - Input: `nums = [2, 7, 11, 15]`, `target = 9`
# - Output: `[0, 1]`

nums = [2, 7, 11, 15]
target = 9

numdict = {}

def sumtarget(nums, target):
    for i in range(len(nums)):
        numdict[nums[i]] = i
        if target-nums[i] in numdict:
            return [numdict[target-nums[i]], numdict[nums[i]]]
print(sumtarget(nums, target))