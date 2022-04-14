class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, ans = 1, []
        for num in nums:
            ans.append(prod)
            prod *= num
        prod = 1
        for i in range(len(ans) - 1, -1, -1):
            ans[i] *= prod
            prod *= nums[i]
        return ans