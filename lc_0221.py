class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        max_side = 0
        for i in range(m):
            for j in range(n):
                cur = matrix[i][j]
                if cur == '1':
                    if i == 0 or j == 0: # edge case
                        dp[i][j] = 1
                        max_side = max(max_side, 1)
                        continue
                    if matrix[i][j-1] == '1' and matrix[i-1][j] == '1' and matrix[i-1][j-1] == '1':
                        # there is possible increment
                        dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
                    else:
                        dp[i][j] = 1
                    max_side = max(max_side, dp[i][j])
        return max_side ** 2
    
                
