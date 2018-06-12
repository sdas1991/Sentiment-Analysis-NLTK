from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_mod as s

#consumer key, consumer secret, access token, access secret.
ckey="5f8Lwi8l5rvwxrbUYw8Bw8Wtm"
csecret="D8et8VOLIUqL5kGrGKRX3fROtzLRGNlsxODvLZPKh9cu4F4vKv"
atoken="935598658216693760-nwn9RboniY4BxKICKb5xfJE6aOwYHAx"
asecret="sVj8zZ98zqs1LbvutjyvJGbYdk7I9vsXvvXJ12WpogN48"



class listener(StreamListener):
    def on_data(self, data):
        print("in on_data")
        all_data = json.loads(data)
        tweet = all_data["text"]
        sentiment_value, confidence =s.sentiment(tweet)
        if confidence *100 >=80:
            print(tweet,sentiment_value, confidence)
            output = open("twitter-out.txt","a")
            output.write(sentiment_value)
            output.write('\n')
            output.close()
        else:
            print(tweet, "neutral", confidence)
    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["Avengers: Infinity War"])