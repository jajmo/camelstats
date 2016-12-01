import nlp
import json
import datetime
from stockReader import StockThing

class ProcessTweets:
    def __init__(self, filename):
        self.filename = filename

    def process(self):
        with open(self.filename, "r") as tweets:
            x = nlp.NLP(json.loads(tweets.read()))
        #return json.dumps(x.processTweets(), indent = 4, separators = (',', ': '), sort_keys = True)
        return x.processTweets()


tweets = ProcessTweets("elonmusk_tweets.json").process()
timeFormat ='%a %b %d %H:%M:%S %z %Y' 
#increase = 0
#decrease = 0
total = 0
yes = 1
no = 0
for tweetid, tweet in tweets.items():
    if 'next' not in tweet:
        break
    tweetDate = datetime.datetime.strptime(tweet['date'], timeFormat).strftime('%m/%d/%Y')
    nextTweetDate = datetime.datetime.strptime(tweets[tweet['next']]['date'], timeFormat).strftime('%m/%d/%Y')
    change = StockThing.getStockChange(tweetDate, nextTweetDate)
    if type(change) != str:
        if float(tweet['polarity']) * float(change) >= 0.0:
            yes += 1
        else:
            no += 1
        #if tweet['polarity'] >= 0 and change >= 0:
        #    increase += 1
        #elif tweet['polarity'] < 0 and change < 0:
        #    decrease += 1
        #else:
        #    no += 1
        total += 1

print('Stats:')
print('--------------------')
print('Correlation:', yes)
#print('Decrease:', decrease)
print('No correlation:', no)
print('Total:', total)
print('--------------------')
print('Average successfully correlated:', (yes) / total)
