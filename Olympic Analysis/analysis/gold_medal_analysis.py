import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the preprocessed dataset
athlete_df = pd.read_csv('D:\Projects\DATA_ANALYST_PROJECTS\Olympic Analysis\data/processed_athlete_events.csv')

# Gold Medal Analysis
gold_medal = athlete_df[athlete_df['Medal'] == 'Gold']
gold_medal = gold_medal[np.isfinite(gold_medal['Age'])]

# Gold Medal for Athletes over Age 60
sport_event = gold_medal['Sport'][gold_medal['Age'] > 60]
plt.figure(figsize=(8,4))
sns.countplot(sport_event)
plt.title('Gold Medal for Athletes over Age 60')
plt.savefig('D:\Projects\DATA_ANALYST_PROJECTS\Olympic Analysis/visualizations/gold_medals_over_60.png')
plt.show()

# Gold Medals for each Country
top_5_goldmedal = gold_medal['Region'].value_counts().reset_index(name='Medals').head()
plt.figure(figsize=(8,5))
sns.barplot(data=top_5_goldmedal, x='index', y='Medals', palette='rocket')
plt.title('Gold Medals per Country')
plt.xlabel('Country')
plt.ylabel('Number of Medals')
plt.savefig('D:\Projects\DATA_ANALYST_PROJECTS\Olympic Analysis/visualizations/gold_medals_per_country.png')
plt.show()
