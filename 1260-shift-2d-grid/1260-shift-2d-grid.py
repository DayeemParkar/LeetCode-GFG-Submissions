class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n, res =len(grid), len(grid[0]), []
        k %= (m * n)
        
        for i in grid:
            for j in i:
                res.append(j)
        
        res = res[m * n - k:] + res[0: m * n - k]
        c, temp, ans = n, [], []
        
        for i in res:
            temp.append(i)
            c -= 1
            if c == 0:
                ans.append(temp)
                temp, c = [], n
        
        return ans