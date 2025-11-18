# Finds the largest histogram in the rectangle with different heights
# Link: https://leetcode.com/problems/largest-rectangle-in-histogram/description/

# This is a stack implimentation and it greedily moves from left to right using a stack. 

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        area = 0
        stack = [] # i, val

        for i, h in enumerate(heights):
            if stack and stack[-1][1] > h:
                i1 = stack[-1][0]
                h1 = stack[-1][1]
                while stack and h1 > h:
                    stack.pop()
                    w = i - i1
                    area = max(area, w*h1)
                    if stack and stack[-1][1] > h:  
                        i1 = stack[-1][0]
                    if stack:
                        h1 = stack[-1][1]
                stack.append((i1, h))
            else:
                stack.append((i, h))

        for _ in range(len(stack)):
            i, h = stack.pop()
            w = len(heights) - i
            area = max(area, w*h)
        return area
