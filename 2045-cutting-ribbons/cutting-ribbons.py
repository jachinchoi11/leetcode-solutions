class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        # so you can do a binary search with the maximum length 
        # if it is true then you make the bounds smaller to make more cut s
        # if it is false then you make the bounds up 
        # jsut have a var that keeps track of the max length of when it passes 
        # if impossible, then you return 0. you can check this at the beginning 
        # or theroretically it wil already be checked 

        # for the left and right bounds you can get 0 and max(ribons)

        l, r = 1, max(ribbons)
        res = 0
        while l <= r:
            m = (l + r) // 2
            if self.binarySearch(m, k, ribbons):
                res = max(res, m)
                l = m + 1
            else:
                r = m - 1
        return res

    def binarySearch(self, m, k, ribbons):

        count = 0
        for ribbon in ribbons:
            count += ribbon // m
        return True if count >= k else False
        
            

