class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        m, n, sums, carry, p, temp = len(num1) - 1, len(num2) - 1, 0, 0, 1, 0
        while m >= 0 or n >= 0:
            if m < 0:
                temp = ord(num2[n:n + 1]) - 48
            elif n < 0:
                temp = ord(num1[m:m + 1]) - 48
            else:
                temp = ord(num1[m:m + 1]) + ord(num2[n:n + 1]) - 96
            sums += ((temp + carry) % 10) * p
            p *= 10
            carry = (temp + carry) // 10
            m -= 1
            n -= 1
        sums += (carry % 10) * p
        return str(sums)