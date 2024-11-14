class RandomizedSet:
    import random
    def __init__(self):
        self.arr = []
        self.hashmap = {}
        self.index = 0

    def insert(self, val: int) -> bool:
        if val in self.hashmap:
            return False
        else:
            self.hashmap[val] = self.index
            self.arr.append(val)
            self.index += 1
            return True

    def remove(self, val: int) -> bool:

        if val in self.hashmap:
            removeIndex = self.hashmap[val] 
            # remove takes first occurnece, pop takes index 
            self.hashmap[self.arr[-1]] = removeIndex
            self.arr[removeIndex] = self.arr[-1]
            self.arr.pop()

            

            self.hashmap.pop(val)
            self.index -= 1
            return True
        return False

    def getRandom(self) -> int:
        randomNum = random.choice(self.arr)
        return randomNum


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()