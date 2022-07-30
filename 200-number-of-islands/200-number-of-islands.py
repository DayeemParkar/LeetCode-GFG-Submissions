class Solution:
    def search(self, i, j):
        if i < 0 or j < 0 or i >= self.m or j >= self.n:
            return
        if self.grid[i][j] != '1':
            return
        self.grid[i][j] = '.'
        self.search(i - 1, j)
        self.search(i, j - 1)
        self.search(i + 1, j)
        self.search(i, j + 1)
    
    def numIslands(self, grid: List[List[str]]) -> int:
        ans, self.grid, self.m, self.n = 0, grid, len(grid), len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.grid[i][j] == '1':
                    self.search(i, j)
                    ans += 1
        return ans