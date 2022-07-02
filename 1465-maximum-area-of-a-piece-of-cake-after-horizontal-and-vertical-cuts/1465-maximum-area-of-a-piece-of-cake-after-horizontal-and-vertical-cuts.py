class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        maxV, maxH, m = 0, 0, 10 ** 9 + 7
        if len(verticalCuts) == 0:
            maxV = w
        else:
            prev = 0
            for i in sorted(verticalCuts):
                maxV = max(maxV, i - prev)
                prev = i
            maxV = max(maxV, w - prev)
        if len(horizontalCuts) == 0:
            maxH = h
        else:
            prev = 0
            for i in sorted(horizontalCuts):
                maxH = max(maxH, i - prev)
                prev = i
            maxH = max(maxH, h - prev)
        return ((maxV % m) * (maxH % m)) % m