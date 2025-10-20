from collections import defaultdict

"""
At first, we convert our list into a defaultdict to be able to store multiple values per key.
The dict is chosen because the lookup for keys is faster compared to lists.
Our keys are the values in our list, while our values are the corresponding indices.
Afterwards, we iterate through the items in our dict.
Based on our target and the current key, we compute a new key so that both keys together result in the target.
Then, we look for the newly computed key in our hashmap.
If we find the key and the key has a unique value, then we return the value from our original and the computed key.
If the key has two values, we return both values.
If the key is not found, then we continue with the next key.
Because there can only be one solution at most, every correctly computed key can only have two values at most.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Create the default dict based on the given list.
        nums_map = defaultdict(list)
        for idx, num in enumerate(nums):
            nums_map[num].append(idx)

        # Iterate through the dictionary and look for valid key pairs.
        for num, idx in nums_map.items():
            search_num = target - num
            search_idx = nums_map.get(search_num)
            if search_idx is None:
                continue
            if len(search_idx) == 1 and search_idx != idx:
                return [idx[0], search_idx[0]]
            if len(search_idx) == 2:
                return [idx[0], search_idx[1]]