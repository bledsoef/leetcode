# optimal solution with sliding window and a set
# O(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # store the length of the longest valid substring we have seen,
        # initialize the right most pointer and create a set to store 
        # all of the characters in our string currently
        longest = 0
        r = 0
        used = set()
        for index, char in enumerate(s):

            # keep adding characters to the string and set if they are not in the 
            # set and recompute the longest substring
            while r < len(s) and s[r] not in used:
                used.add(s[r])
                r += 1
                longest = max(longest, len(s[index:r]))
            # backtrack and remove characters as we adjust the left pointer (index)
            used.remove(char)
            
        return longest