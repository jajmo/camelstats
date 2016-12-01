from textblob import TextBlob
import collections

class NLP():
    def __init__(self, tweets):
        self.tweets = sorted(tweets, key = lambda x: x['id'])
        self.polarity = collections.OrderedDict({})

    def processTweets(self):
        prevID = None
        prevDate = None
        for tweet in self.tweets:
            if tweet['text'][0] == '@' or tweet['created_at'][0:10] == prevDate:
                continue

            if (prevID != None):
                self.polarity[prevID]['next'] = tweet['id']
            self.polarity[tweet['id']] = {
                'polarity': self.getPolarity(tweet),
                'date': tweet['created_at'],
                'likes': tweet['favorite_count'],
                'retweets': tweet['retweet_count'],
                'is_retweet': tweet['text'][1:2] == "RT",
                'text': tweet['text']
            }
            prevID = tweet['id']
            prevDate = tweet['created_at'][0:10]

        return self.polarity

    def getPolarity(self, tweet):
        proc = TextBlob(tweet['text'])
        polarity = proc.sentiment.polarity
        return polarity
