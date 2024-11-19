class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:

        l, r = 0, len(queries)
        found = False
        
        while l < r:
            middle = (l + r) // 2
            result = self.findZeroArray(nums, queries, middle)
            if result:
                r = middle
                found = True
            else:
                l = middle + 1
            
        if found:
            return l
        else:
            result = self.findZeroArray(nums, queries, len(queries))
            if result:
                return len(queries)
            return -1



    def findZeroArray(self, nums, queries, middle):
        copy = []
        copy[:] = nums
        
        track = [0] * (len(copy) + 1)
        
        for index in range(middle):
            left = queries[index][0]
            right = queries[index][1]
            value = queries[index][2]
            
            track[left] -= value
            track[right + 1] += value
            
        currSubtract = 0 
        
        for index in range(len(copy)):
            currSubtract += track[index]
            copy[index] += currSubtract
        
        for num in copy:
            if num > 0:
                return False
        return True