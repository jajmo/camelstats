import nlp
import json

class ProcessTweets:

    def __init__(self, filename):
        self.filename = filename

    def process(self):
        with open(self.filename, "r") as tweets:
            x = nlp.NLP(json.loads(tweets.read()))
        return json.dumps(x.processTweets())

if __name__ == "__main__":
    print(ProcessTweets("elonmusk_weets.json").process())
