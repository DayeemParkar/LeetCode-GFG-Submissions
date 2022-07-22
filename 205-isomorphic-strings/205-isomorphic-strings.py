class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m, used, l = {}, set(), 0
        for i in range(len(s)):
            mapC = m.get(s[i], '')
            if len(mapC) == 0:
                used.add(t[i])
                if l == len(used):
                    return False
                l += 1
                m[s[i]] = t[i]
            elif mapC != t[i]:
                return False
        return True