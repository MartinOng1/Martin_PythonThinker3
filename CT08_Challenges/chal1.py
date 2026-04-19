"""
Given an integer array `nums` and an integer `k`, return the total number of subarrays whose sum equals `k`.

Example 1
- Input: `nums = [1, 1, 1]`, `k = 2`
- Output: `2` because [1, 1] (index 0 and 1) and [1,1] (index 1 and 2)
"""

"""
Given an array of strings `strs`, group the anagrams together. You can return the groups in any order.

Example
- Input: `["eat", "tea", "tan", "ate", "nat", "bat"]`
- Output: `[["eat","tea","ate"], ["tan","nat"], ["bat"]]` (order may vary)
"""

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
sortedstrs = {}
for word in strs:
    sortedstr = "".join(sorted(word))
    if sortedstr not in sortedstrs:
        sortedstrs[sortedstr] = [word]
    else:
        sortedstrs[sortedstr].append(word)

print(*sortedstrs.values(), sep='\n')