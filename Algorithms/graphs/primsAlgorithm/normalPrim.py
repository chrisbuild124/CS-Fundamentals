# This is not a leetcode problem

# The goal is to find the minimum spanning tree in v^2 logE time. 
# NOTE: It would be V*E*logE if G was not a matrix and instead an adj list. 
# Can handle negative weights. 

import heapq

def connect_bridges(G):
    """Uses Prim's algorithm to find the min span tree.
    It will find the order to visit all the islands 
    the cheapest total distance.
    
    The output: A list of tuples where each tuple represents 
    two islands connected by a bridge and the cost of that 
    bridge in the format: (Island1_Index, Island2_Index, cost)."""

    res = []
    heap = []

    for i in range(len(G[0])):
        if G[0][i] != 0:
            heap.append((G[0][i], 0, i))

    heapq.heapify(heap)
    visit = {0}

    while heap:
        value, start, end = heapq.heappop(heap)
        if end in visit:
            continue
        visit.add(end)
        res.append((start, end, value))
        for i in range(len(G[end])):
            if G[end][i] != 0 and i not in visit:
                heapq.heappush(heap, (G[end][i], end, i))

    return res

# G = [
#   [0, 8, 5, 0, 0, 0, 0],
#   [8, 0, 10, 2, 18, 0, 0],
#   [5, 10, 0, 3, 0, 16, 0],
#   [0, 2, 3, 0, 12, 30, 14],
#   [0, 18, 0, 12, 0, 0, 4],
#   [0, 0, 16, 30, 0, 0, 26],
#   [0, 0, 0, 14, 4, 26, 0]
# ]
# print(connect_bridges(G))
