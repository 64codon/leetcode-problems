# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def size():
            current = head
            count = 0
            while current is not None:
                count += 1
                current = current.next
            return count
        
        prev = None
        current = head
        step = size() - n
        while step:
            step -= 1
            prev = current
            current = current.next

        if prev is None:
            head = head.next
        elif current is None:
            prev.next = None
        else:
            prev.next = current.next

        return head