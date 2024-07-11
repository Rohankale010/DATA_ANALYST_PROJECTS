import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
deliveries_df = pd.read_csv('D:\Projects\DATA_ANALYST_PROJECTS\IPL Analysis (2008-2023)\data\deliveries.csv')
matches_df = pd.read_csv('D:\Projects\DATA_ANALYST_PROJECTS\IPL Analysis (2008-2023)\data\matches.csv')

# Merge the datasets
ipl_df = pd.merge(deliveries_df, matches_df, left_on='match_id', right_on='id', how='outer')

# Calculate number of 4s and 6s for each batsman
boundary_counts = ipl_df.groupby('batter')['batsman_runs'].value_counts().unstack(fill_value=0)
boundary_counts = boundary_counts[[4, 6]].rename(columns={4: 'Fours', 6: 'Sixes'})
boundary_counts['Total_Boundaries'] = boundary_counts['Fours'] + boundary_counts['Sixes']

# Select top 10 batsmen based on total boundaries
top_10_batsmen = boundary_counts.sort_values(by='Total_Boundaries', ascending=False).head(10)

# Plotting
top_10_batsmen[['Fours', 'Sixes']].plot(kind='bar', stacked=True, figsize=(15,5))
plt.title('Top 10 Batsmen by Boundaries')
plt.xlabel('Batsman')
plt.ylabel('Number of Boundaries')
plt.xticks(rotation=0)
plt.legend(title='Type of Boundary')
plt.savefig('D:\Projects\DATA_ANALYST_PROJECTS\IPL Analysis (2008-2023)/visualizations/top_boundary_scorers.png')
plt.show()
