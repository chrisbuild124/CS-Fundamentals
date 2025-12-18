# Hierholzer Algorithm - it uses a Eulerian path to search through and find the path.
# It works in ElogE in this problem but it's very specific to this problem because
# there are many solutions but the solution desired is ordered, so the algorithm
# can search directly to find the correct answer. 

# There are really no branches in this problem, it's more of a special graph that
# will always give a solution. 
# 
# An Eulerian circuit (path that starts and ends at the same node) exists if and only if:

# An Eulerian path (can start and end at different nodes) exists if and only if:
# The graph is connected.
# Exactly two vertices have odd degree (for undirected), or exactly one vertex has out-degree = in-degree + 1 and one has in-degree = out-degree + 1 (for directed).

# Link: https://leetcode.com/problems/reconstruct-itinerary

# Since this needs to be in lexigraphical order, after sorting, each dfs call is 
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dst in sorted(tickets)[::-1]:
            adj[src].append(dst)

        res = []
        def dfs(src):
            while adj[src]:
                dst = adj[src].pop()
                dfs(dst)
            res.append(src)

        dfs('JFK')
        return res[::-1]
