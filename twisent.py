import tweepy
from textblob import TextBlob
import matplotlib.pyplot as plt
import re
import pandas as pd
from collections import deque
from matplotlib.animation import FuncAnimation
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')

api_key = 'YOUR_API_KEY'
api_key_secret = 'YOUR_API_KEY_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

topic = "Python"
tweet_limit = 100

def clean(text):
    text = re.sub(r'@[A-Za-z0-9]+', '', text)
    text = re.sub(r'https?://[A-Za-z0-9./]+', '', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text.strip()

def vader_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    scores = analyzer.polarity_scores(clean(text))
    return scores['compound']

def textblob_sentiment(text):
    analysis = TextBlob(clean(text))
    return analysis.sentiment.polarity

def fetch_data():
    tweets = api.search_tweets(q=topic, count=tweet_limit)
    vader_scores = [vader_sentiment(tweet.text) for tweet in tweets]
    textblob_scores = [textblob_sentiment(tweet.text) for tweet in tweets]
    tweet_texts = [tweet.text for tweet in tweets]
    return tweet_texts, vader_scores, textblob_scores

def save_data(tweet_texts, vader_scores, textblob_scores):
    df = pd.DataFrame({
        'Tweet': tweet_texts,
        'VADER_Sentiment': vader_scores,
        'TextBlob_Sentiment': textblob_scores
    })
    df.to_csv('tweet_sentiments.csv', index=False)

class LiveSentimentAnalysis:
    def __init__(self, interval=1000):
        self.fig, self.ax = plt.subplots()
        self.vader_scores = deque([0]*tweet_limit, maxlen=tweet_limit)
        self.textblob_scores = deque([0]*tweet_limit, maxlen=tweet_limit)
        self.animation = FuncAnimation(self.fig, self.refresh, interval=interval)
        plt.title("Live Twitter Sentiment Analysis")
        plt.xlabel("Time")
        plt.ylabel("Sentiment")

    def refresh(self, frame):
        tweet_texts, latest_vader_scores, latest_textblob_scores = fetch_data()
        self.vader_scores.extend(latest_vader_scores)
        self.textblob_scores.extend(latest_textblob_scores)
        save_data(tweet_texts, latest_vader_scores, latest_textblob_scores)
        self.ax.clear()
        self.ax.plot(self.vader_scores, label='VADER Sentiment')
        self.ax.plot(self.textblob_scores, label='TextBlob Sentiment')
        self.ax.legend()
        self.ax.set_title("Live Twitter Sentiment Analysis")
        self.ax.set_xlabel("Time")
        self.ax.set_ylabel("Sentiment")

    def show(self):
        plt.show()

if __name__ == "__main__":
    live_analysis = LiveSentimentAnalysis()
    live_analysis.show()
