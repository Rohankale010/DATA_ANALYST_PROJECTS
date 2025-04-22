import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet

# Load and prepare 
demand_df=pd.read_csv(r'D:\Projects\DATA_ANALYST_PROJECTS\Time_Series_Forecasting_Stock_Market_&_Demand_Prediction\data\product_demand_cleaned.csv',parse_dates=['Date'])
demand_df_grouped=demand_df.groupby('Date')['Order_Demand'].sum().reset_index()
df_prophet_demand=demand_df_grouped.rename(columns={'Date':'ds','Order_Demand':'y'})

# Build and Fit Model
demand_model=Prophet(daily_seasonality=True)
demand_model.fit(df_prophet_demand)

# Forecast 30 days ahead
future_demand_model=demand_model.make_future_dataframe(periods=30)
forecast_demand_model=demand_model.predict(future_demand_model)


# Plot
demand_model.plot(forecast_demand_model)
plt.title('Product Demand Forecast - Prophet')
plt.savefig('D:\Projects\DATA_ANALYST_PROJECTS\Time_Series_Forecasting_Stock_Market_&_Demand_Prediction/visuals\Product_demand/Product Demand Forecast - Prophet.png')
plt.show()

demand_model.plot_components(forecast_demand_model)
plt.savefig('D:\Projects\DATA_ANALYST_PROJECTS\Time_Series_Forecasting_Stock_Market_&_Demand_Prediction/visuals\Product_demand/Product Demand Forecast Components - Prophet.png')
plt.show()

forecast_demand_model.to_csv('D:\Projects\DATA_ANALYST_PROJECTS\Time_Series_Forecasting_Stock_Market_&_Demand_Prediction\data/forecast_demand_prophet.csv',index=False)
print("✅ Forecast Demand Prophet saved")
