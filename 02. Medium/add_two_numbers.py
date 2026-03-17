from typing import ListNode
from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val -> The head of the node
#         self.next = next -> The end of the node
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Instantialize an anchor node for a forward filling order
        anchor_node = ListNode()
        # Share anchor_node with another variable
        # This allows for us to initially mutate the shared object and drop it later
        current = anchor_node
        # Initialize the remainder to carry over
        remainder = 0
        while l1 is not None or l2 is not None:
        # Check if either l1 or l2 is None
        # If so, return zero (a mathematical equivalent of None)
            if l1 is not None:
                val1 = l1.val
            else:
                val1 = 0
            if l2 is not None:
                val2 = l2.val
            else:
                val2 = 0
            # Calculate the sum of the items in each node
            # Account for the addition of a previous remainder
            node_sum = (val1 + val2) + remainder
            # Ensure it is set to the unit place
            item = node_sum % 10
            # Calculate the remainder to be carried over
            remainder = node_sum // 10
            # Instantialize a new node
            #    Notice how the end of the anchor changes from None to the newly created node
            current.next = ListNode(item)
            # Move your head to the current node
            #    Also notice that the default value for any newly created node is None
            #    Unless a different value is explicitly passed in ListNode()
            current = current.next
            
            # Check if either l1 or l2 is None
            #     If not, l1 and l2 pointers move on to each of their neighboring nodes
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        
        # Make sure you have no remainders floating around after the loop was exited
        if remainder != 0:
            current.next = ListNode(remainder)
            current = current.next

        return anchor_node.next