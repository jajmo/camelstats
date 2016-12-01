from textblob import TextBlob

class NLP():
    def __init__(self, tweets):
        self.tweets = tweets
        self.polarity = {}

    def processTweets(self):
        for tweet in self.tweets:
            if tweet['text'][0] == '@':
                continue
            self.polarity[tweet['id']] = {
                'polarity': self.getPolarity(tweet),
                'date': tweet['created_at'],
                'favorites': tweet['favorite_count'],
                'retweets': tweet['retweet_count'],
                'is_retweet': tweet['text'][0:2] == "RT",
                'text': tweet['text']
            }

        return self.polarity

    def getPolarity(self, tweet):
        proc = TextBlob(tweet['text'])
        polarity = proc.sentiment.polarity
        return polarity
