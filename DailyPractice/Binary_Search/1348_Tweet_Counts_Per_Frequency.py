class TweetCounts:
    import collections
    import bisect
    def __init__(self):
        self.record = collections.defaultdict(list)

    def recordTweet(self, tweetName, time):
        bisect.insort(self.record[tweetName], time)

    def getTweetCountsPerFrequency(self, freq, tweetName, startTime, endTime):
        time_to_seconds_mapping = {'minute': 60, 'hour': 3600, 'day': 86400}
        delta = time_to_seconds_mapping[freq]
        ans = []
        while startTime <= endTime:
            frequency = bisect.bisect_left(self.record[tweetName],
                                           min(endTime + 1, startTime + delta)) - bisect.bisect_left(
                self.record[tweetName], startTime)
            ans.append(frequency)
            startTime += delta
        return ans



        # Your TweetCounts object will be instantiated and called as such:
        # obj = TweetCounts()
        # obj.recordTweet(tweetName,time)
        # param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)