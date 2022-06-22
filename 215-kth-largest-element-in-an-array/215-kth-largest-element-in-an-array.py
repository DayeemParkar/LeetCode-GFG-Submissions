class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h, ans = [], 0
        for i in nums:
            heapq.heappush(h, i * -1)
        for i in range(k):
            ans = heapq.heappop(h)
        return ans * -1