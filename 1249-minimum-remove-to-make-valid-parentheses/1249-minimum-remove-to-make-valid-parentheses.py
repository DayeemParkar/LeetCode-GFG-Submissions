class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        newStr, bal = "", 0
        for char in s:
            if char == "(":
                bal += 1
                newStr += char
            elif char == ")":
                if bal != 0:
                    bal -= 1
                    newStr += char
            else: newStr += char
        i = len(newStr) - 1
        while bal > 0:
            if newStr[i] == "(": newStr, bal = newStr[:i] + newStr[i + 1:], bal - 1
            i -= 1
        return newStr