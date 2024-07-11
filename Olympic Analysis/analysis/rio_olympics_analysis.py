import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the preprocessed dataset
athlete_df = pd.read_csv('D:\Projects\DATA_ANALYST_PROJECTS\Olympic Analysis\data/processed_athlete_events.csv')

# Rio Olympics Gold Medals
goldmedal_rio = athlete_df[(athlete_df['Year'] == 2016) & (athlete_df['Medal'] == 'Gold')]['Team']
goldmedal_rio = goldmedal_rio.value_counts()

# Visualizing the Gold Medal country in Rio Olympics
plt.figure(figsize=(15,7))
sns.barplot(x=goldmedal_rio.head(15).values, y=goldmedal_rio.head(15).index, orient='h')
plt.title('Countrywise Gold Medal in Rio Olympics')
plt.xlabel('Number of Medals')
plt.ylabel('Country')
plt.savefig('D:\Projects\DATA_ANALYST_PROJECTS\Olympic Analysis/visualizations/rio_olympics_gold_medals.png')
plt.show()
