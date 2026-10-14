# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
            
        def reverse(node):
            curr = node
            prev = None
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

        slow = head
        if not head or not head.next:
            return
        fast = slow.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        end = reverse(mid)

        c1 = head
        c2 = end
        while c1 and c2:
            nxt1 = c1.next
            nxt2 = c2.next
            c1.next  = c2
            if nxt1 is None:
                break
            c2.next = nxt1
            c1 = nxt1
            c2 = nxt2
            









        