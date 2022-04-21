class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            newS, i = "", 0
            while i < len(s):
                sumS = 0
                for c in s[i:i + k]:
                    sumS += int(c)
                newS += str(sumS)
                i += k
            s = newS
        return s