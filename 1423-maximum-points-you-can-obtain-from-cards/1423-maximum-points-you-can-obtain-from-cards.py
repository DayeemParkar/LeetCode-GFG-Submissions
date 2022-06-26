class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        cs, ms = 0, 0
        for i in range(k):
            cs += cardPoints[i]
        ms = cs
        for i in range(k - 1, -1, -1):
            cs -= cardPoints[i]
            cs += cardPoints[len(cardPoints) - k + i]
            ms = max(cs, ms)
        return ms