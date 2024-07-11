import pandas as pd

# Load the Dataset
athlete = pd.read_csv('D:\Projects\DATA_ANALYST_PROJECTS\Olympic Analysis\data/athlete_events.csv')
region = pd.read_csv('D:\Projects\DATA_ANALYST_PROJECTS\Olympic Analysis\data/noc_regions.csv')

# Merge the two datasets
athlete_df = athlete.merge(region, how='left', on='NOC')
athlete_df.rename(columns={'region': 'Region', 'notes': 'Notes'}, inplace=True)

# Save the preprocessed data
athlete_df.to_csv('D:\Projects\DATA_ANALYST_PROJECTS\Olympic Analysis\data/processed_athlete_events.csv', index=False)
