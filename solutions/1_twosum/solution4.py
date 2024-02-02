# one pass
# time complexity: O(n)
from typing import List

class Solution:
    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        # create a hashmap that will map the value (key) to the index (value)
        hashmap = {}

        # while iterating over each number, if its counterpart exists in the dict
        # return the number and its counterpart, otherwise, add the number to the hashmap
        for index, num in enumerate(nums):
            if target-num in hashmap:
                return [hashmap[target-num], index]
            else:
                hashmap[num] = index

print(Solution.twoSum([2, 7, 11, 15], 9))