# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        curr1 = l1
        curr2 = l2
        dummy = ListNode()
        curr = dummy
        carry = 0
        while curr1 or curr2:
            v1 = curr1.val if curr1 else 0
            v2 = curr2.val if curr2 else 0
            sm = v1 +v2+ carry    
            if  sm <= 9:
                    curr.next = ListNode(sm)
                    curr = curr.next
                    carry = 0
            else:
                carry = sm // 10
                r = sm % 10
                curr.next = ListNode(r)
                curr = curr.next
            if curr1:
                curr1 = curr1.next 
            if curr2:
                curr2= curr2.next 
        if carry != 0:
            curr.next = ListNode(carry)
        return dummy.next
        
        


        