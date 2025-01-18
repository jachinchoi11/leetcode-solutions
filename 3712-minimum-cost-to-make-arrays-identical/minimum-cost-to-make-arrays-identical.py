class Solution:
    def minCost(self, arr: List[int], brr: List[int], k: int) -> int:
        # so the rearrangement just means it will be added in the very end, if the configuration is not the same 
        # if not, the only way to actually switch the contents of the array is to switch the values
        
        # Case 1: where you would rather switch everything to the other one (cost being x) (k value being super high)
        # Case 2: where you woudl rather switch eveyrthing until you have the same things(rearrange)
        # Case 3: where it would already be the same

        if arr[:] == brr[:]:
            return 0
        
        # calcualte teh price to switch everything 
        # calculate the price to switch, and then rearrange 
        changeEverythingCost = 0
        changeAndRearrange = 0

        count = Counter(arr)
        switch = []
        
        for index in range(len(arr)):
            changeEverythingCost += abs(arr[index] - brr[index])
        
        for curr1, curr2 in zip(sorted(arr), sorted(brr)):
            changeAndRearrange += abs(curr1 - curr2)
        
        return min(changeAndRearrange + k, changeEverythingCost)
        