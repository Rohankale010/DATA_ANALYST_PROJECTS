import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
deliveries_df = pd.read_csv('D:\Projects\DATA_ANALYST_PROJECTS\IPL Analysis (2008-2023)\data\deliveries.csv')
matches_df = pd.read_csv('D:\Projects\DATA_ANALYST_PROJECTS\IPL Analysis (2008-2023)\data\matches.csv')

# Merge the datasets
ipl_df = pd.merge(deliveries_df, matches_df, left_on='match_id', right_on='id', how='outer')

# Filter data for IPL 2023 season
ipl_2023 = ipl_df[ipl_df['season'] == '2023']

# Most runs in 2023
runs_2023 = ipl_2023.groupby('batter')['batsman_runs'].sum().reset_index(name='runs')
mostruns_2023 = runs_2023.sort_values(by='runs', ascending=False)

# Visualizing top 5 Most run scorer in 2023
plt.figure(figsize=(10,6))
sns.barplot(data=mostruns_2023, x=mostruns_2023['batter'].head(), y=mostruns_2023['runs'].head())
plt.title('Most Runs Score in IPL 2023')
plt.xlabel('Batsman Name')
plt.ylabel('Runs')
plt.savefig('D:\Projects\DATA_ANALYST_PROJECTS\IPL Analysis (2008-2023)/visualizations/top_run_scorers_2023.png')
plt.show()

# Most wickets in 2023
mostwicket_2023 = ipl_2023[ipl_2023['is_wicket'] == 1]['bowler'].value_counts().reset_index(name='wickets')

# Visualizing top 5 Most wicket takers in 2023
plt.figure(figsize=(10,6))
sns.barplot(data=mostwicket_2023, x=mostwicket_2023['index'].head(), y=mostwicket_2023['wickets'].head(), palette='viridis')
plt.title('Most Wicket-taking Bowler in IPL 2023')
plt.xlabel('Bowler Name')
plt.ylabel('Wickets')
plt.savefig('D:\Projects\DATA_ANALYST_PROJECTS\IPL Analysis (2008-2023)/visualizations/top_wicket_takers_2023.png')
plt.show()

# Trophy wins by team
trophy = ipl_df[ipl_df['match_type'] == 'Final'][['winner', 'season']].value_counts().reset_index()
trophy = trophy['winner'].value_counts().reset_index(name='trophy')
trophy.rename(columns={'index': 'Team_Name'}, inplace=True)

# Visualization for Number of Trophy Wins
plt.pie(x=trophy['trophy'], labels=trophy['Team_Name'], autopct=lambda trophy_count: f"{trophy_count * trophy['trophy'].sum() / 100:.0f}")
plt.title('Number of Trophy Win by a Team')
plt.savefig('D:\Projects\DATA_ANALYST_PROJECTS\IPL Analysis (2008-2023)/visualizations/trophy_wins.png')
plt.show()
