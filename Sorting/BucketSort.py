# This is bucket sort used for a leetcode problem.
# Leetcode: https://leetcode.com/problems/top-k-frequent-elements/ 

# KEY INFORMATION:
# The test cases are generated such that the answer is always unique.
# So we do not have to sort the lists generated, but if there were more than one answer, we would. 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Make a dictionary:
            # Key being num, value being occurance
        # Make a new array size of nums
            # array[count] = num (a list) of values
        # Loop backward and count up until k occurances inside the list
        # This is Bucket sort

        tempDict = defaultdict(int) # Default value is 0
        for num in nums:
            tempDict[num] += 1
        
        tempArray = [None] * (len(nums) + 1)
        for key in tempDict:
            if tempArray[tempDict[key]] is not None:
                tempArray[tempDict[key]].append(key)
            else:
                tempArray[tempDict[key]] = [key]

        count = 1
        returnList = list()
        for temp in tempArray[::-1]:
            if temp:
                for temp2 in temp:
                    if count <= k:
                        returnList.append(temp2)
                        count += 1
        
        return returnList

