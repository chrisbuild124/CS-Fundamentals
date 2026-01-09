# Coin change ii - bottom up solution
# Link: https://leetcode.com/problems/coin-change-ii/description/

# Cannot be done in 1Ddp since the dimension is both the index and what's left

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Bottom up dp
        dp = [[0 for _ in range(len(coins) + 1)] for _ in range(amount + 1)]
        for i in range(len(coins) + 1):
            dp[0][i] = 1
        coins.sort()

        for amt in range(1, amount + 1):
            for j in range(len(coins) - 1, -1, -1):
                if amt - coins[j] >= 0:
                    dp[amt][j] += dp[amt - coins[j]][j]
                dp[amt][j] += dp[amt][j + 1]
        return dp[amount][0]
