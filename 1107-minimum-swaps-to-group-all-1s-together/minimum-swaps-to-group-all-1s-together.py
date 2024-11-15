class Solution:
    def minSwaps(self, data: List[int]) -> int:
        
        # initially, traverse through the array and count all the ones
        # and then simulate through the array and see if there's gaps in the data where I can put it the ones
        # do this through some sort of a count for 0's in a subarray
        # keep on going and check subarrays of how much 1s there are 

        countOfOnes = 0
        countOfZeroes = 0
        for bit in data:
            # count how big the subarray should be 
            if bit == 1:
                countOfOnes += 1
        
        left, right = 0, 0
        while right < countOfOnes:
            if data[right] == 0:
                countOfZeroes += 1
            right += 1
        
        minSwaps = countOfOnes

        while right < len(data):
            minSwaps = min(minSwaps, countOfZeroes)
            if data[left] == 0:
                countOfZeroes -= 1
            left += 1
            if data[right] == 0:
                countOfZeroes += 1
            right += 1
        
        minSwaps = min(minSwaps, countOfZeroes)

        return minSwaps
        
