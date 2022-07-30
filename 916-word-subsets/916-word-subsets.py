class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        maxFreq, ans = {}, []
        for word in words2:
            f = {}
            for i in word:
                f[i] = f.get(i, 0) + 1
                if f[i] > maxFreq.get(i, 0):
                    maxFreq[i] = f[i]
        for word in words1:
            fCpy, chars = maxFreq.copy(), len(maxFreq)
            for i in word:
                val = fCpy.get(i, 0)
                if val == 1:
                    chars -= 1
                if val != 0:
                    fCpy[i] -= 1
            if chars == 0:
                ans.append(word)
        return ans