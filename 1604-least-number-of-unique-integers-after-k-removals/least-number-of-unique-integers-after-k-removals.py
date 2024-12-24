class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        # we want to have the leas tnumber o funique integers after k amount of removals 
        # essentialyw ecan just be greedy and take away the lowest frequencye 


        count = Counter(arr)

        minHeap = [(cnt, num) for num, cnt in count.items()]
        heapq.heapify(minHeap)

        while k > 0:
            currCount, num = heapq.heappop(minHeap)
            if k < currCount:
                break
            else:
                k -= count[num]
                print(num)
                count.pop(num)
        print(count)
        return len(count)