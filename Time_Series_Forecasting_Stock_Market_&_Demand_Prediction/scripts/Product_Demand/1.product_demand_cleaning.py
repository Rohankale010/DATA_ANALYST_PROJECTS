import pandas as pd

# Load dataset
demand_df=pd.read_csv(r'D:\Projects\DATA_ANALYST_PROJECTS\Time_Series_Forecasting_Stock_Market_&_Demand_Prediction\data\raw_demand_data.csv.csv')

# Convert 'Date' to datetime
demand_df['Date']=pd.to_datetime(demand_df['Date'])

# Convert unwanted character of 'Order_Demand' and changing to numeric
demand_df['Order_Demand']=demand_df['Order_Demand'].str.strip()
demand_df['Order_Demand']=demand_df['Order_Demand'].replace('[^0-9]','',regex=True)
demand_df['Order_Demand']=pd.to_numeric(demand_df['Order_Demand'],errors='coerce')

# Droping missing and null values
demand_df.dropna(inplace=True)

# Removing Negative values
demand_df=demand_df[demand_df['Order_Demand']>=0]

# Sort values according to 'Date'
demand_df.sort_values(by='Date',inplace=True)

# Reset Index
demand_df.reset_index(drop=True,inplace=True)

# Save cleaned data
demand_df.to_csv('D:\Projects\DATA_ANALYST_PROJECTS\Time_Series_Forecasting_Stock_Market_&_Demand_Prediction\data/product_demand_cleaned.csv',index=False)
print("✅ Product demand dataset cleaned and saved.")