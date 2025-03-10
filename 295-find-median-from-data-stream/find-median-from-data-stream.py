# our approach is using a max and min heap to find the median in O(1) time 

# our left heap will be the max heap
# our right heap will be the min heap

# left and right heap can only be offset by 1 left having more than 1
    # for our purposes left should have as we retunr left heap
    
    # the absolute values of all of our values in the left heap should be less than the ones in the right heap

    # if it is bigger than the min heap max  --> max heap
        # and then if max heap has more then you pop off max heap and put it into min heap
    
    # if it is smaller than the max heap min, --> min heap
        # and then if min heap has more, then you pop off the min heap and put it into max heap

# Case 1: if the lneght of our thing is even --> thne it is in the average of left and righ heap
# Case 2: the length is odd --> the one on the left heap

import heapq

class MedianFinder:

    def __init__(self):

        self.left_max_heap = [] # max heap to carry left side of numbers
        self.right_min_heap = [] # min heap to carry right side of numbers

    def addNum(self, num: int) -> None:

        # just adding to left_max_heap if nothing
        heapq.heappush(self.left_max_heap, (-num))
        
        # checking if it should be in right or left heap
        if self.left_max_heap and self.right_min_heap and (-self.left_max_heap[0] > self.right_min_heap[0]):
            value = -heapq.heappop(self.left_max_heap)
            heapq.heappush(self.right_min_heap, (value))
    
        # rebalancing
        if len(self.left_max_heap) - len(self.right_min_heap) > 1:
            value = -heapq.heappop(self.left_max_heap)
            heapq.heappush(self.right_min_heap, (value))
        
        if len(self.left_max_heap) < len(self.right_min_heap):
            value = heapq.heappop(self.right_min_heap)
            heapq.heappush(self.left_max_heap, (-value))

    def findMedian(self) -> float:

        # find median should be based on the length of the max and min heap 

        total_length = len(self.left_max_heap) + len(self.right_min_heap)

        if total_length % 2 == 1:
            return -self.left_max_heap[0]
        else:
            return (-self.left_max_heap[0] + self.right_min_heap[0]) / 2






# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()