class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        # so there's two factors, essentially, when he's actually grumpy to be not grumpy and then you want the biggest sliding window 
        # you would have save those indexes and then go about it after and get it 


        l = 0
        change_customers = 0
        max_change_customers = 0
        indexes = [0, minutes - 1]
        res = 0 

        for r in range(minutes):
            if grumpy[r] == 1:
                change_customers += customers[r]
        max_change_customers = change_customers
        r += 1

        while r < len(customers):
            if grumpy[r] == 1:
                change_customers += customers[r]
            if grumpy[l] == 1:
                change_customers -= customers[l]
            l += 1
            if change_customers > max_change_customers:
                max_change_customers = change_customers
                indexes = [l, r]
            r += 1
        
        for index, customer in enumerate(customers):
            if index >= indexes[0] and index <= indexes[1]:
                res += customers[index]
            else:
                if grumpy[index] == 0:
                    res += customers[index]
        print(indexes)
        return res