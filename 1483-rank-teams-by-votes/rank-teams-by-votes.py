class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        # we will design a hashmap with a list of 4 stuff
        count = len(votes[0])
        hashmap = {}
        res = ""
        heap = []
        for vote in votes[0]:
            hashmap[vote] = [0] * count

        for vote in votes:
            for index in range(len(vote)):
                hashmap[vote[index]][index] += 1
        
        for key, values in hashmap.items():
            curr = []
            for value in values:
                curr.append(-1 * value)
            curr.append(key)
            heapq.heappush(heap, curr)
        while heap:
            currentArr = heapq.heappop(heap)
            res += currentArr[-1]
        
        return res
        
        