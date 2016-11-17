from textblob import TextBlob

class NLP():
    def __init__(self, tweets):
        self.tweets = tweets
        self.polarity = {}

    def processTweets(self):
        for tweet in self.tweets:
            if tweet['text'][0] == '@':
                continue
            self.polarity[tweet['id']] = {}
            self.polarity[tweet['id']]['polarity'] = self.getPolarity(tweet)
            self.polarity[tweet['id']]['date'] = tweet['created_at']
            self.polarity[tweet['id']]['favorites'] = tweet['favorite_count']
            self.polarity[tweet['id']]['retweets'] = tweet['retweet_count']
            self.polarity[tweet['id']]['is_retweet'] = tweet['text'][0:2] == "RT"
            self.polarity[tweet['id']]['text'] = tweet['text']
        return self.polarity

    def getPolarity(self, tweet):
        proc = TextBlob(tweet['text'])
        polarity = proc.sentiment.polarity
        return polarity
