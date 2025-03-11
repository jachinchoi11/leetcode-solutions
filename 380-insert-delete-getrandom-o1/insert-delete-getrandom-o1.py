# we ahbea a randomized set, and we have to put in a random thing
    # you can not index through a set 
    # so we need to have some type of array 

class RandomizedSet:

    def __init__(self):

        self.numbers = []
        self.number_to_index = {}
        self.curr_index = 0

    def insert(self, val: int) -> bool:
        if val not in self.number_to_index:
            self.numbers.append(val)
            self.number_to_index[val] = self.curr_index
            self.curr_index += 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.number_to_index:
            remove_index = self.number_to_index[val]
            self.numbers[remove_index] = self.numbers[-1]
            self.number_to_index[self.numbers[remove_index]] = remove_index
            self.number_to_index.pop(val)
            self.numbers.pop()
            self.curr_index -= 1
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.numbers)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()