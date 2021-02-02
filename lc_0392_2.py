class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        lens = len(s)
        lent = len(t)
        dp = [[0 for i in range(lens+1)] for j in range(lent+1)] # [lens][lent]
        for i in range(1,lent+1):
            for j in range(1,lens+1):
                if s[j-1] == t[i-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[lent][lens] == lens
