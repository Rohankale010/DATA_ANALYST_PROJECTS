import pandas as pd
from statsmodels.tsa.stattools import adfuller

# Load dataset
stock_df=pd.read_csv('D:\Projects\DATA_ANALYST_PROJECTS\Time_Series_Forecasting_Stock_Market_&_Demand_Prediction\data\stock_data_cleaned.csv',parse_dates=['Date'])

# Sort by 'Date'
stock_df['Date']=stock_df['Date'].sort_values(ascending=True)

# Feature Engineering
stock_df['Day']=stock_df['Date'].dt.day
stock_df['Month']=stock_df['Date'].dt.month
stock_df['Year']=stock_df['Date'].dt.year
stock_df['Daily_Return']=(stock_df['Close']-stock_df['Open'])/stock_df['Open']
stock_df['Volatility']=(stock_df['High']-stock_df['Low'])/stock_df['Open']
stock_df['7D_MA_Close']=stock_df['Close'].rolling(window=7).mean()
stock_df['30D_MA_Close']=stock_df['Close'].rolling(window=30).mean()
stock_df['LAG_Close']=stock_df['Close'].shift(1)
stock_df['LAG_Volume']=stock_df['Volume'].shift(1)

# Save into dataset
stock_df.to_csv('D:\Projects\DATA_ANALYST_PROJECTS\Time_Series_Forecasting_Stock_Market_&_Demand_Prediction\data/stock_features.csv',index=False)
print('✅ Stock Feature saved')

# ADF Test
adf_result = adfuller(stock_df['Close'].dropna())
print(f"ADF Statistic: {adf_result[0]}")
print(f"p-value: {adf_result[1]}")

# Now we making it Stationary
stock_df.set_index('Date',inplace=True)

stock_df['Close_diff']=stock_df['Close'].diff()

adf_result=adfuller(stock_df['Close_diff'].dropna())

# ADF Test again
print(f"ADF Statistic: {adf_result[0]}")
print(f"p-value: {adf_result[1]}")