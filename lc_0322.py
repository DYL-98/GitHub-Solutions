class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1) # initialize to an impossible & large number
        dp[0] = 0
        coins = sorted(coins)
        for i in range(1, amount+1):
            for coin in coins:
                if i >= coin and dp[i-coin] != amount+1:
                    dp[i] = min(dp[i], dp[i-coin] + 1)
        return dp[amount] if dp[amount] != amount+1 else -1
        
