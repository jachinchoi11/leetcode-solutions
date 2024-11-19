class Solution:

    def __init__(self, w: List[int]):
        self.prefixSum = []
        self.prefix_sum = 0
        for weight in w:
            self.prefix_sum += weight
            self.prefixSum.append(self.prefix_sum)

    def pickIndex(self) -> int:
        
        randomInteger = random.randint(1, self.prefix_sum)

        for index, num in enumerate(self.prefixSum):
            if randomInteger < num:
                return index
        return 0


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()