# brute force
# O(n^3)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # store the longest valid substring we have seen
        longest = 0

        # iterate over every possible substring
        for index1, char1 in enumerate(s):
            for index2, char2 in enumerate(s):
                if index2 >= index1:
                    # if every character is unique and it is longer than the previous longest
                    # we have seen, update the longest value
                    if len(set(s[index1:index2+1])) == len(s[index1:index2+1]):
                        longest = max(longest, len(s[index1:index2+1]))

        return longest

