# brute force
# O(n^3)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # store the longest valid palindrome we have seen
        longest = 0
        string = ""

        # iterate over every possible substring
        for index1, char1 in enumerate(s):
            for index2, char2 in enumerate(s):
                if index2 >= index1:
                    # if every the string is a palindrome and it is longer than the previous longest
                    # we have seen, update the longest value
                    if s[index1:index2+1][:] == s[index1:index2+1][::-1]:
                        if longest < len(s[index1:index2+1]):
                            string = s[index1:index2+1]
                        longest = max(longest, len(s[index1:index2+1]))

        return string