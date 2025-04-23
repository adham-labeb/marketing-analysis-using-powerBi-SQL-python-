import nltk
import pandas as pd
from rich import print
from configparser import ConfigParser
from nltk.sentiment.vader import SentimentIntensityAnalyzer



nltk.download('vader_lexicon')

config = ConfigParser(allow_no_value=True)
config.read('config.ini')


def fetch_data_from_csv() -> pd.DataFrame:

    df: pd.DataFrame = \
        pd.read_csv('out/fact_customer_reviews.csv')
    

    return df


customer_reviews_df = fetch_data_from_csv()


sia = SentimentIntensityAnalyzer()


def calculate_sentiment(review: str) -> float:

    sentiment = sia.polarity_scores(review)

    return sentiment['compound']


def categorize_sentiment(score: float, rating: int) -> str:

    if score > 0.05:
        if rating >= 4:
            return 'Positive'
        elif rating == 3:
            return 'Mixed Positive'
        else:
            return 'Mixed Negative'
    elif score < -0.05:
        if rating <= 2:
            return 'Negative'
        elif rating == 3:
            return 'Mixed Negative'
        else:
            return 'Mixed Positive'
    else:
        if rating >= 4:
            return 'Positive'
        elif rating <= 2:
            return 'Negative'
        else:
            return 'Neutral'


def sentiment_bucket(score: float) -> str:
    if score >= 0.5:
        return '0.5 to 1.0'
    elif 0.0 <= score < 0.5:
        return '0.0 to 0.49'
    elif -0.5 <= score < 0.0:
        return '-0.49 to 0.0'
    else:
        return '-1.0 to -0.5'


customer_reviews_df['SentimentScore'] = \
    customer_reviews_df['ReviewText'].apply(calculate_sentiment)


customer_reviews_df['SentimentCategory'] = \
    customer_reviews_df.apply(
    lambda row: categorize_sentiment(row['SentimentScore'],
    row['Rating']), axis=1
    )


customer_reviews_df['SentimentBucket'] = \
    customer_reviews_df['SentimentScore'].apply(sentiment_bucket)


print(customer_reviews_df.head())


customer_reviews_df.to_csv('out/fact_customer_reviews_modified.csv', index=False)
