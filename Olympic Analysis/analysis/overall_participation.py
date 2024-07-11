import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the preprocessed dataset
athlete_df = pd.read_csv('D:\Projects\DATA_ANALYST_PROJECTS\Olympic Analysis\data/processed_athlete_events.csv')

# Top Countries Participating
top_10_countries = athlete_df['Team'].value_counts().sort_values(ascending=False).head(10)

# Visualizing
plt.figure(figsize=(12,7))
sns.barplot(x=top_10_countries.index, y=top_10_countries.values)
plt.title('Overall Participation by Country')
plt.xlabel('Country')
plt.ylabel('Number of Participants')
plt.savefig('D:\Projects\DATA_ANALYST_PROJECTS\Olympic Analysis/visualizations/overall_participation.png')
plt.show()
