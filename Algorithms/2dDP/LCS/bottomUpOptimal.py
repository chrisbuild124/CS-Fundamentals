# Longest common subsequence
# Link: https://leetcode.com/problems/longest-common-subsequence/description/ 

# Uses N*M runttime and M memory
# Optimization: Memory
# NOTE: only 1 M array and optimizes the text to only include the array with
# shortest length as the length in memory. 

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1
        
        dp = [0]*(len(text2) + 1)

        for i in range(len(text1) - 1, -1, -1):
            prev = 0
            for j in range(len(text2) - 1, -1, -1):
                tmp = dp[j]
                if text1[i] == text2[j]:
                    dp[j] = 1 + prev
                else:
                    dp[j] = max(dp[j], dp[j + 1])
                prev = tmp

        return dp[0]
