class Solution:
    
    def findPairs(self, nums: List[int], k: int) -> int:
        count =  defaultdict(int)
        res = set()
        
        for num in nums:
            if k == 0:
                if count[num] == 1:
                    res.add((num, num))
            else:
                if num - k in count:
                    if (num - k, num) not in res:
                        res.add((num, num - k))
                if num + k in count:
                    if (num + k, num) not in res:
                        res.add((num, num + k))
            count[num] += 1
        return len(res)
