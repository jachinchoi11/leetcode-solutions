class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # we are going to use a queue to make it so that we ahve to wait until we reintroduce it to the queue
        currTime = 0 
        res = 0 
        count = defaultdict(int)
        maxHeap = []
        queue = deque()

        for t in tasks:
            count[t] += 1
        
        for c in count:
            heapq.heappush(maxHeap, (-count[c], c))
        
        while maxHeap or queue:
            if maxHeap:
                freq, currLetter = heapq.heappop(maxHeap)
                count[currLetter] -= 1
                res += 1
                if count[currLetter] > 0:
                    queue.append((-count[currLetter], currLetter, currTime + n))
            else:
                res += 1
            while queue and queue[0][2] == currTime:
                freq, currLetter, _ = queue.popleft()
                heapq.heappush(maxHeap, (freq, currLetter))
            currTime += 1
        return res
            
            
        


        
        





        



        
        

        

