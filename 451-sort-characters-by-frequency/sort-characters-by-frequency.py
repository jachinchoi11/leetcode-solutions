import heapq
class Solution:
    def frequencySort(self, s: str) -> str:
        count = defaultdict(int)
        res = []
        ans = ""
        for char in s:
            count[char] += 1
        
        for key, value in count.items():
            res.append((-value, key))
        
        heapq.heapify(res)

        while len(res) > 0:
            curr = heapq.heappop(res)
            value = abs(curr[0])
            key = curr[1]
            while abs(value) > 0:
                ans += key
                value -= 1
        return ans

        
