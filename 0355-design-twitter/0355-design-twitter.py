class Twitter:

    def __init__(self):
        self.totalTweets = 0  # Decrement the value as tweets get posted to construct the minHeap
        self.followMap = defaultdict(set)  # {followerId: {followeeIds}}
        self.tweetMap = defaultdict(list)  # {userId: [(totalTweets, tweetId)]}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.totalTweets, tweetId))
        self.totalTweets -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        
        self.followMap[userId].add(userId)  # Include userId in their own following list to access their own tweets
        # Iterate over the users the current user follows, including themselves
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                idx = len(self.tweetMap[followeeId]) - 1
                tot, tweetId = self.tweetMap[followeeId][idx]  # Get the most recent tweet
                heapq.heappush(minHeap, [tot, followeeId, tweetId, idx - 1])
        
        # Collect the 10 most recent tweets from the heap
        while minHeap and len(res) < 10:
            _, followeeId, tweetId, idx = heapq.heappop(minHeap)
            res.append(tweetId)
            if idx >= 0:
                tot, tweetId = self.tweetMap[followeeId][idx]  # Get the next most recent tweet from this user
                heapq.heappush(minHeap, [tot, followeeId, tweetId, idx - 1])
                
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)
        

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)