# semi optimal solution with sliding window and no set
# O(n^2)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # store the longest valid substring we have seen and the
        # right most pointer
        longest = 0
        r = 0

        for index, char in enumerate(s):
            # keep adding characters to the string if they are not in the 
            # current string and recompute the longest substring
            while r < len(s) and s[r] not in s[index:r]:
                r += 1
                longest = max(longest, len(s[index:r]))
            # whenever that case is not met move the left most pointer (index)
            # up by one
        return longest