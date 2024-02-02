# more efficient but worse practice
# O(n)
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # create the string to hold the values in l1
        first = ""
        while l1:
            first = str(l1.val) + first
            l1 = l1.next

        # create the string to hold the values in l2
        second = ""
        while l2:
            second = str(l2.val) + second
            l2 = l2.next

        # get the total result and initialize our new list
        res = str(int(first) + int(second))
        head = ListNode()
        temp = head

        # iterate through our result in reverse order to create the result
        # list
        for i in res[::-1]:
            temp.next = ListNode(int(i))
            temp = temp.next

        # return the first node we care about
        return head.next