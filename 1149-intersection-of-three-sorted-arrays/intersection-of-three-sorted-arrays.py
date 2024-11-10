class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        res = []
        for num in arr1:
            if num in arr2:
                if num in arr3:
                    res.append(num)
        
        return res