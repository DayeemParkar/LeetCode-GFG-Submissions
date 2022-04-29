class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        people = list(range(1, n + 1))
        result = []
        trusted = [i[1] for i in trust]
        s = list(set(i[0] for i in trust))
        possible = [i for i in people if i not in s]
        
        for i in possible:
            if trusted.count(i) == (n-1):
                result.append(i)
        
        if len(result) == 1:
            return result[0]
        else:
            return -1