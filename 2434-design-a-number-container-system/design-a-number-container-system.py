class NumberContainers:
    # so i think in this case we can have a hashmap with the numbers and their lowest index
    # so in case that number gets replaced, we also need to account for that edge case, so essentially, we have to keep track of all the other instances 
    # so that if it does get replaced somewhere we can look and find the next minimum index

    def __init__(self):
        self.index_tracker = defaultdict(list)
        self.number_tracker = dict()
    
    def change(self, index: int, number: int) -> None:

        if number in self.index_tracker:
            heapq.heappush(self.index_tracker[number], (index))
        else:
            self.index_tracker[number].append(index)
        
        self.number_tracker[index] = number
    
    def find(self, number):
        if number in self.index_tracker:
            # if the number is in this, then we have to keep on popping until we find 
            while self.index_tracker[number]:
                current_index = heapq.heappop(self.index_tracker[number])
                if current_index in self.number_tracker and self.number_tracker[current_index] == number:
                    heapq.heappush(self.index_tracker[number], current_index)
                    return current_index
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)