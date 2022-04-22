class MyHashMap:

    def __init__(self):
        self.hmap = []

    def put(self, key: int, value: int) -> None:
        inserted = False
        for i in range(len(self.hmap)):
            if self.hmap[i][0] == key:
                self.hmap[i][1] = value
                inserted = True
                break
        if not inserted:
            self.hmap.append([key, value])

    def get(self, key: int) -> int:
        for i in range(len(self.hmap)):
            if self.hmap[i][0] == key:
                return self.hmap[i][1]
        return -1

    def remove(self, key: int) -> None:
        for i in range(len(self.hmap)):
            if self.hmap[i][0] == key:
                self.hmap.remove(self.hmap[i])
                break


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)