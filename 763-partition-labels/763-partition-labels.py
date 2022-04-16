class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        pos, start, end, ans = {}, 0, 0, []
        for i in range(len(s)):
            if s[i] in pos:
                pos[s[i]].append(i)
            else:
                pos[s[i]] = [i]
        for key in pos:
            if pos[key][0] > end:
                ans.append(end - start + 1)
                print(end)
                start, end = pos[key][0], pos[key][len(pos[key]) - 1]
            elif len(pos[key]) > 1:
                end = max(end, pos[key][len(pos[key]) - 1])
        ans.append(end - start + 1)
        return ans