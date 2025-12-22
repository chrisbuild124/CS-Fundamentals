# Alian Dictionary - Premium Leetcode

# There are some subtle tricks to this one, like
# detecting a cycle and abc abcef. Otherwise,
# adding it to the dictionary is tough.

# The indegree is needed since it's pre/post and check each off. 

# More ways are available for bfs but this is the most efficient: adj[pre] = post, and
# post: pre for the indegree

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Try topological sort
        adj = defaultdict(set) # adj[pre] = post
        indegree = defaultdict(int) # post: pre

        for word in words:
            for c in word:
                indegree[c] += 0

        for i in range(len(words)-1):
            for j in range(min(len(words[i]), len(words[i+1]))):
                if words[i+1][j] != words[i][j]:
                    if words[i+1][j] not in adj[words[i][j]]:
                        indegree[words[i+1][j]] += 1
                        adj[words[i][j]].add(words[i+1][j])
                    break
            if words[i][0:len(words[i+1])] == words[i+1] and len(words[i]) > len(words[i+1]):
                return '' 

        q = deque()
        res = []

        for key in indegree:
            if indegree[key] == 0:
                q.append(key)

        while q:
            c = q.popleft()
            res.append(c)
            for nei in adj[c]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        print(res)

        return '' if len(indegree) != len(res) else ''.join(res)
                    
