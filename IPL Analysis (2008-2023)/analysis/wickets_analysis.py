import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
deliveries_df = pd.read_csv('D:\Projects\DATA_ANALYST_PROJECTS\IPL Analysis (2008-2023)\data\deliveries.csv')
matches_df = pd.read_csv('D:\Projects\DATA_ANALYST_PROJECTS\IPL Analysis (2008-2023)\data\matches.csv')

# Merge the datasets
ipl_df = pd.merge(deliveries_df, matches_df, left_on='match_id', right_on='id', how='outer')

# Find the top wicket-takers
most_wicket = ipl_df[ipl_df['is_wicket'] == 1]['bowler'].value_counts().reset_index(name='Wicket')

# Visualize Top 10 Most wicket-taking Bowler in IPL
plt.figure(figsize=(15,6))
sns.barplot(data=most_wicket, x=most_wicket['index'].head(10), y=most_wicket['Wicket'].head(10), palette='magma')
plt.title('Most Wicket-taking Bowler in IPL')
plt.xlabel('Name')
plt.ylabel('Wickets')
plt.savefig('D:\Projects\DATA_ANALYST_PROJECTS\IPL Analysis (2008-2023)/visualizations/top_wicket_takers.png')
plt.show()

# Grouping wickets by season for a specific player
player_wickets = ipl_df[ipl_df['bowler'] == 'DJ Bravo'].groupby('season')['is_wicket'].sum().reset_index()

# Plotting
plt.figure(figsize=(12,6))
sns.lineplot(data=player_wickets, x='season', y='is_wicket', marker='o', color='purple')
plt.title('Wicket Taken by DJ Bravo Across Seasons')
plt.xlabel('Season')
plt.ylabel('Wickets')
plt.savefig('D:\Projects\DATA_ANALYST_PROJECTS\IPL Analysis (2008-2023)/visualizations/bravo_wickets_by_season.png')
plt.show()
