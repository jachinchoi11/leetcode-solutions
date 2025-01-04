class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.user = collections.defaultdict(set)
        self.heap = []
        self.tasks = {}
        for userId, taskId, priority in tasks:
            self.user[userId].add(taskId)
            self.tasks[taskId] = [priority, userId]
            heapq.heappush(self.heap, [-priority, -taskId, userId])
        
    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.user[userId].add(taskId)
        self.tasks[taskId] = [priority, userId]
        heapq.heappush(self.heap, [-priority, -taskId, userId])

    def edit(self, taskId: int, newPriority: int) -> None:
        if newPriority != self.tasks[taskId][0]:
            _ , curr_user = self.tasks[taskId]
            self.tasks[taskId][0] = newPriority
            heapq.heappush(self.heap, [-newPriority, -taskId, curr_user])

    def rmv(self, taskId: int) -> None:
        priority, curr_user = self.tasks[taskId]
        self.user[curr_user].remove(taskId)
        self.tasks.pop(taskId)

    def execTop(self) -> int:
        while self.heap:
            prio, curr_task, curr_user = heapq.heappop(self.heap)
            prio *= -1
            curr_task *= -1
            if curr_task not in self.tasks or self.tasks[curr_task][0] != prio:
                continue
            self.tasks.pop(curr_task)
            self.user[curr_user].remove(curr_task)
            return curr_user
        return -1
        


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()