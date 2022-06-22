class Solution:
    def findSwapValues(self, a, n, b, m):
        s1, s2, s = 0, 0, set()
        for i in b:
            s.add(i)
            s2 += i
        for i in a:
            s1 += i
        for i in a:
            if (s2 - s1 + 2 * i) % 2 == 0 and (s2 - s1 + 2 * i) // 2 in s:
                return 1
        return -1
        

#{ 
#  Driver Code Starts
if __name__ == '__main__': 
    
    
    t=int(input())
    for _ in range(0,t):
        l=list(map(int,input().split()))
        n=l[0]
        m=l[1]
        a = list(map(int,input().split()))
        b = list(map(int, input().split()))
        ob = Solution()
        print(ob.findSwapValues(a,n,b,m))
# } Driver Code Ends