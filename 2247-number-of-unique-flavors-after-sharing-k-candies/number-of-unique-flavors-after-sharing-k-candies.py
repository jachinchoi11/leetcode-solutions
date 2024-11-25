class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        # i thnk this is the sldiign windo problem where you give away the minimum k substrsing flavors highest frequencey 
        # you can track it using a hashmap
        # we should just use a set instead, as we are looking for uniqueness
        maxCandies = defaultdict(int)
        uniqueCandyCount = defaultdict(int)
        maxRes = 0
        for candy in candies:
            maxCandies[candy] += 1
        
        left = 0
        for right in range(k):
            maxCandies[candies[right]] -= 1
            if maxCandies[candies[right]] == 0:
                maxCandies.pop(candies[right])
        right = k
        while right < len(candies):
            maxRes = max(maxRes, len(maxCandies))
            maxCandies[candies[left]] += 1
            maxCandies[candies[right]] -= 1
            if maxCandies[candies[right]] == 0:
                maxCandies.pop(candies[right])
            left += 1
            right += 1
        maxRes = max(maxRes, len(maxCandies))
        
        return maxRes


