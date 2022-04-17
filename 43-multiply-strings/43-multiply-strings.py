class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        d = dict([(i, ord(i) - ord("0")) for i in list("0123456789")])
        def convert(x):
            s = 0
            for i in enumerate(x[::-1]):
                s += pow(10, i[0]) * d.get(i[1])
            return s
        return str(convert(num1) * convert(num2))