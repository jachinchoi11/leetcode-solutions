class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # do a sliding window
        # edge case where they're both at teh same index 
        # can that happen 
        # so add the numbers into the sliding windo
        
        # whichever one has the lower index we promote unitl the difference of is equal or lower than the limit
        hashset = set()
        l, r = 0, 0
        minHeap = []
        maxHeap = []
        longestValue = 0

        while r < len(nums):
            
            heapq.heappush(minHeap, (nums[r], r))
            heapq.heappush(maxHeap, (-nums[r], r))


            while (-maxHeap[0][0]- minHeap[0][0]) > limit:
                l = min(minHeap[0][1], maxHeap[0][1]) + 1

                while minHeap and minHeap[0][1] < l:
                    heapq.heappop(minHeap)
                    
                while maxHeap and maxHeap[0][1] < l:
                    heapq.heappop(maxHeap)
        
            longestValue = max(longestValue, r - l + 1)
            r += 1

        return longestValue
            

