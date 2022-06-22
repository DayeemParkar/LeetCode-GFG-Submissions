#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        ml, s, sm = 0, 0, {}
        for i in range(n):
            s += arr[i]
            if s == 0:
                ml = max(ml, i + 1)
            else:
                if sm.get(s, -1) != -1:
                    ml = max(ml, i - sm.get(s))
                else:
                    sm.update({s: i})
        return ml

#{ 
#  Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends