# This is an interval problem but it's a heap trick that can also be used with queues
# Link: https://leetcode.com/problems/minimum-interval-to-include-each-query/description/

# The trick is to pop invalid entries at the top of the heap before finding if it is the correct
# value. Therefore the heap could have invalid answers but never at the top, which is where the answer
# lies. 
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # Try using heap

        intervals.sort()

        # To get back to indexes
        queries = sorted((q, i) for i, q in enumerate(queries))

        res = [-1]*len(queries)
        heap = []
        heapq.heapify(heap)

        i = 0 # intervals
        j = 0 # queries
        while j < len(queries):
            time, index = queries[j][0], queries[j][1]
            while i < len(intervals) and time >= intervals[i][0]: # Push new intervals <= time
                heapq.heappush(heap, (intervals[i][1] - intervals[i][0] + 1, intervals[i][1]))
                i += 1
            while heap and heap[0][1] < time: # Pop invalid times (old times)
                length, end = heapq.heappop(heap)
            res[index] = (heap[0][0]) if heap else -1
            j += 1
        
        return res
