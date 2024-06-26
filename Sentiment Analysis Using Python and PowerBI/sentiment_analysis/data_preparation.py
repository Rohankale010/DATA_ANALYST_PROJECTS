# sentiment_analysis/data_preparation.py

import pandas as pd
import re
import nltk
from nltk.corpus import stopwords

# Ensure the necessary resources are downloaded
nltk.download('stopwords')

# Load the dataset
df = pd.read_csv('D:\Projects\DATA_ANALYST_PROJECTS\Sentiment Analysis Using Python and PowerBI\data/raw/training.1600000.processed.noemoticon.csv', names=['target', 'id', 'date', 'flag', 'user', 'text'], encoding='latin1')

# Drop unnecessary columns
df = df.drop(['target', 'id', 'date', 'flag', 'user'], axis=1)

# Function to clean text
def cleaned_text(text):
    if isinstance(text, str):
        text = re.sub(r'http\S+|www.\S+', '', text)
        text = re.sub(r'[^A-Za-z\s]', '', text)
        text = text.lower()
        text = ' '.join([word for word in text.split() if word not in stopwords.words('english')])
        return text
    else:
        return ''

# Apply the cleaning function to the text
df['text'] = df['text'].apply(cleaned_text)

# Save the cleaned data to a CSV file
df.to_csv('D:\Projects\DATA_ANALYST_PROJECTS\Sentiment Analysis Using Python and PowerBI\data\processed/cleaned_data.csv', index=False)

print("Data preparation completed successfully.")
