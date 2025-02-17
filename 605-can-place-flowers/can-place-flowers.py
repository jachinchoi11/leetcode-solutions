class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                continue
            if i == 0:
                if i == len(flowerbed) - 1 or flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    n -= 1
            elif i == len(flowerbed) - 1 and flowerbed[i - 1] == 0:
                if flowerbed[i - 1] == 0:
                    flowerbed[i] = 1
                    n -= 1
            elif flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                n -= 1
                flowerbed[i] = 1

        return True if n <= 0 else False
