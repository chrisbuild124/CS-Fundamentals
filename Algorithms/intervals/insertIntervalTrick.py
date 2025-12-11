# Insert Interval Trick - uses Greedy
# Link: https://leetcode.com/problems/insert-interval/description/

# This problem uses a greedy trick: It basically keeps editing the newInterval
# to be an overlapping interval, and then if it no longer overlaps, returns
# the intervals before, the newInterval, and the rest of the intervals. 

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        
        for i, interval in enumerate(intervals):
            if interval[0] > newInterval[1]:
                return res + [newInterval] + intervals[i:]
            elif interval[1] < newInterval[0]:
                res.append(interval)
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        res.append(newInterval)
        return res
