class Twitter:

    def __init__(self):
        self.users = defaultdict(set)
        self.tweets = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        followees = self.users[userId]
        newsfeed = []

        count = 0
        for i in range(len(self.tweets) - 1, -1, -1):
            if count == 10:
                break
            
            if self.tweets[i][0] == userId or self.tweets[i][0] in followees:
                newsfeed.append(self.tweets[i][1])
                count += 1
            
        return newsfeed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)

    
