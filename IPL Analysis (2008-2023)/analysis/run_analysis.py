import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
deliveries_df = pd.read_csv('D:\Projects\DATA_ANALYST_PROJECTS\IPL Analysis (2008-2023)\data\deliveries.csv')
matches_df = pd.read_csv('D:\Projects\DATA_ANALYST_PROJECTS\IPL Analysis (2008-2023)\data\matches.csv')

# Merge the datasets
ipl_df = pd.merge(deliveries_df, matches_df, left_on='match_id', right_on='id', how='outer')

# Count the runs scored by each batsman
runs_count = ipl_df.groupby('batter')['batsman_runs'].sum().reset_index()
most_run = runs_count.sort_values(by='batsman_runs', ascending=False).reset_index(drop=True)

# Visualizing Top 5 Run Scorer
plt.figure(figsize=(15,6))
sns.barplot(data=most_run, x=most_run['batter'].head(10), y=most_run['batsman_runs'].head(10))
plt.title('Most Run Scorer Batsman in IPL')
plt.xlabel('Name')
plt.ylabel('Runs')
plt.savefig('D:\Projects\DATA_ANALYST_PROJECTS\IPL Analysis (2008-2023)/visualizations/top_run_scorers.png')
plt.show()

# Grouping runs by season for a specific player
player_runs = ipl_df[ipl_df['batter'] == 'V Kohli'].groupby('season')['batsman_runs'].sum().reset_index()

# Plotting
plt.figure(figsize=(12,6))
sns.lineplot(data=player_runs, x='season', y='batsman_runs', marker='o')
plt.title('Runs Scored by Virat Kohli Across Seasons')
plt.xlabel('Season')
plt.ylabel('Runs')
plt.savefig('D:\Projects\DATA_ANALYST_PROJECTS\IPL Analysis (2008-2023)/visualizations/kohli_runs_by_season.png')
plt.show()
