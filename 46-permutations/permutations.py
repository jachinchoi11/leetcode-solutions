class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        # here we can only use 1 number once because it is a permutation 
        # i think we can do it so it can only use numbers it does not have
        # so if it chooses 1, then it has t

        # for the backtracking base case, i think when the length of the currList == len(nums) 
        # essentially, if we just let it go like try out all the combinations 

        currList, res = [], []

        def backtrack(i):
            if len(currList) == len(nums):
                res.append(currList[:])
                return

            print(currList)
            for index in range(i, len(nums)):
                if nums[index] not in currList:
                    currList.append(nums[index])
                    backtrack(0)
                    currList.pop()
        backtrack(0)
        return res