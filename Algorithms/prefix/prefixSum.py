# subarraySum
# Leetcode: https://leetcode.com/problems/subarray-sum-equals-k/

# Basically, the problem sums left to right and keeps a cumulative sum in an array at each index from left to right.
# If k - current sum is in the dictionary as moving left to right, then we know there is an array x times 
# that adds with the current num to equal k. 
# Then we increment by 1 so we can look forward for more values. 

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # [i0, i1, i2, i3, i4]
        # [1, 2, 3, 4, 5]
        # [1, 3, 6, 10, 15]
        # hashMap = {
            # 1: 1 (i0)
            # 3: 1 (i0, i1)
            # 6: 1 (i0, i1, i2)
            # 10: 1 (i0, i1, i2, i3)
            # 15: 1 (i0, i1, i2, i3, i4)
        # }
        # if (i2, i1, i0) - (i2, i1, i0 or i1, i0 or i0 or 0) == k
        # or if (i2, i1, i0) - k == (i2, i1, i0 or i1, i0 or i0 or 0)
        # This is constant (in preFix Array) - constant k, looks in dictionary, so O(N)

        sum_dict = defaultdict(int)
        sum_dict[0] = 1
        total = 0
        sum_list = []

        temp = 0
        for num in nums:
            temp += num
            sum_list.append(temp)
        
        for num in sum_list:
            if num - k in sum_dict:
                total += sum_dict[num - k]              
            sum_dict[num] += 1
        return total     
