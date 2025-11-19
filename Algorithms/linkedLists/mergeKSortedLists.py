# Merge K Sorted Linked Lists 
# Leetcode Link: https://leetcode.com/problems/merge-k-sorted-lists/description/

# The trick is to merge two linked lists together by imitating the merge sort
# algorithm. 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) < 1:
            return None
        
        # Uses mergeSort algorithm 
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                if len(lists) - 1 < i + 1:
                    sll2 = None
                else:
                    sll2 = lists[i+1]
                mergedLists.append(merge(lists[i], sll2))
            lists = mergedLists

        return lists[0]
        
def merge(l, r):
    dummy = ListNode()
    res = dummy
    while l and r:
        if l and r:
            if l.val <= r.val:
                res.next = l
                l = l.next
            else:
                res.next = r
                r = r.next
        res = res.next
    if l:
        res.next = l
    elif r:
        res.next = r
    return dummy.next
