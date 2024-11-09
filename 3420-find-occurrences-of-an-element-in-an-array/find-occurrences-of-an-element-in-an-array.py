class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        count = defaultdict(list)
        res = []

        for index, num in enumerate(nums):
            count[num].append(index)

        if x not in count:
                return [-1] * len(queries)
        else:
            for query in queries:
                if query <= len(count[x]):
                    res.append(count[x][query - 1])
                else:
                    res.append(-1)
        return res 
            
            
        
            