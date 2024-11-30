class TimeMap:
    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:

        self.hashmap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:

        self.currList = self.hashmap[key]
        res = ""
        l, r = 0, len(self.currList) - 1

        while l <= r:
            m = (l + r) // 2
            currElement = self.currList[m]
            if currElement[1] == timestamp:
                return currElement[0]
            elif currElement[1] > timestamp:
                r = m - 1
            else:
                res = currElement[0]
                l = m + 1
        return res



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)