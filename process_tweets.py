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


tweets = ProcessTweets("data/elonmusk_tweets.json").process()
timeFormat ='%a %b %d %H:%M:%S %z %Y' 
total = 0
yes = 0
no = 0
st = StockThing()
for tweetid, tweet in tweets.items():
    if 'next' not in tweet:
        break
    tweetDate = datetime.datetime.strptime(tweet['date'], timeFormat).strftime('%m/%d/%Y')
    nextTweetDate = datetime.datetime.strptime(tweets[tweet['next']]['date'], timeFormat).strftime('%m/%d/%Y')
    change = st.getStockChange(tweetDate, nextTweetDate)
    if type(change) != str:
        if float(tweet['polarity']) * float(change) >= 0.0:
            yes += 1
        else:
            no += 1
        total += 1

# sanity check
assert total == yes + no
print('Stats:')
print('--------------------')
print('Correlation:', yes)
print('No correlation:', no)
print('Total:', total)
print('--------------------')
print('Average successfully correlated:', (yes) / total)
