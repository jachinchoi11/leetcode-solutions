class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # you want to use a min heap to assign a child one at a time to the lowest percentage
        # first compute all the ratio's and store the ratios into a min heap
        # then add the percentages into the min heap, along with the indexes, so that when we add a student
        # we can recompute the ratio and feed it back in 
        # then at the end we can recompute 
        res = 0
        heap = []
        for index, certainClass in enumerate(classes):
            passValue, totalValue = certainClass
            ratio = self.computeGain(passValue, totalValue)
            heapq.heappush(heap, (-ratio, index))
        while extraStudents > 0:
            _, index = heapq.heappop(heap)
            classes[index][0] += 1
            classes[index][1] += 1
            ratio = self.computeGain(classes[index][0], classes[index][1])
            heapq.heappush(heap, (-ratio, index))
            extraStudents -= 1
        
        for passS, total in classes:
            res += passS/total
        
        return res / len(classes)
        
    def computeGain(self, passValue, totalValue):
        return (passValue + 1)/(totalValue + 1) - (passValue/totalValue)