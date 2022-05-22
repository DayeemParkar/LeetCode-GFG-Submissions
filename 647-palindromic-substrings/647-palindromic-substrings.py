class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        ans = [s[x:y] for x, y in combinations(range(len(s) + 1), r = 2)]
        for s in ans:
            if s == s[::-1]:
                count += 1
        return count