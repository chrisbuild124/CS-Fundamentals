# Coin change ii - top down solution
# Link: https://leetcode.com/problems/coin-change-ii/description/

# Cannot be done in 1Ddp since the dimension is both the index and what's left

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Memoization
        cache = [[-1 for _ in range(amount + 1)] for _ in range(len(coins) + 1)] # [Index in coins][amount left]
        coins.sort()

        def dfs(i, cur):
            if cur == 0:
                return 1
            if i >= len(coins):
                return 0
            if cache[i][cur] != -1:
                return cache[i][cur]
            
            res = 0
            if cur >= coins[i]:
                res = dfs(i + 1, cur) + dfs(i, cur - coins[i])

            cache[i][cur] = res
            return res

        return dfs(0, amount)
