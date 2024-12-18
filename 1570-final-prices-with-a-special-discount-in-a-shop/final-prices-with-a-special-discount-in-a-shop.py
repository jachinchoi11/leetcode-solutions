class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # monotonic stack from the top, the next smaller or equal to element 
        # next smallest element 
        stack = []
        discount = [0] * len(prices)
        for index, price in enumerate(prices):
            if stack:
                while stack and price <= prices[stack[-1]]:
                    discount[stack[-1]] = price
                    stack.pop()
                stack.append(index)
            else:
                stack.append(index)
        
        for index in range(len(prices)):
            prices[index] -= discount[index]
        
        return prices

