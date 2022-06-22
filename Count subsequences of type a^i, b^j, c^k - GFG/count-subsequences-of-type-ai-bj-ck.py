#User function Template for python3

class Solution:
    def fun(self, s):
        dp, m = [1, 0, 0, 0], 1000000007
        for i in s:
            k = ord(i) - 96
            dp[k] = (dp[k - 1] + dp[k] * 2) % m
        return dp[3]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#Position this line where user code will be pasted.

t=int(input())
for _ in range(t):
    s=input()
    print(Solution().fun(s))
# } Driver Code Ends