class MyHashSet:

    def __init__(self):
        self.hs = []

    def add(self, key: int) -> None:
        for i in self.hs:
            if key == i:
                return
        self.hs.append(key)

    def remove(self, key: int) -> None:
        for i in self.hs:
            if key == i:
                self.hs.remove(i)
                return

    def contains(self, key: int) -> bool:
        for i in self.hs:
            if key == i:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)