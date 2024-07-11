import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the preprocessed dataset
athlete_df = pd.read_csv('D:\Projects\DATA_ANALYST_PROJECTS\Olympic Analysis\data/processed_athlete_events.csv')

# Women Participation in Summer and Winter Olympics
women_olympics_summer = athlete_df[(athlete_df['Sex'] == 'F') & (athlete_df['Season'] == 'Summer')]
women_olympics_winter = athlete_df[(athlete_df['Sex'] == 'F') & (athlete_df['Season'] == 'Winter')]

plt.figure(figsize=(15,7))
sns.countplot(data=women_olympics_summer, x='Year', palette='Spectral')
plt.title('Women Participation in Summer')
plt.savefig('D:\Projects\DATA_ANALYST_PROJECTS\Olympic Analysis/visualizations/women_participation_summer.png')
plt.show()

plt.figure(figsize=(15,7))
sns.countplot(data=women_olympics_winter, x='Year', palette='Spectral')
plt.title('Women Participation in Winter')
plt.savefig('D:\Projects\DATA_ANALYST_PROJECTS\Olympic Analysis/visualizations/women_participation_winter.png')
plt.show()

plt.figure(figsize=(15,7))
women_olympics_summer.groupby('Year')['Sex'].value_counts().loc[:, 'F'].plot(label='Summer')
women_olympics_winter.groupby('Year')['Sex'].value_counts().loc[:, 'F'].plot(label='Winter')
plt.title('Women Athlete Participation over Time in Different Seasons')
plt.legend()
plt.savefig('D:\Projects\DATA_ANALYST_PROJECTS\Olympic Analysis/visualizations/women_participation_over_time.png')
plt.show()
