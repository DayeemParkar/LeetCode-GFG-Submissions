class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0 and n % 2 != 0:
            temp = self.myPow(x, n // 2 + 1)
        else:
            temp = self.myPow(x, n // 2)
        if n % 2 == 0:
            return temp * temp
        else:
            if n > 0:
                return x * temp * temp
            else:
                return (temp * temp) / x