class NumArray:

    def __init__(self, nums: List[int]):
        len_ = len(nums)
        self.arr = [0] * (len_ + 1)
        for i in range(1, len_ + 1):
            self.arr[i] += self.arr[i-1] + nums[i-1]

    def sumRange(self, i: int, j: int) -> int:
        return self.arr[j+1] - self.arr[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
