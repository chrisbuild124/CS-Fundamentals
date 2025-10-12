# This leetcode problem uses tries to find words in a word list.
# Leetcode: https://leetcode.com/problems/word-search-ii/description/ 

# Core conepts: Trie, Backtracking, saving '#' in memory to avoid the visit set


class Node:
    def __init__(self):
        self.next = dict()
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        head = Node()
        for word in words:
            temp = head
            for l in word:
                if l in temp.next:
                    temp = temp.next[l]
                else:
                    temp.next[l] = Node()
                    temp = temp.next[l]
            temp.word = word
        
        def dfs(i, j, temp):
            if temp.word != None:
                res.add(temp.word)
            cl = board[i][j]
            board[i][j] = '#'
            for ox, oy in directions:
                nx, ny = ox+i, oy+j
                if nx < 0 or ny < 0 or nx >= len(board) or ny >= len(board[0]):
                    continue
                if board[nx][ny] in temp.next:
                    dfs(nx, ny, temp.next[board[nx][ny]])
            board[i][j] = cl

        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        res = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in head.next:
                    dfs(i, j, head.next[board[i][j]])

        res = list(res)
        return res
