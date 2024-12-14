class Twitter:
    def __init__(self):
        self.posts = defaultdict(list)
        self.followers = defaultdict(set)
        self.curr = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((-self.curr, tweetId))
        self.curr += 1
    def getNewsFeed(self, userId: int) -> List[int]:
        print(self.posts[userId])
        heap = []
        res = []
        for tweet in self.posts[userId][-10:]:
            heapq.heappush(heap, tweet)
        
        for follower in self.followers[userId]:
            for tweet in self.posts[follower][-10:]:
                heapq.heappush(heap, tweet)
        print(heap)
        while heap and len(res) < 10:
            res.append(heapq.heappop(heap)[1])
        return res
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers:
            self.followers[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)