# Design Add and Search Word Data Structure
# Leetcode: https://leetcode.com/problems/design-add-and-search-words-data-structure/

# Same as basic, but we have a special character: '.'. We need a Trie
# because this special character helps eliminate duplicate work.

# Runttime: O(t + n), where t is total number of TrieNodes created in the Trie,
# and n is the length of the string. This is a lot better than the n^2 solution.

class Node:
    def __init__(self, val=False):
        self.trie = {}
        self.val = val

class WordDictionary:

    def __init__(self):
        self.trie = Node(False)

    def addWord(self, word: str) -> None:
        cur = self.trie
        for c in word:
            if c not in cur.trie:
                cur.trie[c] = Node()
            cur = cur.trie[c]
        cur.val = True

    def search(self, word: str) -> bool:

        def dfs(i, word, cur):
            if i == len(word):
                return cur.val
            
            if word[i] == '.':
                for node in cur.trie.values():
                    if dfs(i+1, word, node):
                        return True
                return False
            elif word[i] in cur.trie:
                return dfs(i+1, word, cur.trie[word[i]])
            else:
                return False
        return dfs(0, word, self.trie)
            
