class RandomizedSet:

    def __init__(self):
        self.data_map = {}
        self.data = []

    def insert(self, val: int) -> bool:
        if val in self.data:
            return False
        self.data.append(val)
        self.data_map[val] = len(self.data) - 1
        return True

    def remove(self, val: int) -> bool:
        if not val in self.data:
            return False
        val_pos = self.data_map[val]
        self.data_map[self.data[-1]] = val_pos
        self.data[val_pos], self.data[-1] = self.data[-1], self.data[val_pos]
        self.data_map.pop(val)
        self.data.pop()

        return True

    def getRandom(self) -> int:
        return random.choice(self.data)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()