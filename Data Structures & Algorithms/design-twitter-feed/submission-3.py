class Twitter:

    def __init__(self):
        self.users = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        tweet = (self.time, tweetId)
        self.tweets[userId].append(tweet)

        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        ids = [userId]
        ids.extend(self.users[userId])

        minHeap = []
        for id in ids:
            for tweet in self.tweets[id]:
                heapq.heappush(minHeap, tweet)
                if len(minHeap) > 10:
                    heapq.heappop(minHeap)

        res = []
        while minHeap:
            res.append(heapq.heappop(minHeap)[1])
        
        return res[::-1]


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)
