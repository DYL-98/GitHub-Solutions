class Solution:
    def countSubstrings(self, s: str) -> int:
        length = len(s)
        dp = [[0 for i in range(length)] for j in range(length)]
        for end in range(length):
            for start in range(end+1):
                if start == end:
                    dp[start][end] = 1
                elif end == start + 1:
                    dp[start][end] = 1 if s[start] == s[end] else 0
                else:
                    dp[start][end] = 1 if s[start] == s[end] and dp[start+1][end-1] == 1 else 0
        # print(dp)
        return sum([sum(row) for row in dp])
    
# "abba"
#      start 0 1 2 3 
# end
# 0          1   -->
# 1          0 1   -->
# 2          0 1 1   --> 
# 3          1 0 0 1   -->
# [a:a] = 1
# [a:a+1] = s[a]==s[a+1]
# [a:b] = s[a]==s[b] & dp[a+1][b-1] (b>a+1)




