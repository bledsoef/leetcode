# easiest optimal solution
# O(n)

class Solution:
    def reverse(self, x: int) -> int:
        # flip around the integer
        list_x = str(abs(x))[::-1]
        res = int("".join(list_x))
        # if it was negative make the integer negative again
        if x < 0:
            res *= -1
        
        # return the integer if it is within the given constraints
        # otherwise, return 0
        return res if (-2**31) < res and res < (2**31)-1 else 0