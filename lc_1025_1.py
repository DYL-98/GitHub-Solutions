class Solution:
    def divisorGame(self, N: int) -> bool:
        dp = [-1] * (N+1)
        
        def helper(N: int) -> bool:
            if N == 1:
                dp[1] = False
                return False
            if dp[N] != -1:
                return dp[N]
            win = False
            for i in range(1, int(N/2)+1):
                if N % i == 0:
                    win = win or ~helper(N-i) 
                    # hand N-i over to the opponent; if there is any case that the opponent cannot win, I win.
            dp[N] = win
            return win
        
        return helper(N)
