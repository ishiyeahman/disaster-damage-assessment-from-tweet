import tweepy
import authentication as ac

# api = tweepy.API(consumer_key=auth.consumer_key,
#                   consumer_secret=auth.consumer_secret,
#                   access_token_key=auth.access_token,
#                   access_token_secret=auth.access_token_secret,
#                   tweet_mode='extended')

auth = tweepy.OAuth1UserHandler(
    ac.consumer_key, ac.consumer_secret, ac.access_token, ac.access_token_secret
)

api = tweepy.API(auth)

"""
def get_deta_position():
    results = api.search_tweets(
    q="台風")
"""
# get_deta_position()
def main():
    tweets = api.search_tweets(q="台風") # you should write here your query something like about disaster key word, but you wouldn't get the place data,  sometime.
    print(tweets)

"""
def get_datas():
    tweets = api.search_tweets(q="吹き返し")
    for tw in tweets:
        place = tw._json['place']
        user = tw._json['user']
        # desc = tw._json['description']
        # print(user['name'])
        if not (tw._json['is_quote_status']):
            print(tw)
    # if user['geo_enabled']:
    #     print(tw._json['place'])
        # print(print(user))~
"""

# for tw in tweets:
#     # print(tw.name)
#     print(tw)       
#tweepy.Cursor(api.search, q="風", geocode="35.6467139,139.707889,1km").items()

main()