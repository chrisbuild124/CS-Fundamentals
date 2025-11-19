# Linked List Cycle
# Link: https://leetcode.com/problems/linked-list-cycle/description/

# The trick here is to use fast and slow pointers to find the cycle.
# NOTE: This is a core algorithm 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        slow, fast = head, head

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow is fast:
                return True
        
        return False
