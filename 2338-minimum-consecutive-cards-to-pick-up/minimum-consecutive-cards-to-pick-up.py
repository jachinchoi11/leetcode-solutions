class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        
        count = {}
        minCount = float('inf')
        for index, card in enumerate(cards):

            if card in count:
                minCount = min(minCount, index - count[card] + 1)
            count[card] = index

        if minCount == float('inf'):
            return -1
        return minCount
