import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet

# Load and prepare 
stock_df=pd.read_csv('D:\Projects\DATA_ANALYST_PROJECTS\Time_Series_Forecasting_Stock_Market_&_Demand_Prediction\data\stock_data_cleaned.csv',parse_dates=['Date'])
df_prophet_stock=stock_df[['Date','Close']].rename(columns={'Date':'ds','Close':'y'})

# Build and Fit Model
model_stock=Prophet(daily_seasonality=True)
model_stock.fit(df_prophet_stock)

# Forecast 30 days ahead
future_stock=model_stock.make_future_dataframe(periods=30)
forecast_stock=model_stock.predict(future_stock)

# Plot
model_stock.plot(forecast_stock)
plt.title("Stock Close Price Forecast - Prophet")
plt.savefig('D:\Projects\DATA_ANALYST_PROJECTS\Time_Series_Forecasting_Stock_Market_&_Demand_Prediction/visuals\Stock/Stock Close Price Forecast - Prophet.png')
plt.show()

model_stock.plot_components(forecast_stock)
plt.savefig('D:\Projects\DATA_ANALYST_PROJECTS\Time_Series_Forecasting_Stock_Market_&_Demand_Prediction/visuals\Stock/Stock Close Price Forecast Components - Prophet.png')
plt.show()

forecast_stock.to_csv('D:\Projects\DATA_ANALYST_PROJECTS\Time_Series_Forecasting_Stock_Market_&_Demand_Prediction\data/forecast_stock_prophet.csv',index=False)
print("✅ Forecast Stock Prophet saved")