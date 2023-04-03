import os
import tweepy
from utils.file_utils import *

path = "tweets"
count_file = f'{path}/tweet_count.txt'
tweets_file = f'{path}/trading_tweets.txt'

def main():
    client = tweepy.Client(consumer_key = os.environ.get('CONSUMER_KEY'), 
                           consumer_secret = os.environ.get('CONSUMER_SECRET'), 
                           access_token = os.environ.get('ACCESS_TOKEN'), 
                           access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET'))

    count = get_tweet_count(count_file)
    tweet = get_tweet(tweets_file, count)
    print(tweet)

    response = client.create_tweet(text=tweet)
    print(response)
 
if __name__ == "__main__":
    main()