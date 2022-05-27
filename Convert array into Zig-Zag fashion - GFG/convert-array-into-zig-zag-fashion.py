#User function Template for python3
class Solution:

	def zigZag(self, arr, n):
		f = 0
		for c in range(n - 1):
		    if f == 0:
		        if arr[c] > arr[c + 1]:
		            arr[c], arr[c + 1] = arr[c + 1], arr[c]
		    else:
		        if arr[c] < arr[c + 1]:
		            arr[c], arr[c + 1] = arr[c + 1], arr[c]
		    c += 1
		    f ^= 1

#{ 
#  Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.zigZag(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends