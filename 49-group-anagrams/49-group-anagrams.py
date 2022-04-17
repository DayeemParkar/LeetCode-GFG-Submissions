class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag = {}
        for strg in sorted(strs):
            key = tuple(sorted(strg))
            anag[key] = anag.get(key, []) + [strg]
        return anag.values()