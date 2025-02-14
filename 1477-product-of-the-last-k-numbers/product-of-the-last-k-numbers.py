from collections import deque

class ProductOfNumbers:

    def __init__(self):
        self.prefixMult = [1]  # Store prefix products (1-based indexing for easy division)
    
    def add(self, num: int) -> None:
        if num == 0:
            self.prefixMult = [1]  # Reset on zero
        else:
            self.prefixMult.append(self.prefixMult[-1] * num)  # Maintain prefix product

    def getProduct(self, k: int) -> int:
        if k >= len(self.prefixMult):  
            return 0  # Zero exists in range

        return self.prefixMult[-1] // self.prefixMult[-k-1]  # Compute product efficiently
