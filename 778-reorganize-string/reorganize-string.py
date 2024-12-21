class Solution:
    def reorganizeString(self, s: str) -> str:
        # i think we can ahve a count of the chars in s
        # use a greedy approach by putting in the highest one 
        # what we do is look for the next highest 
        # if we end up having to add the same thing then that is not good 
        # we don't have to use a queue here, in all honesty because we can jsut look for the second value 
        count = Counter(s)
        maxHeap = [(-cnt, char ) for char, cnt in count.items()]
        heapq.heapify(maxHeap)
        queue = deque()
        res = ""
        time = 0

        while maxHeap:
            currCount, currChar = heapq.heappop(maxHeap)
            if res and res[-1] == currChar:
                if not maxHeap:
                    return ""
                nextCount, nextChar = heapq.heappop(maxHeap)
                res += nextChar
                count[nextChar] -= 1
                if count[nextChar] > 0:
                    heapq.heappush(maxHeap, (-(count[nextChar]), nextChar))
                heapq.heappush(maxHeap, (currCount, currChar))
            else:
                res += currChar
                count[currChar] -= 1
                if count[currChar] > 0:
                    heapq.heappush(maxHeap, (-count[currChar], currChar))
        
        return res



