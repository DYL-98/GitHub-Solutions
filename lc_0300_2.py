class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        d = []
        # d[i]: the smallest ending number that has length i
        for num in nums:
            i = bisect.bisect_left(d, num)
            if i == len(d):
                d.append(num)
            else:
                d[i] = num
        return len(d)
# [3,4,1,2,8,5,6]
# [3,4,5] is always better than [3,4,6], better than [1,2,8]
# num d
# 3   [3]
# 4   [3,4] #[3], [:,4]
# 1   [1,4] #[1], [:,4]
# 2   [1,2] #[1], [:,2]
# 8   [1,2,8] #[1], [:,2], [:,:,8]
# 5   [1,2,5] #[1], [:,2], [:,:,5]
# 6   [1,2,5,6] #[1], [:,2], [:,:,5], [:,:,:,6]
