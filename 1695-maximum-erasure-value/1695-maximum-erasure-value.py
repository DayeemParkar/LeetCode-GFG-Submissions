class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        v, i, j, ms, cs = set(), 0, 0, 0, 0
        while j < len(nums):
            if nums[j] not in v:
                cs += nums[j]
                v.add(nums[j])
                ms = max(ms, cs)
                j += 1
            else:
                cs -= nums[i]
                v.remove(nums[i])
                i += 1 
        return ms