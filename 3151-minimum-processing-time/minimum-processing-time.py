class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        # so i think you jsut solve this in a greedy way, get the tasks that take the maximum times 
        # get it in groups of 4 using a heap (only care about the highest in the group)
        # and then just add the time 

        taskTime = [-time for time in tasks]
        heapq.heapify(taskTime)
        processor_time_pointer = 0
        processorTime.sort()
        res = 0

        while taskTime:
            time = -heapq.heappop(taskTime)
            self.eraseThree(taskTime)
            res = max(processorTime[processor_time_pointer] + time, res)
            processor_time_pointer += 1
        return res

    def eraseThree(self, taskTime):
        for i in range(3):
            heapq.heappop(taskTime)
