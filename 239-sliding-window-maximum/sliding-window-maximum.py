class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        # this is a hard sliding window problem, we are cracked if we can figure this out

        # ok so you have a static k sliding window, in which you will increase one and then decrease one
        # find the highest value in your window 
        # do that for all windows res.append(x)

        # i initially thought you could have a max var, but that only works if the max is always increasing 
        # if it is not always increasing, then you need to be able to do this in a nother way
        # potenitally a heap that we can have, we can first index through the k and find their indexes
        # then as we go trhough we can check taht the heap is in bounds of the number 

        curr_heap = []
        left, right, res = 0, 0, []

        while right < len(nums):
            right_num = nums[right]
            heapq.heappush(curr_heap, (-right_num, right))
            if right >= k - 1:
                while curr_heap and curr_heap[0][1] < left or curr_heap[0][1] > right:
                    heapq.heappop(curr_heap)

                res.append(-curr_heap[0][0])
                left += 1
            right += 1
        return res
        
        # (-1, 0)
        # (-3, 1)
        # (1, 2)
        # 