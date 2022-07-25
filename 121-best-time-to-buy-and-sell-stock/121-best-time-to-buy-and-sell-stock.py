class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        price = prices[0]
        ans = 0
        for i in range(1,len(prices)):
            if prices[i] < price:
                price = prices[i]
            else:
                ans = max(ans, prices[i] - price)
        return ans