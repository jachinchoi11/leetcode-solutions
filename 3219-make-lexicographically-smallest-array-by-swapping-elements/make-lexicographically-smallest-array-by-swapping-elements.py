class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        
        '''
        so the correct approach is that youa ctuallly have to groiup them, as that would be the only way to do this problem 
        the reason is why is because finding the smalles one at that second, is not alwyas the optimal choice, and you mnigth need to do repetiive swaps
        that is why it is better to just group the ones you can swap and greedily choosing the lowest one out of those
        '''
        connected_components = []
        num_to_group = {}
        res = []

        for n in sorted(nums):
            if not connected_components or abs(n - connected_components[-1][-1]) > limit:
                connected_components.append(deque())
            
            connected_components[-1].append(n)
            num_to_group[n] = len(connected_components) - 1

        for num in nums:
            find_index = num_to_group[num]
            lowest_value = connected_components[find_index].popleft()
            res.append(lowest_value)
        
        return res
            




