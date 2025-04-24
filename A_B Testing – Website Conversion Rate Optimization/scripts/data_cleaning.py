import pandas as pd

# Load dataset
df=pd.read_csv('D:\Projects\DATA_ANALYST_PROJECTS\A_B Testing – Website Conversion Rate Optimization\data/ab_data.csv')

# Shape of Dataset
df.shape

# Display Information
df.info()

# Remove Duplicates
df.dropna(inplace=True)

# Considering only 
# control -> old_page
# treatment -> new_page

df=df[((df['group'] == 'control') & (df['landing_page'] == 'old_page')) | 
      ((df['group'] == 'treatment') & (df['landing_page'] == 'new_page')) ]

# Convert timestamp to datetime
df['timestamp']=pd.to_datetime(df['timestamp'])

# Reset index
df.reset_index(drop=True,inplace=True)

# Save cleaned data
df.to_csv('D:\Projects\DATA_ANALYST_PROJECTS\A_B Testing – Website Conversion Rate Optimization\data/ab_cleaned_data.csv',index=False)
print('Saved CSV file')