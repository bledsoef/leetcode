# two pass
# time complexity: O(n)
from typing import List

class Solution:
    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        # create a hashmap that maps the value (key) to the index (value)
        hashmap = {}
        for index, num in enumerate(nums):
            hashmap[num] = index
        
        # iterate over each number in nums, if its counterpart (target-num)
        # exists in the dictionary, return the index of both the number and its counterpart
        for num in nums:
            if target-num in hashmap:
                return [hashmap[target-num], hashmap[num]]

print(Solution.twoSum([2, 7, 11, 15], 9))