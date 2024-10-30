class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for index in range(len(nums)):
            nums[index] = -nums[index]
        
        heapq.heapify(nums)

        for i in range(k):
            value = heapq.heappop(nums)

        return -value