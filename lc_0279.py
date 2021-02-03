class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n+1] * (n+1)
        dp[0] = 0
        dp[1] = 1
        
        for i in range(2, n+1):
            min_ = n+1
            num = 1
            while num * num <= i:
                min_ = min(min_, dp[i-num*num] + 1)
                num += 1
            dp[i] = min_
        
        return dp[n]
    
