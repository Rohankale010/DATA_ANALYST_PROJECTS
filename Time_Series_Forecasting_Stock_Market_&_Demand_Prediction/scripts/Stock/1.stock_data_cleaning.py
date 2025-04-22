import pandas as pd

# Loading the Dataset
stock_df=pd.read_csv('D:\Projects\DATA_ANALYST_PROJECTS\Time_Series_Forecasting_Stock_Market_&_Demand_Prediction\data/raw_stock_data.csv.csv')

# Convert 'Date' to datetime
stock_df['Date']=pd.to_datetime(stock_df['Date'])

# Sorting values according to Date column
stock_df.sort_values(by='Date').reset_index(drop=True,inplace=True)

# Droping Null and Missing values
stock_df.dropna(inplace=True)

# Saving cleaned data
stock_df.to_csv('D:\Projects\DATA_ANALYST_PROJECTS\Time_Series_Forecasting_Stock_Market_&_Demand_Prediction\data/stock_data_cleaned.csv',index=False)
print("✅ Stock market dataset cleaned and saved.")