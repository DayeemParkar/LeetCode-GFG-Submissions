class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n, prefix_sums = len(nums), collections.defaultdict(int)
        prefix_sums[0], prefix_sum, ans = 1, 0, 0
        for i in range(n):
            prefix_sum += nums[i]
            key = prefix_sum - k
            if prefix_sums[key]:
                ans += prefix_sums[key]
            prefix_sums[prefix_sum] += 1
        return ans