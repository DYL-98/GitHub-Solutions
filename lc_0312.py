class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [1] + nums + [1]
        dp = [[0] * (n+2) for i in range(n+2)]
        for l in range(1, n+1): # length: i->j = l
            for i in range(1, n-l+2): 
                # starting position of the interval is i;
                # The last possible starting position of interval length = l is n - l + 1
                j = i + l - 1
                for k in range(i, j+1):
                    dp[i][j] = max(dp[i][j], dp[i][k-1] + nums[i-1] * nums[k] * nums[j+1] + dp[k+1][j])
        return dp[1][n]
# i-1,  ||i,    i+1,  ...,   k-1,  k,    k+1, ... , j-1,  j,||    j+1
#         ||<-   dp[i][k-1]  ->||.      ||<-  dp[k+1][j] ->||   
