class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:

        count = 0
        hashmap = {}
        maxOutlier = -1001

        for index, val in enumerate(nums):
            count += val
            hashmap[val] = index
        print(count)
        for index in range(len(nums)):
            curr = count - nums[index]
            if curr % 2 == 0:
                target = curr // 2
                if target in hashmap and index != hashmap[target]:
                    print(target)
                    maxOutlier = max(maxOutlier, nums[index])
        
        return maxOutlier
            

            

