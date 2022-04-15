class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter, ans = {}, 0
        for char in s:
            if char in counter:
                counter[char] += 1
            else:
                counter[char] = 1
        for key in counter:
            ans += (counter[key] // 2) * 2
            if (ans % 2 == 0):
                ans += counter[key] % 2
        return ans