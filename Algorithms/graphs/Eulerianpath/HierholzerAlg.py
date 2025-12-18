# Hierholzer Algorithm - it uses a Eulerian path to search through and find the path.
# It works in ElogE in this problem but it's very specific to this problem because
# there are many solutions but the solution desired is ordered, so the algorithm
# can search directly to find the correct answer. 

# There are really no branches in this problem, it's more of a special graph that
# will always give a solution. 

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
