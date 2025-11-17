# dfs solution of Serialize and Deserialize a binary tree
# (Hard problem)

# Leetcode: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def dfs(node):
            if node:
                res.append(str(node.val))
            else:
                res.append('N')
                return
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return '#'.join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        print(data)
        if not data:
            return
        vals = data.split('#')
        count = 0
        
        def dfs():
            nonlocal count 
            if vals[count] == 'N':
                count += 1
                return None
            node = TreeNode(int(vals[count]))
            count += 1
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()
