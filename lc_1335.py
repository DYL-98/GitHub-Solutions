class Solution:    
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        
        dp = [[0] + [float('inf')] * n for _ in range(d + 1)]
        
        for i in range(1, d + 1):
            for j in range(i, n + 1):
                current = 0
                for k in range(j, i - 1, -1):
                    current = max(current, jobDifficulty[k - 1])
                    dp[i][j] = min(dp[i][j], current + dp[i - 1][k - 1])
        return dp[-1][-1]
# dp[i][j]: min difficulty to schedule the first j jobs (1-indexed) in i days
# if n < d: no solution
# dp[*][0] = 0, otherwise, dp[*][*] = inf
# dp[i][j] = min (dp[i-1][k-1] + max(jobDifficulty[k-1, k, ..., j])) for k in j, j-1, j-2, ..., i
# Eg:
# 1.   2.   3.   4.   5.   6.   7.   8.   
# 11   111  22   222  33   333  44   444 
# i = 3; j = 5
# k = 5,4,3
# k = 5: dp[3][5] = min(dp[3][5], max(33) + dp[3-1][5-1])
# 1.   2.   3.   4.   5.   6.   7.   8.   
# |11  111  22   222||33|  333  44   444
# k = 4: dp[3][5] = min(dp[3][5], max(33,222) + dp[3-1][4-1])
# 1.   2.   3.   4.   5.   6.   7.   8.   
# |11  111  22|| 222  33|  333  44   444
# k = 3: dp[3][5] = min(dp[3][5], max(33,222,22) + dp[3-1][3-1])
# 1.   2.   3.   4.   5.   6.   7.   8.   
# |11  111||22   222  33|  333  44   444
