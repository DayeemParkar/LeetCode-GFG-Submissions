#User function Template for python3

class Solution:
    def helper(self, s1, s2):
        j, m = 0, min(len(s1), len(s2))
        while j < m:
            if s1[j] != s2[j]:
                break
            j += 1
        return s1[:j]
    
    def longestCommonPrefix(self, arr, n):
        if n == 1:
            return arr[0]
        ans = self.helper(arr[0], arr[1])
        for i in range(2, n):
            ans = self.helper(ans, arr[i])
            if len(ans) == 0:
                return "-1"
        if len(ans) == 0:
            return "-1"
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n = int(input())
        arr = [x for x in input().strip().split(" ")]
        
        ob=Solution()
        print(ob.longestCommonPrefix(arr, n))
# } Driver Code Ends