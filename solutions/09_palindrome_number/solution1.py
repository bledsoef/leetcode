# convert integer to string and reverse
# O(n)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # it can't be a palindrome if it is negative
        if x < 0:
            return False

        return str(x)[::-1] == str(x)