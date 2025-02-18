from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # first course of action, we count the number of times a number appears in teh array (nums)

        # second one is going to be using some sort of a sorting algorithm to get the top k frequent ones
            # in this case, since we're not doing any modficiations or adding any new values into the heap
            # we can just sort it using the lambda sort function and output the top k elements
        
        counter_map = defaultdict(int)
        unsorted_list = []
        res = []

        for num in nums:
            counter_map[num] += 1
        
        for key, value in counter_map.items():
            key_value_pair = [key, value]
            unsorted_list.append(key_value_pair)
        unsorted_list.sort(key =lambda x: -x[1])

        for i in range(k):
            res.append(unsorted_list[i][0])

        return res

