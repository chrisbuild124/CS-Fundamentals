# Depth First Search Recursive Version: Maximum Depth of Binary Tree
# Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# This is an implimentation of dfs using recursion on the maximum depth of binary tree problem.
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # try dfs
        if not root:
            return 0

        def dfs(root, count):
            if not root:
                return count
            count = max(dfs(root.left, count + 1), dfs(root.right, count + 1))
            return count

        return dfs(root, 0)
