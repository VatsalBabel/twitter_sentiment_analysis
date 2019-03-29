import tweepy
from textblob import TextBlob

#API tokens
consumer_API_Key = 'o7NVeEy5YTfDZoMp0ph32xUx6'
consumer_secret_Key = 'sqTpBQmUEsj1m5hcw99IoV8bRdxIqvdtfTe4oaZRrmB54OwUV5'
access_token = '863604438925180928-NYA8x1cbuNeqN9rv5tlrHfqKM1rJnts'
access_token_secret = 'dMqS46Ch14jh0wpS9ijC0gqcRk5mgjBVjevm3aWH6UGNC'

#Tweepy auth
auth = tweepy.OAuthHandler(consumer_API_Key, consumer_secret_Key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#Keyword input
search = input('Enter search keyword - ')
tweets = api.search(search)

#Sentiment analyzing
for tweet in tweets:
	print(tweet.text)
	tweet = TextBlob(tweet.text)
	print(tweet.sentiment)
