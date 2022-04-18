class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        counter, ans = {}, []
        for i in range(len(s) - 9):
            strg = s[i: i + 10]
            if strg in counter:
                if counter[strg] == 1:
                    ans.append(strg)
                    counter[strg] = 2
            else:
                counter[strg] = 1
        return ans