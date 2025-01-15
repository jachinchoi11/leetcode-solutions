class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        
        '''
        - i think all we ahve to do is add one number in the hashset (we can iterarte through both using zip)
        - simplay make a new array for this and newArr[index] = len(hashset)
        '''
        res = [0] * len(A)
        currSame = 0
        hashset = set()
        aSubset = []
        for index in range(len(A)):
            hashset.add(B[index])
            if A[index] in hashset:
                currSame += 1
            else:
                aSubset.append(A[index])
            for number in aSubset:
                if number in hashset:
                    currSame += 1
                    hashset.remove(number)
        
            res[index] = currSame
        
        return res


