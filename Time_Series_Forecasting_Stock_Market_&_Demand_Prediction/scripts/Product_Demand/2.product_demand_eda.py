import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
demand_df=pd.read_csv(r'D:\Projects\DATA_ANALYST_PROJECTS\Time_Series_Forecasting_Stock_Market_&_Demand_Prediction\data\product_demand_cleaned.csv',parse_dates=['Date'])

# Daily demand of product
daily_df=demand_df.groupby('Date')['Order_Demand'].sum().reset_index()

plt.figure(figsize=(12,6))
plt.plot(daily_df['Date'],daily_df['Order_Demand'])
plt.title('Product demand over time')
plt.xlabel('Date')
plt.ylabel('Product Demand')
plt.tight_layout()
plt.savefig('D:\Projects\DATA_ANALYST_PROJECTS\Time_Series_Forecasting_Stock_Market_&_Demand_Prediction/visuals\Product_demand/Product demand over time.png')
plt.show()

# Top 10 product by demand
top_products=demand_df.groupby('Product_Code')['Order_Demand'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(12,6))
sns.barplot(top_products.index,top_products.values)
plt.title('Top 10 Product by demand')
plt.xlabel('Product')
plt.ylabel(' Total Demand')
plt.tight_layout()
plt.savefig('D:\Projects\DATA_ANALYST_PROJECTS\Time_Series_Forecasting_Stock_Market_&_Demand_Prediction/visuals\Product_demand/Top 10 Product by demand')
plt.show()


# Top 5 Category by demand
top_category=demand_df.groupby('Product_Category')['Order_Demand'].sum().sort_values(ascending=False).reset_index().head()

plt.figure(figsize=(10,6))
sns.barplot(y=top_category['Product_Category'],x=top_category['Order_Demand'],orient='h')
plt.title('Top 5 Category by Demand')
plt.xlabel('Total Demand')
plt.ylabel('Category')
plt.tight_layout()
plt.savefig('D:\Projects\DATA_ANALYST_PROJECTS\Time_Series_Forecasting_Stock_Market_&_Demand_Prediction/visuals\Product_demand/Top 5 Category by Demand')
plt.show()