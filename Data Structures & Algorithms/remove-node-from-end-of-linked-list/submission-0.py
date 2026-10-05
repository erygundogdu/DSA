# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        curr = head
        prev = None
        cnt = 0
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        curr = prev
        prev_del = None
        cnt = 1

        while curr:
            if cnt == n:
                if prev_del is None:
                    prev = curr.next
                else:
                    prev_del.next = curr.next
                break

            prev_del = curr
            curr = curr.next
            cnt += 1
        curr = prev
        prev_n = None
        while curr:
            nxt = curr.next
            curr.next = prev_n
            prev_n = curr
            curr = nxt
        return prev_n

            



        