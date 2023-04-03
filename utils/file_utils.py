def get_tweet_count(file):
    with open(file, "r") as f:
        count = f.read()
        count = int(count)

    with open(file, "w") as f:
        f.write(str(count+1))

    return count

def get_tweet(file, count):
    with open(file, "r") as f:
        tweets = f.readlines()
    return tweets[count]

def randomize_write(tweets, file):
    import random
    random.shuffle(tweets)

    with open(file, "a") as f:
        for tweet in tweets:
            f.write(str(tweet))