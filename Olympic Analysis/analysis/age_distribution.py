import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the preprocessed dataset
athlete_df = pd.read_csv('D:\Projects\DATA_ANALYST_PROJECTS\Olympic Analysis\data/processed_athlete_events.csv')

# Age Distribution of Athletes
plt.figure(figsize=(12,6))
plt.hist(x=athlete_df['Age'], bins=np.arange(10,80,2), color='orange', edgecolor='white')
plt.title('Age Distribution of Athletes')
plt.xlabel('Age')
plt.ylabel('Number of Participants')
plt.savefig('D:\Projects\DATA_ANALYST_PROJECTS\Olympic Analysis/visualizations/age_distribution.png')
plt.show()
