import nlp
import json

with open("elonmusk_tweets.json", "r") as tweets:
    x = nlp.NLP(json.loads(tweets.read()))
    print(json.dumps(x.processTweets(), indent = 4, separators = (',', ': '), sort_keys = True))
    tweets.close()