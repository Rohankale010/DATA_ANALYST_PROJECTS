# sentiment_analysis/sentiment_analysis.py

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Load the cleaned dataset
df = pd.read_csv('D:\Projects\DATA_ANALYST_PROJECTS\Sentiment Analysis Using Python and PowerBI\data\processed\cleaned_data.csv')

# Initialize the SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

# Function to analyze sentiment
def analyze_sentiment(text):
    if isinstance(text, str):
        score = analyzer.polarity_scores(text)
        return score['compound']
    else:
        return 0

# Apply the sentiment analysis function
df['Sentiment_score'] = df['text'].apply(analyze_sentiment)

# Classify the sentiment based on the sentiment score
df['Sentiment'] = df['Sentiment_score'].apply(lambda x: 'Positive' if x > 0 else ('Negative' if x < 0 else 'Neutral'))

# Save the data with sentiment analysis to a new CSV file
df.to_csv('D:\Projects\DATA_ANALYST_PROJECTS\Sentiment Analysis Using Python and PowerBI\data\processed/tweets_sentiments.csv', index=False)

print("Sentiment analysis completed successfully.")
