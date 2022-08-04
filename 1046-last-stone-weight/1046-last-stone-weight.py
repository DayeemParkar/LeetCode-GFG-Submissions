class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        x, y, c, f = 0, 0, len(stones), {}
        if c == 1:
            return stones[0]
        for i in stones:
            f[i] = f.get(i, 0) + 1
            if i > y:
                x, y = y, i
            elif i == y:
                x = y
            elif i > x:
                x = i
        print(x, y)
        while True:
            ans = y
            if x == y:
                c -= f[y]
                if f[y] % 2 == 0:
                    del f[y]
                else:
                    c += 1
                    f[y] = 1
            else:
                c -= 1
                f[y - x], ans = f.get(y - x, 0) + 1, y - x
                del f[y]
                f[x] -= 1
                if f[x] == 0:
                    del f[x]
                y = max(y - x, x)
            if c == 0:
                return 0
            if c == 1:
                while f.get(ans, 0) == 0:
                    ans -= 1
                return ans
            while f.get(y, 0) == 0:
                y -= 1
            x = y - 1
            if f[y] > 1:
                x += 1
            else:
                while f.get(x, 0) == 0:
                    x -= 1
        return 0