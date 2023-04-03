def get_tweet_counter(file):
    with open(file, "r") as f:
        counter = f.read()
        counter = int(counter)
    return counter

def update_tweet_counter(counter, file):
    with open(file, "w") as f:
        f.write(str(counter+1))
    

def get_tweet(file, counter):
    with open(file, "r") as f:
        tweets = f.readlines()
    return tweets[counter]

def randomize_write(tweets, file):
    import random
    random.shuffle(tweets)

    with open(file, "a") as f:
        for tweet in tweets:
            f.write(str(tweet))