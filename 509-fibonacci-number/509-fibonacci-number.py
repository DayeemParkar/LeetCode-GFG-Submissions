class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        mem = (0, 1)
        for _ in range(2, N + 1):
            mem = (mem[1], mem[0] + mem[1])
        return mem[1]