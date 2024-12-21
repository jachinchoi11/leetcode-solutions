class Solution:
    def reorganizeString(self, s: str) -> str:
        # i think we can ahve a count of the chars in s
        # use a greedy approach by putting in the highest one 
        # what we do is look for the next highest 
        # if we end up with one thing left in hashamp, and the frequency is hgiher than 1, then we are screwed 

        count = Counter(s)
        maxHeap = [(-cnt, char ) for char, cnt in count.items()]
        heapq.heapify(maxHeap)
        queue = deque()
        res = ""
        time = 0

        while maxHeap or queue:
            if queue and queue[0][2] == time:
                currCount, currChar, _ = queue.popleft()
                heapq.heappush(maxHeap, (currCount, currChar))
            if maxHeap:
                currCount, currChar = heapq.heappop(maxHeap)
                if res and res[-1] == currChar:
                    return ""
                res += currChar
                count[currChar] -= 1
                if count[currChar] > 0:
                    queue.append([-count[currChar], currChar, time + 2])
                else:
                    count.pop(currChar)
            time += 1
        return res 



