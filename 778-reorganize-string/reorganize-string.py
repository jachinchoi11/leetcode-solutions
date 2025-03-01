class Solution:
    def reorganizeString(self, s: str) -> str:
        
        # essetnialy you're given a stirng, and then we kind of have to construct a string whreer no two adjace cahracters 
        # yeah so im wondeirng what do you do in the case, aaaa, ""
        # the total length of our answerr has to match the length of the input string and if not then we can return "" 


        # prioritizing the higher frequency numbers 
            # just because when you do this, and have say 3 a's, 1b and 1c 
            # we would wnat to use a whenever possible and then use the next highest 
            # and that will ensure we will get any every possible rearrangement 
        
        # 1. creating a hashmap mapping the character (as the key), and the frequency (as the value)
        
        # 2. pushing this into a pq 
            # so that we can kind of priorizie the higher numbers (make sure to make this. - , as the defualt implementation is -
            # decrement when we use, and then there has to be some cooldown feature 
                # we can put it in a queue 
                    # for one and then pop it back in later 
         
        # 3. simulating through and while heap, we woudl keep on going
            # if we are ever in a scenario where we don't have nayting in the heap --> we can reutrn false

        res = []
        frequency_map = Counter(s) 
        heap = []
        timeout = deque()
        time = 0

        # s = "aaab"
        # a, b, a 
        # freq_map = {a: 3, b: 1}
        # heap = [(b,-1)]
        # queue = []
        # 
        # [-2, a, 1]
        # res = [a, b]


        for key, value in frequency_map.items():
            heapq.heappush(heap, (-value, key))
        
        while heap:
            print(heap, res, timeout)
            curr_freq, curr_char = heapq.heappop(heap)
            curr_freq *= -1
            curr_freq -= 1 
            res.append(curr_char)
            if curr_freq > 0:
                timeout.append((curr_freq, curr_char, time))
            while timeout and timeout[0][2] < time:
                new_freq, new_char, _ = timeout.popleft()
                heapq.heappush(heap, (-new_freq, new_char))
            time += 1
        
        return "".join(res) if len(res) == len(s) else ""
        

        

        

