#User function Template for python3
import heapq

class Solution:
    def maxCoins(self, A, B, T, N):
        if T == 0 or N == 0:
            return 0
        maxC, f, c = 0, [], 0
        heapq.heapify(f)
        for i in range(N):
            heapq.heappush(f, [B[i] * -1, A[i]])
        while T != 0 and c < N:
            p = heapq.heappop(f)
            coins = p[0] * -1
            c += 1
            for i in range(p[1]):
                if T == 0:
                    break
                maxC += coins
                T -= 1
        return maxC

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        T,N=map(int,input().split())
        A=list(map(int,input().split()))
        B=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.maxCoins(A,B,T,N))
# } Driver Code Ends