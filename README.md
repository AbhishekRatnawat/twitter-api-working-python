# twitter-api-working-python

#file_name
twitter_api_streamer_python.py -

 - class TwitterAuthenticator(): - authenticate ACCESS_KEY and ACCESS_TOKEN

 - class TwitterClient(): - guides the information required about the user using the functions within class itself like home_timeline_tweets, get_user_timeline_tweets etc...

 - class TwitterStreamer(): - class for streaming and processing tweets

 - class TwitterListener(StreamListener): - This is a basic listener class that will print all tweets in the STDOUT


#file_name
analysis_tweets.py

 - class TweetAnalyzer(): - uses pandas to create DataFrames, Functionality for analysing and categorizing cotent from tweets.

#file_name
data_visualization.py
 - using the content of data frame ploting time-series graph using pandas and matplotlib

#file_name
sentimental_analysis.py
 - cleaning the data by removing the special characters in it and based on polarity classifying the tweet as - 0 , 1 , -1 
