class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 1:
            return [[1]]
        ans = [[i for i in range(1, n + 1)]] + [[0 for _ in range(n)] for _ in range(n - 1)]
        row, col, end, currElem, currLen, incr = 0, n - 1, n * n, n + 1, n - 1, 1
        
        while currElem <= n * n:
            for i in range(currLen):
                row += incr
                ans[row][col] = currElem
                currElem += 1
            for i in range(currLen):
                col -= incr
                ans[row][col] = currElem
                currElem += 1
            currLen -= 1
            incr *= -1
        
        return ans