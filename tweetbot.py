import os
import tweepy
from utils.file_utils import *

counter_file = 'utils/tweet_counter.txt'
tweets_file = 'tweets/trading_tweets.txt'

def main():
    client = tweepy.Client(consumer_key = os.environ.get('CONSUMER_KEY'), 
                           consumer_secret = os.environ.get('CONSUMER_SECRET'), 
                           access_token = os.environ.get('ACCESS_TOKEN'), 
                           access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET'))

    count = get_tweet_count(counter_file)
    tweet = get_tweet(tweets_file, count)
    print(tweet)

    response = client.create_tweet(text=tweet)
    print(response)
 
if __name__ == "__main__":
    main()