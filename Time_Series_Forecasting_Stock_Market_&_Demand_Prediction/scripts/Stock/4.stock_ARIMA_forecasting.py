import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
import warnings
warnings.filterwarnings('ignore')

# Load dataset
stock_df=pd.read_csv('D:\Projects\DATA_ANALYST_PROJECTS\Time_Series_Forecasting_Stock_Market_&_Demand_Prediction\data\stock_data_cleaned.csv',parse_dates=['Date'])

# Set Index to 'Date'
stock_df.set_index('Date',inplace=True)

# Build and Fit ARIMA model
model=ARIMA(stock_df['Close'],order=(1,1,1))
model_fit=model.fit()

# Print model summary
print(model_fit.summary())

#Forecast next 30 day
forecast=model_fit.forecast(steps=30)
forecast.plot(title='Stock Price Forecast - ARIMA')
plt.xlabel('Time Step (Days)')
plt.ylabel('Forecasted Close Price')
plt.grid(True)
plt.savefig('D:\Projects\DATA_ANALYST_PROJECTS\Time_Series_Forecasting_Stock_Market_&_Demand_Prediction/visuals\Stock/Stock Price Forecast - ARIMA.png')
plt.show()

forecast.to_csv('D:\Projects\DATA_ANALYST_PROJECTS\Time_Series_Forecasting_Stock_Market_&_Demand_Prediction\data/forecast_stock_arima.csv',index=False)
print("✅ Forecast Stock ARIMA saved")