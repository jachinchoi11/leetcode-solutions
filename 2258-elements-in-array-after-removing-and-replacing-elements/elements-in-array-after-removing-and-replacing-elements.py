class Solution:
    def elementInNums(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        # so let's make a hashmap for this entire thing, at a certian tikme
        # essentially, we can just keep track of the reminader from the len(nums) * 2

        length_at_time = {}
        queue = deque(nums)
        startingLength = len(nums)
        isDecreasing = True
        pointer = 0
        for i in range(len(nums) * 2 + 1):
            length_at_time[i] = list(queue)
            if len(queue) == 0:
                isDecreasing = False
            if isDecreasing:
                queue.popleft()
            else:
                if pointer < len(nums):
                    queue.append(nums[pointer])
                    pointer += 1

        res = [0] * len(queries)
        print(length_at_time)
        for i, (time, index) in enumerate(queries):
            remainder = (time % (len(nums) * 2))
            if len(length_at_time[remainder]) > index and remainder in length_at_time:
                res[i] = length_at_time[remainder][index]
            else:
                res[i] = -1
        
        return res



            