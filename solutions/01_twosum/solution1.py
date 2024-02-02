# brute force
# time complexity: O(n^2)
from typing import List

class Solution:
    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        # iterate over every possible combination
        for index1, num1 in enumerate(nums):
            for index2, num2 in enumerate(nums):
                if index2 > index1:
                    if num1 + num2 == target:
                        return [index1, index2]

print(Solution.twoSum([2, 7, 11, 15], 9))