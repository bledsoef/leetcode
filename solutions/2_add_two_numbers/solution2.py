# carrying your 1s
# O(n)
from typing import Optional
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = ListNode(0)
        temp = head
        while l1 or l2 or carry:
            if l1 and l2:
                total = l1.val + l2.val + carry
                if total > 9:
                    carry = 1
                    total %= 10
                else:
                    carry = 0
                l1 = l1.next
                l2 = l2.next
            elif l1:
                total = l1.val + carry
                if total > 9:
                    carry = 1
                    total %= 10
                else:
                    carry = 0
                l1 = l1.next
            elif l2:
                total = l2.val + carry
                if total > 9:
                    carry = 1
                    total %= 10
                else:
                    carry = 0
                l2 = l2.next
            else:
                total = carry
                carry = 0

            temp.next = ListNode()
            temp = temp.next
            temp.val = total
        return head.next
                
