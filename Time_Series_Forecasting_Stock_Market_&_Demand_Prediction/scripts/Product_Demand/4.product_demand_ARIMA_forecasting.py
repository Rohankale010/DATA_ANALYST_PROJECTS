import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
import warnings
warnings.filterwarnings('ignore')

# Load dataset
demand_df=pd.read_csv(r'D:\Projects\DATA_ANALYST_PROJECTS\Time_Series_Forecasting_Stock_Market_&_Demand_Prediction\data\product_demand_cleaned.csv',parse_dates=['Date'])

agg_demand=demand_df.groupby('Date')['Order_Demand'].sum().reset_index()

# Set Index to 'Date'
agg_demand.set_index('Date',inplace=True)


# Build and Fit ARIMA model
model_demand=ARIMA(agg_demand['Order_Demand'],order=(1,0,1))
model_demand_fit=model_demand.fit()


# Print model summary
print(model_demand_fit.summary())

#Forecast next 30 day
demand_forecast=model_demand_fit.forecast(steps=30)
demand_forecast.plot(title='Product Demand Forecast - ARIMA')
plt.xlabel('Time Steps (Days)')
plt.ylabel('Forecasted Demand')
plt.grid(True)
plt.savefig('D:\Projects\DATA_ANALYST_PROJECTS\Time_Series_Forecasting_Stock_Market_&_Demand_Prediction/visuals\Product_demand/Product Demand Forecast - ARIMA.png')
plt.show()

demand_forecast.to_csv('D:\Projects\DATA_ANALYST_PROJECTS\Time_Series_Forecasting_Stock_Market_&_Demand_Prediction\data/forecast_demand_arima.csv',index=False)
print("✅ Forecast Demand ARIMA saved")







