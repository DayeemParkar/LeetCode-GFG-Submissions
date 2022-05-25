class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        mid = (l + r) // 2
        while l < r:
            if nums[mid] == target: return mid
            if nums[mid] < target: l = mid + 1
            else: r = mid
            mid = (l + r) // 2
        return -1