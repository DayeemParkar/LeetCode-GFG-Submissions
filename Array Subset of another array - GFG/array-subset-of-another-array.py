#User function Template for python3

def isSubset(a1, a2, n, m):
    f = {}
    for i in a1:
        f[i] = f.get(i, 0) + 1
    for j in a2:
        c = f.get(j, 0)
        if c == 0:
            return "No"
        f[j] -= 1
    return "Yes"


#{ 
#  Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m = sz[0], sz[1]
        a1 = [int(x) for x in input().strip().split()]
        a2 = [int(x) for x in input().strip().split()]
        
        print(isSubset( a1, a2, n, m))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends