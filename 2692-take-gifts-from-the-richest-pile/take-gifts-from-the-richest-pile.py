class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # use a heap and return the heighest one 
        # pop and push back for x amount fo seconds and return the numebr of gifts 

        for index in range(len(gifts)):
            gifts[index] *= -1
        heapq.heapify(gifts)

        res = 0
        for second in range(k):
            curr = heapq.heappop(gifts)
            heapq.heappush(gifts, -1 *int((-1 * curr) ** 0.5))
        print(gifts)
        for gift in gifts:
            res += -1 * gift
        return res