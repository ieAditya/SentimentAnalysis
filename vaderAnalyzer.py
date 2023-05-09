import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

df = pd.read_csv("contents.csv")

sentiment = []

for i in df["Tweets"]:
    a = i
    if analyzer.polarity_scores(a)["compound"] < -0.05:
        sentiment.append(-1)
    elif analyzer.polarity_scores(a)["compound"] > 0.35:
        sentiment.append(1)
    elif (
        analyzer.polarity_scores(a)["compound"] >= -0.05
        and analyzer.polarity_scores(a)["compound"] <= 0.35
    ):
        sentiment.append(0)

df.insert(2, "Sentiment", sentiment, True)

df.to_csv("TweetsWithSentiments.csv")


print(
    "\n\n\nSentiment for each tweet labeled as -1:Negative 0:Neutral 1:Positive and saved to 'TwwetsWithSentiment.csv'.\n\n\n\n"
)
