# optimal solution with dynamic programming
# O(n^2)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # store the longest valid substring we have seen
        string = ""

        # iterate over all characters and start an iteration from there
        for index, char in enumerate(s):
            l, r = index, index
            # move outwards from the current index as long as the string stays a
            # palindrome
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > len(string):
                    string = s[l:r+1]
                l -= 1
                r += 1

        # repeat the steps from the above the loop, but instead of strictly odd strings,
        # use strictly even strings
        for index, char in enumerate(s):
            l, r = index, index+1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > len(string):
                    string = s[l:r+1]
                l -= 1
                r += 1
            

        return string