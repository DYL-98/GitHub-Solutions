class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        length = len(words)
        words.sort(key=lambda k: len(k))
        dp = dict() # Using hashmap as memory for dp
        res = 0
        for word in words:
            word_res = 0
            for i in range(len(word)): # try deleting every letter
                pred = word[:i]+word[(i+1):]
                pred_res = dp.get(pred, 0) + 1
                word_res = max(word_res, pred_res)
            dp[word] = word_res # memorize current word
            res = max(res, dp[word])
        print(dp)
        return res
