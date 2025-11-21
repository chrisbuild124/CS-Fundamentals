# Vertical Order Traversal of a Binary Tree
# Link: https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/description/

# The trick here is to use a heap to sort items by col, row, and value. 
# For example, of col=col, then it sorts row, if row=row, then it sorts by value.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([(0, 0, root)])
        heap = []
        res = []

        while q:
            for _ in range(len(q)):
                col, row, node = q.popleft()
                heap.append((col, row + 1, node.val))
                if node.left:
                    q.append((col - 1, row + 1, node.left))
                if node.right:
                    q.append((col + 1, row + 1, node.right))

        heapq.heapify(heap)
        prevCol = None
        
        while heap:
            col, row, val = heapq.heappop(heap)
            if col != prevCol:
                res.append([])
                prevCol = col
            res[-1].append(val)

        return res
