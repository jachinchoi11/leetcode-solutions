class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        greaterPostFix = [-1] * len(nums2)
        # -1 is gonna indicate that there is no greater number
        # any number will indicate that is the greatest number 

        res = []
        for index in range(len(nums2) - 2, -1, -1):
            for number in range(index + 1, len(nums2)):
                if nums2[number] > nums2[index]:
                    greaterPostFix[index] = nums2[number]
                    break

        for index, number in enumerate(nums1):
            if number in nums2:
                res.append(greaterPostFix[nums2.index(number)])
        
        print(greaterPostFix)
        return res
        '''
        # have a stack that runs through and sees if theres anythign bigger than it 

        res = [0] * len(nums2)
        stack = []
        count = {}

        for i, value in enumerate(nums2):
            while stack and value > stack[-1]:
                index = stack.pop()
                count[index] = value
            stack.append(value)

        while stack:
            index = stack.pop()
            count[index] = -1
        ans = []

        for num in nums1:
            ans.append(count[num])
        return ans



    




