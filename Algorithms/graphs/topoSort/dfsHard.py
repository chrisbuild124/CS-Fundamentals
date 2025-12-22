# Alian Dictionary - Premium Leetcode

# There are some subtle tricks to this one, like
# detecting a cycle and abc abcef. Otherwise,
# adding it to the dictionary is tough.

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(set) # pre: post

        # Tests for a cycle and a scenario like abc abcef, for both of these, the return is ''

        for i in range(len(words)-1):
            min_len = min(len(words[i]), len(words[i+1]))
            if len(words[i+1]) < len(words[i]) and words[i][0:min_len] == words[i+1][0:min_len]:
                return ''
            for j in range(min_len):
                if words[i+1][j] != words[i][j]:
                    adj[words[i][j]].add(words[i+1][j])
                    break
                
        res = []
        visit = set()
        global_visit = set()

        def dfs(c):
            if c in global_visit:
                return True
            visit.add(c)
            for nei in adj[c]:
                if nei in visit:
                    return False
                if not dfs(nei):
                    return False
            global_visit.add(c)
            visit.remove(c)
            res.append(c)
            return True

        for word in words:
            for c in word:
                if c not in global_visit:
                    if not dfs(c):
                        return ''
        
        return ''.join(res)[::-1]
