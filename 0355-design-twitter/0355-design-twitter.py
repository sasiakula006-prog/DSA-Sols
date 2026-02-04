class Twitter(object):

    def __init__(self):
        self.time_posted = 0
        self.followers_list = defaultdict(set) # Dictionary of Sets so there is no repeating followers
        self.tweets = defaultdict(list) # Dictionary of lists for the the tweets  
        

    def postTweet(self, userId, tweetId):
        self.time_posted -= 1 # Negative value for the max heap use
        self.tweets[userId].append([self.time_posted, tweetId])
        

    def getNewsFeed(self, userId):
        max_heap = []
        recent_tweets = []
        count = 0
        
        if self.tweets[userId]:
            for tweet in self.tweets[userId][-10:]:
                heapq.heappush(max_heap, tweet) 
        
        for followerId in self.followers_list[userId]:
            if followerId in self.tweets:
                for tweet in self.tweets[followerId][-10:]:
                    heapq.heappush(max_heap, tweet) 
        
        while count < 10 and max_heap :
            _, recent_tweet = heapq.heappop(max_heap)
            recent_tweets.append(recent_tweet)
            count += 1
        
        return recent_tweets
        
        
    def follow(self, followerId, followeeId):
        if followeeId not in self.followers_list[followerId]:
            self.followers_list[followerId].add(followeeId)
        
        

    def unfollow(self, followerId, followeeId):
        if followeeId in self.followers_list[followerId]:
            self.followers_list[followerId].discard(followeeId) 
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)