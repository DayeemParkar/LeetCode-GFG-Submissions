class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull, cow = 0, 0
        s, g = {}, {}
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull += 1
            else:
                s[secret[i]], g[guess[i]] = s.get(secret[i], 0) + 1, g.get(guess[i], 0) + 1
        for k in s:
            if g.get(k, 0) != 0:
                cow += min(s[k], g[k])
        
        return '{0}A{1}B'.format(bull, cow)