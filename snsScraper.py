# import pandas as pd
# from tqdm.notebook import tqdm
# import snscrape.modules.twitter as sntweeter

# scraper = sntweeter.TwitterSearchScraper(query="#layoffs")

# tweets = []
# for i, tweet in enumerate(scraper.get_items()):
#     data = [
#         # tweet.date,
#         # tweet.id,
#         tweet.rawContent
#         # tweet.user.username,
#         # tweet.likeCount,
#         # tweet.retweetCount
#     ]
#     tweets.append(data)
#     if i == 5001:
#         break

# contents = pd.DataFrame(tweets, columns=["Tweets"])

# contents.to_csv("contents.csv")

