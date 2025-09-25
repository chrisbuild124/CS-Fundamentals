# Longest Consecutive Sequence
# Leetcode: https://leetcode.com/problems/longest-consecutive-sequence/

# The idea is to throw the numbers into a hash set.
# Check if it is a local max, and find the number of consecutive numbers.
# Of course you could always sort this but that would be NlogN, this is N. 

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        testSet = set()
        total = 0

        for num in nums:
            testSet.add(num)
        
        for num in nums:
            if num-1 not in testSet and num in testSet:
                temp = num
                tempTotal = 0
                while temp in testSet:
                    tempTotal += 1
                    temp += 1
                total = max(total, tempTotal)
        
        return total
