# dailyTemperatures is the best way to understand the minStack implimentation
# Link: https://leetcode.com/problems/daily-temperatures/description/

# This is the minStack implimentation (basically, a stack that keeps track of
# the last value that was less than the current at each iteration. 

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # [30,38,30,36,35,40,28]
        # i = 6: 28
        # i = 5: 40
        # i = 4: 40, 35
        # i = 3: 40, 36
        # i = 2: 40, 36, 30
        # i = 1: 40, 38
        # i = 0: 40, 38, 30

        stack = []
        returnTemp = [0] * len(temperatures)
        for i in range(len(temperatures)-1, -1, -1):
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            if stack:
                returnTemp[i] = stack[-1] - i
            stack.append(i)
        return returnTemp

