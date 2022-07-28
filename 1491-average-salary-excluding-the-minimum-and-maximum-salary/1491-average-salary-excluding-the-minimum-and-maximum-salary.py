class Solution:
    def average(self, salary: List[int]) -> float:
        tS, maxS, minS = salary[0], salary[0], salary[0]
        for i in range(1, len(salary)):
            tS += salary[i]
            maxS = max(maxS, salary[i])
            minS = min(minS, salary[i])
        return (tS - maxS - minS) / (len(salary) - 2)
        