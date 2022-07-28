class Solution:
    def countOdds(self, low: int, high: int) -> int:
        c = (high - low) // 2
        if low % 2 == 1 or high % 2 == 1:
            return c + 1
        return c