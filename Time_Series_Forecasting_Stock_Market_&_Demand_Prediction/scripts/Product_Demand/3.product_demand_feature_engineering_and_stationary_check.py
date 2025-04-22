import pandas as pd
from statsmodels.tsa.stattools import adfuller

# Load dataset
demand_df=pd.read_csv(r'D:\Projects\DATA_ANALYST_PROJECTS\Time_Series_Forecasting_Stock_Market_&_Demand_Prediction\data\product_demand_cleaned.csv',parse_dates=['Date'])

# Sort by 'Date'
demand_df['Date']=demand_df['Date'].sort_values(ascending=True)

# Feature engineering
demand_df['Day']=demand_df['Date'].dt.day
demand_df['Month']=demand_df['Date'].dt.month
demand_df['Year']=demand_df['Date'].dt.year

# Aggregate demand per day
agg_demand=demand_df.groupby('Date')['Order_Demand'].sum().reset_index(name='Total_Demand')

# Rolling and Lag features
agg_demand['7D_MA_demand']=agg_demand['Total_Demand'].rolling(window=7).mean()
agg_demand['30D_MA_demand']=agg_demand['Total_Demand'].rolling(window=30).mean()
agg_demand['LAG_demand']=agg_demand['Total_Demand'].shift(1)

# Save into dataset
demand_df.to_csv('D:\Projects\DATA_ANALYST_PROJECTS\Time_Series_Forecasting_Stock_Market_&_Demand_Prediction\data/product_demand_features.csv',index=False)
print('✅ Demand Feature saved')

# ADF test
adf_result=adfuller(agg_demand['Total_Demand'].dropna())
print(f"ADF Statistic: {adf_result[0]}")
print(f"p-value: {adf_result[1]}")