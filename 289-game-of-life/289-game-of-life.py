class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n, flipped = len(board), len(board[0]), []
        
        for i in range(m):
            for j in range(n):
                cell, nb = board[i][j], 0
                for p in range(i - 1, i + 2):
                    for q in range(j - 1, j + 2):
                        if p >= 0 and p < m and q >= 0 and q < n and board[p][q] == 1:
                            if p == i and q == j:
                                continue
                            nb += 1
                if cell == 0:
                    if nb == 3:
                        flipped.append([i, j])
                else:
                    if nb < 2 or nb > 3:
                        flipped.append([i, j])
        
        for i in flipped:
            board[i[0]][i[1]] ^= 1
