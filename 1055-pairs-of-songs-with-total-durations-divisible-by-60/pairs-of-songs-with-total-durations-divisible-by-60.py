class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        # yes so essentially, we can only use it if it is after 

        # so maybe as we go we can store it in a hashmap 

        count = defaultdict(int)

        res = 0

        for curr_time in time:
            converted_time = curr_time % 60
            target = 60 - converted_time
            if target in count:
                res += count[target]
            if target == 60:
                res += count[0]
            count[converted_time] += 1
        
        return res

