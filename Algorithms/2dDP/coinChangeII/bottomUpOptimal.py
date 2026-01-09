# Coin change ii - bottom up solution optimized
# Link: https://leetcode.com/problems/coin-change-ii/description/

# Cannot be done in 1Ddp since the dimension is both the index and what's left

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Bottom up dp optimized
        dp = [0]*(amount + 1)
        dp[0] = 1

        for i in range(len(coins)):
            for amt in range(1, amount + 1):
                dp[amt] += dp[amt - coins[i]] if coins[i] <= amt else 0
        
        return dp[amount]
