class Leaderboard:
    # so essentially, you have a leaderboard class that keeps track of the highest score for each player id 
    # if we were to reset the player id, maybe make sure that we have a hashmap with the most recent data 
    # and then we will have a heap, since k can be different, we can just compute it as we go 
    def __init__(self):
        self.score_tracker = {}
    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.score_tracker:
            self.score_tracker[playerId] += score
        else:
            self.score_tracker[playerId] = score
        
    def top(self, K: int) -> int:
        # i think for this one, we can jus make it inside of here and try to brute force the answer to it
        heap = []
        sum_of_scores = 0
        for key, value in self.score_tracker.items():
            heapq.heappush(heap, (-value, key))
        
        for times in range(K):
            value, _ = heapq.heappop(heap)
            sum_of_scores += (-value)
        
        return sum_of_scores

    def reset(self, playerId: int) -> None:
        self.score_tracker[playerId] = 0

