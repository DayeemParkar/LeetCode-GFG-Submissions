class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        patWordTab, wordSet, strList = {}, set(), s.split()
        if len(strList) != len(pattern):
            return False
        
        for pat, word in zip(pattern, strList):
            if pat not in patWordTab:
                if word in wordSet:
                    return False
                else:
                    patWordTab[pat] = word
                    wordSet.add(word)
            elif patWordTab[pat] != word:
                return False
        return True 