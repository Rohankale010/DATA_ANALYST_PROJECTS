import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
deliveries_df = pd.read_csv('D:\Projects\DATA_ANALYST_PROJECTS\IPL Analysis (2008-2023)\data\deliveries.csv')
matches_df = pd.read_csv('D:\Projects\DATA_ANALYST_PROJECTS\IPL Analysis (2008-2023)\data\matches.csv')

# Merge the datasets
ipl_df = pd.merge(deliveries_df, matches_df, left_on='match_id', right_on='id', how='outer')

# Filter out the Non League Matches
qualify = ipl_df[ipl_df['match_type'] != 'League']

# Groupby to count the versus match of team according to season
qualifiers = qualify.groupby(['season', 'team1', 'team2']).size().reset_index()

# Count the number of occurrences of each team in team1 and team2
team1_counts = qualifiers['team1'].value_counts().reset_index()
team2_counts = qualifiers['team2'].value_counts().reset_index()

# Merge the both team counts
team = pd.merge(team1_counts, team2_counts, left_on=team1_counts['index'], right_on=team2_counts['index'], how='outer')
team.fillna(0, inplace=True)

# Sum the number of occurrences of each team to get total
team['Qualified'] = team['team1'].astype('int') + team['team2'].astype('int')
team.rename(columns={'key_0': 'team_name'}, inplace=True)
team = team[['team_name', 'Qualified']].sort_values(by='Qualified', ascending=False)

# Visualizing the Most Qualifying team in IPL
plt.figure(figsize=(20,8))
sns.barplot(data=team, y=team['team_name'], x=team['Qualified'], orient='h', palette='Spectral')
plt.title('Most Qualifying Teams in IPL')
plt.xlabel('Number of Times')
plt.ylabel('Teams')
plt.savefig('D:\Projects\DATA_ANALYST_PROJECTS\IPL Analysis (2008-2023)/visualizations/top_qualifying_teams.png')
plt.show()
