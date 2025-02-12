class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        
        max_number = -1
        num_index = defaultdict(list)

        for index, num in enumerate(nums):
            calculated_sum = self.calculateDigitSum(num)
            heapq.heappush(num_index[calculated_sum], (-num, index))
        
        for value in num_index.values():
            if len(value) >= 2:
                num, _ = heapq.heappop(value)
                num2, _ = heapq.heappop(value)
                max_number = max(max_number, -1 * num + -1 *num2)
        
        return max_number
    
    def calculateDigitSum(self, num):
        curr_sum = 0

        for char in str(num):
            curr_sum += int(char)
        return curr_sum