class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ls, rs = 0, sum(nums) - nums[0]
        if ls == rs:
            return 0
        for i in range(1, len(nums)):
            ls += nums[i - 1]
            rs -= nums[i]
            if ls == rs:
                return i
        return -1