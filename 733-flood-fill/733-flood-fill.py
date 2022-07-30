from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited, rem, m, n, ogcol = set(), deque(), len(image), len(image[0]), image[sr][sc]
        rem.append([sr, sc])
        while rem:
            r, c = rem.popleft()
            visited.add(str(r) + " " + str(c))
            image[r][c] = color
            if r - 1 > -1:
                if str(r - 1) + " " + str(c) not in visited and image[r - 1][c] == ogcol:
                    image[r - 1][c] = color
                    rem.append([r - 1, c])
            if c - 1 > -1:
                if str(r) + " " + str(c - 1) not in visited and image[r][c - 1] == ogcol:
                    image[r][c - 1] = color
                    rem.append([r, c - 1])
            if r + 1 < m:
                if str(r + 1) + " " + str(c) not in visited and image[r + 1][c] == ogcol:
                    image[r + 1][c] = color
                    rem.append([r + 1, c])
            if c + 1 < n:
                if str(r) + " " + str(c + 1) not in visited and image[r][c + 1] == ogcol:
                    image[r][c + 1] = color
                    rem.append([r, c + 1])
        return image