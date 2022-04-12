class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        ans = [1,1]
        for i in range(1, rowIndex):
            newAns = [1]
            for j in range(len(ans) // 2):
                newAns.append(ans[j] + ans[j + 1])
            if i % 2 == 0:
                ans = newAns + newAns[::-1]
            else:
                ans = newAns + newAns[:len(newAns) - 1][::-1]
        return ans