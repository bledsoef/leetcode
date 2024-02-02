# carrying your 1s
# O(n)
from typing import Optional
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # initialize our carry variable which will hold our carry when necessary and create the head
        # of the linked list and a temp reference to it
        carry = 0
        head = ListNode(0)
        temp = head
        
        # iterate through while there are still numbers remaining in l1 or l2 or there is still some
        # carry left over
        while l1 or l2 or carry:
            if l1 and l2:
                # find the total of the two values plus our carry
                total = l1.val + l2.val + carry

                # make sure our value is one digit, if it isn't set carry = 1
                if total > 9:
                    carry = 1
                    total %= 10
                else:
                    carry = 0
                l1 = l1.next
                l2 = l2.next
            elif l1:
                # make sure our value is one digit, if it isn't set carry = 1
                total = l1.val + carry
                if total > 9:
                    carry = 1
                    total %= 10
                else:
                    carry = 0
                l1 = l1.next
            elif l2:
                # make sure our value is one digit, if it isn't set carry = 1
                total = l2.val + carry
                if total > 9:
                    carry = 1
                    total %= 10
                else:
                    carry = 0
                l2 = l2.next
            else:
                # if all we have is carry left add it to the list and then set it to 0
                # to end our while loop
                total = carry
                carry = 0
            # create a new node on our linked list
            temp.next = ListNode(total)
            temp = temp.next

        # return the first node in the list we carry about
        return head.next
                
