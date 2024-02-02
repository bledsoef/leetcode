# slightly less brute force
# time complexity: O(nlogn)
from typing import List

class Solution:
    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        # create a list coupling all values with the index they occur
        # in the original list
        pairs = []
        for index, value in enumerate(nums):
            pairs.append((value, index))
        
        # sort the list by the values using a lambda function
        pairs.sort(key=lambda x: x[1])

        # iterate over the sorted list with two pointers moving towards each other
        f, l = 0, len(nums)-1
        while f <= l:
            smaller_value, larger_value = pairs[f][0], pairs[l][0]
            f_index, l_index = pairs[f][1], pairs[l][1]
            total = smaller_value + larger_value
            # if our two values equal the target, return the indexes at which they occur
            # otherwise, if the total is less than the target, move our f pointer to the right
            # to increase the sum. If it is more, move our l pointer back one to decrease the sum.
            if total == target:
                return [f_index, l_index]
            elif total < target:
                f += 1
            else:
                l -= 1
        
    
print(Solution.twoSum([2, 7, 11, 15], 9))