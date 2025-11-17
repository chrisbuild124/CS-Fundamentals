# bfs solution of Serialize and Deserialize a binary tree
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
        temp = ''
        if not root:
            return temp
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                temp = temp + str(node.val) + '#'
            else:
                temp = temp + 'N' + '#'
            if node:
                queue.append(node.left)
                queue.append(node.right)
        return temp
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return 
        for i in range(len(data)-1, 0, -2):
            if data[i] == '#' and data[i-1] == 'N':
                continue
            else:
                break
        data = data[0:i+1]
        head = None
        parent = None
        prev = ''
        queue = deque()
        count = 0
        temp = ''
        print(data)
        for c in data:
            if c == '#' and prev != 'N':
                node = TreeNode(temp)
                print(temp)
                queue.append(node)
                if head is None:
                    head = node
                temp = ''
                count += 1
            elif c == 'N':
                temp = ''
                node = None
                count += 1
            elif c != '#':
                temp = temp + c

            if count == 2:
                parent = queue.popleft()
                count = 0
            if parent and c == '#':
                if count == 0:
                    parent.left = node
                elif count == 1:
                    parent.right = node
            prev = c
            
        queue = deque([head])
        while queue:
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            print(node.val)
        return head
