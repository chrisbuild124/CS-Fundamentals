# Sweep Line Algorithm implimented on Merge Intervals problem
# Link: https://leetcode.com/problems/merge-intervals/description/

# The trick here is to keep a running total of curent meetings right now.
# Then, go through from start to finihs and compute the current net meetings.
# If the current net meetings is 0 and the current start is the same interval,
# then we know it's the end of an interval and can be appended to the result. 

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []

        n = max(interval[0] for interval in intervals)
        mp = [-1] * (n + 1)
        for s, e in intervals:
            mp[s] = max(mp[s], e)

        start, end = -1, -1

        for i in range(len(mp)):
            if mp[i] >= 0 and start == -1:
                start = i
            end = max(mp[i], end)
            if start != -1 and i == end:
                res.append([start, end])
                start, end = -1, -1

        if start != -1 and end != -1:
            res.append([start, end])
        return res
            
