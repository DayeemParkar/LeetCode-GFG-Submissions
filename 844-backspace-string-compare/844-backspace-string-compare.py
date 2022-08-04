class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1, s2 = [], []
        for i in s:
            if i == '#':
                if len(s1) > 0:
                    s1.pop()
            else:
                s1.append(i)
        for i in t:
            if i == '#':
                if len(s2) > 0:
                    s2.pop()
            else:
                s2.append(i)
        return s1 == s2