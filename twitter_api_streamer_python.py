from tweepy import API
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import twitter_creds
import numpy as np
import pandas as pd
# TWITTER CLIENT


class TwitterClient():
    def __init__(self, twitter_user=None):  # if it is none it will go to default user_timeline
        self.auth = TwitterAuthenticator().authenticate_twitter_app()
        self.twitter_client = API(self.auth)
        self.twitter_user = twitter_user

    def get_twitter_client_api(self):
        return self.twitter_client

    def get_user_timeline_tweets(self, num_tweets):
        tweets = []
        for tweet in Cursor(self.twitter_client.user_timeline, id=self.twitter_user).items(num_tweets):
            tweets.append(tweet)
        return tweets

    def get_friend_list(self, num_friends):
        friend_list = []
        for friend in Cursor(self.twitter_client.friends, id=self.twitter_user).items(num_friends):
            friend_list.append(friend)
        return friend_list

    def get_home_timeline_tweets(self, num_tweets):
        home_timeline_tweets = []
        for tweet in Cursor(self.twitter_client.home_timeline, id=self.twitter_user).items(num_tweets):
            home_timeline_tweets.append(tweet)
        return home_timeline_tweets


# AUTHENTICATOR CLASS
class TwitterAuthenticator():

    def authenticate_twitter_app(self):
        auth = OAuthHandler(twitter_creds.ACCESS_KEY, twitter_creds.ACCESS_KEY_SECRET)
        auth.set_access_token(twitter_creds.ACCESS_TOKEN, twitter_creds.ACCESS_TOKEN_SECRET)
        return auth

# STREAMER CLASS


class TwitterStreamer():
    """
    class for streaming and processing tweets
    """

    def __init__(self):
        self.twitter_authenticator = TwitterAuthenticator()

    def stream_tweets(self, fetched_tweeets_filename, hash_tag_list):
        listener = TwitterListener(fetched_tweeets_filename)
        auth = self.twitter_authenticator.authenticate_twitter_app()
        stream = Stream(auth, listener)
        stream.filter(track=hash_tag_list)

# LISTENER CLASS


class TwitterListener(StreamListener):  # inheritance of StreamListener Class
    """
    This is a basic listener class that will print all tweets in the STDOUT
    """

    def __init__(self, fetched_tweeets_filename):
        self.fetched_tweeets_filename = fetched_tweeets_filename

    def on_data(self, data):  # StreamListener class provides 2 methods  - on_data and on_error
        try:
            print(data)
            with open(self.fetched_tweeets_filename, 'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("Error on data: %s" % str(e))
        return True

    def on_error(self, status):
        if status == 420:
            return false
        print(status)


class TweetAnalyzer():
    """
    Functionality for analysing and categorizing cotent from tweets.
    """
    pass


if __name__ == "__main__":

    hash_tag_list = ["AMDOCS", "TELECOM"]
    fetched_tweeets_filename = "tweets.json"
    twitter_client = TwitterClient('pyconindia')
    print(twitter_client.get_user_timeline_tweets(1))
    print(twitter_client.get_home_timeline_tweets(2))
    print(twitter_client.get_friend_list(1))
    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweeets_filename, hash_tag_list)
