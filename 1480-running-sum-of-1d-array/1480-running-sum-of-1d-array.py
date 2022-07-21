class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        rsum = [nums[0]]
        for i in range(1, len(nums)):
            rsum.append(rsum[-1] + nums[i])
        return rsum