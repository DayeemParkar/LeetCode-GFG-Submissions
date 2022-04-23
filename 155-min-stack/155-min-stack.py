class MinStack:

    def __init__(self):
        self.min = float('inf')
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min = min(self.min, val)

    def pop(self) -> None:
        removed = self.stack.pop()
        if removed == self.min:
            stack2, self.min = [], float('inf')
            while self.stack:
                elem = self.stack.pop()
                self.min = min(self.min, elem)
                stack2.append(elem)
            while stack2:
                self.stack.append(stack2.pop())

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()