import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
stock_df=pd.read_csv('D:\Projects\DATA_ANALYST_PROJECTS\Time_Series_Forecasting_Stock_Market_&_Demand_Prediction\data\stock_data_cleaned.csv',parse_dates=['Date'])

# Plot Closing Price over time 
plt.figure(figsize=(10,6))
plt.plot(stock_df['Date'],stock_df['Close'],label='Closing Price',color='blue')
plt.title('Stock Market - Closing Price over time')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.grid(True)
plt.tight_layout()
plt.legend()
plt.savefig('D:\Projects\DATA_ANALYST_PROJECTS\Time_Series_Forecasting_Stock_Market_&_Demand_Prediction/visuals\Stock/Closing Price over time.png')
plt.show()

# Moving Average
stock_df['MA_30']=stock_df['Close'].rolling(window=30).mean()
stock_df['MA_90']=stock_df['Close'].rolling(window=90).mean()

plt.figure(figsize=(10,6))
plt.plot(stock_df['Date'],stock_df['Close'],label='Closing Price',alpha=0.5)
plt.plot(stock_df['Date'],stock_df['MA_30'],label='30 Day MA',color='green')
plt.plot(stock_df['Date'],stock_df['MA_90'],label='90 Day MA',color='red')
plt.title('Stock Market - Moving Average')
plt.xlabel('Date')
plt.ylabel('Price')
plt.tight_layout()
plt.legend()
plt.savefig('D:\Projects\DATA_ANALYST_PROJECTS\Time_Series_Forecasting_Stock_Market_&_Demand_Prediction/visuals\Stock/Moving Average.png')
plt.show()