# Implement Trie
# Leetcode: https://leetcode.com/problems/implement-trie-prefix-tree/

# The idea behind this is to create a tree with each node being a letter, and a special
# value representing if there is a word there. 

# NOTE: This design is needed because we want to check for prefixes, without it, our
# runttime would go to n^2

class Trie:

    def __init__(self):
        self.tree = {}

    def insert(self, word: str) -> None:
        temp = self.tree
        for c in word:
            if c not in temp:
                temp[c] = dict()
            temp = temp[c]
        temp[1] = True

    def search(self, word: str) -> bool:
        temp = self.tree
        for c in word:
            if c not in temp:
                return False
            temp = temp[c]
        print(temp)
        return True if 1 in temp else False

    def startsWith(self, prefix: str) -> bool:
        temp = self.tree
        for c in prefix:
            if c not in temp:
                return False
            temp = temp[c]
        return True if len(temp) > 0 else False
        
        
