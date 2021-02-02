class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [-1] * length # longest increasing subsequence ending with index
        
        def helper(ending_idx) -> int:
            if dp[ending_idx] != -1:
                return dp[ending_idx]
            max_ = 1
            for i in range(ending_idx):
                if nums[i] < nums[ending_idx]:
                    max_ = max(max_, helper(i)+1)
            dp[ending_idx] = max_
            # print(dp)
            return max_
        
        ans = 0
        for i in range(length):
            ans = max(ans, helper(i)) # have to consider subarray ending with each number
        return ans
        
