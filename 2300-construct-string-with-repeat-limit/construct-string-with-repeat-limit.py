class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        count = defaultdict(int)
        res = ""
        for char in s:
            count[char] += 1

        uniqueChars = set(s)
        currList = list(uniqueChars)
        heap = []

        for letter in currList:
            heapq.heappush(heap, (-ord(letter), letter))

        while heap:
            _, currChar = heapq.heappop(heap)
            if count[currChar] > repeatLimit:
                res += currChar * repeatLimit
                count[currChar] -= repeatLimit
                if heap:
                    _ , secondChar = heapq.heappop(heap)
                    res += secondChar
                    count[secondChar] -= 1
                    if count[secondChar] > 0:
                        heapq.heappush(heap, (-ord(secondChar), secondChar))
                else:
                    break
            else:
                res += currChar * count[currChar]
                count[currChar] -= count[currChar]
            if count[currChar] > 0:
                heapq.heappush(heap, (-ord(currChar),currChar))
        return res 

