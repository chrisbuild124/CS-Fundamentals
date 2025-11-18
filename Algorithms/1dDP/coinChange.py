# Coin change leetcode problem
# Link: https://leetcode.com/problems/coin-change/description/

# Instead of using indexes as the cache, it uses the amount left (not intuitive at first)
# note this is the backtracking solution 

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = float('inf')

        dp = [float('inf')]*(amount+1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return -1 if dp[-1] == float('inf') else dp[-1]
