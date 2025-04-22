
# 📈 Time Series Forecasting: Stock Market & Demand Prediction

This project focuses on building time series forecasting models using **ARIMA** and **Prophet** to predict future trends in both **stock prices** and **product demand**. The goal is to enable data-driven decisions for inventory planning and financial investments through interactive Power BI dashboards.

---

## 📌 Project Objectives

- Forecast **product demand** to optimize inventory management and supply chain planning.
- Predict **stock market prices** to support financial analysis and decision-making.
- Use **ARIMA** and **Prophet** models for time series forecasting.
- Build visually interactive **Power BI dashboards** to present trends and model insights.

---


## 📁 Project Structure

```
Time_Series_Forecasting_Project/
│
├── data/
│   ├── forecast_demand_arima.csv  
│   ├── forecast_demand_prophet.csv
│   ├── forecast_stock_arima.csv
│   ├── forecast_stock_prophet.csv  
│   ├── product_demand_cleaned.csv
│   ├── product_demand_features.csv
│   ├── raw_demand_data.csv.csv
│   ├── raw_stock_data.csv.csv
│   ├── stock_data_cleaned.csv
│   └── stock_features.csv
│
├── scripts/
│   ├── Product_Demand/
│   │     ├── 1.product_demand_cleaning.py
│   │     ├── 2.product_demand_eda.py
│   │     ├── 3.product_demand_feature_engineering_and_stationary_check.py
│   │     ├── 4.product_demand_ARIMA_forecasting.py
│   │     └── 5.product_demand_Prophet_forecasting.py
│   │     
│   └── Stock/
│         ├── 1.stock_data_cleaning.py 
│         ├── 2.stock_eda.py
│         ├── 3.stock_feature_engineering_and_stationary_check.py
│         ├── 4.stock_ARIMA_forecasting.py
│         └── 5.stock_Prophet_forecasting.py
│
├── notebooks/
│   ├── Product_Demand/
│   │     ├── 1.product_demand_cleaning.ipynb
│   │     ├── 2.product_demand_eda.ipynb
│   │     ├── 3.product_demand(Feature engineering and Stationary check).ipynb
│   │     ├── 4.product_demand(ARIMA forecasting).ipynb
│   │     └── 5.product_demand(Prophet forecasting).ipynb
│   │     
│   └── Stock/
│         ├── 1.stock_data_cleaning.ipynb 
│         ├── 2.stock_eda.ipynb
│         ├── 3.stock(Feature engineering and Stationary check).ipynb
│         ├── 4.stock(ARIMA forecasting).ipynb
│         └── 5.stock(Prophet forecasting).ipynb
│
├── dashboards/
│   ├── Stock_Market_Forecasting_Dashboard.pbix
│   └── Product_Demand_Forecasting_Dashboard.pbix
│
├── visuals/
│   ├── Product_Demand/
│   │     ├── Product Demand Forecast - ARIMA.png
│   │     ├── Product Demand Forecast - Prophet.png
│   │     ├── Product Demand Forecast Components - Prophet.png
│   │     ├── Product demand over time.png
│   │     ├── Top 10 Product by demand.png
│   │     └── Top 5 Category by Demand.png
│   │     
│   └── Stock/
│         ├── Closing Price over time.png 
│         ├── Moving Average.png
│         ├── Stock Close Price Forecast - Prophet.png
│         ├── Stock Close Price Forecast Components - Prophet.png
│         └── Stock Price Forecast - ARIMA.png
│
├── README.md
└── requirements.txt
```

---

## 🗃️ Datasets Used

### 1. Stock Market Dataset
- **Source**: Kaggle
- **Columns**: `Date`, `Open`, `High`, `Low`, `Close`, `Adj Close`, `Volume`

### 2. Product Demand Dataset
- **Source**: Kaggle
- **Columns**: `Product_Code`, `Warehouse`, `Product_Category`, `Date`, `Order_Demand`

---

## 🔍 Project Workflow

### ✅ Step 1: Data Collection & Cleaning
- Handled null values, duplicates, and irrelevant columns.
- Converted `Date` columns to datetime and set as index.
- Checked for and ensured proper time intervals and continuity.

### ✅ Step 2: Feature Engineering
- For stock data: Calculated daily returns, volatility.
- For demand data: Aggregated `Order_Demand` at daily level per product/warehouse.

### ✅ Step 3: Stationarity Check
- **Product Demand**: Already stationary → no differencing needed.
- **Stock Data**: Used ADF test and differencing to achieve stationarity.

### ✅ Step 4: Forecasting Models
- **ARIMA**: Applied after ensuring stationarity and identifying (p,d,q) using ACF/PACF.
- **Prophet**: Used for trend-based forecasting and holiday-aware predictions.
- Models built separately for stock and demand datasets.

### ✅ Step 5: Visualization in Power BI
- Designed two dashboards:
  - **Stock Market Forecasting Dashboard**
  - **Product Demand Forecasting Dashboard**
- Included: KPIs, time series charts, forecast overlays, model accuracy.

---

## 💡 Key Insights

- Stock prices showed volatile patterns; Prophet handled trends better.
- Product demand patterns helped reveal warehouse-level inventory needs.
- Dashboards provide intuitive visualizations for both domains.

---

## 🛠️ Tools & Technologies

- **Python**: pandas, numpy, matplotlib, seaborn, statsmodels, fbprophet
- **Power BI**: For building forecasting dashboards
- **Jupyter Notebooks**: For EDA and model development
- **VS Code**: Project development

---

## ✅ How to Run

1. Clone the repo and navigate to the project directory.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run notebooks or scripts for forecasting.
4. View the `.pbix` dashboards in Power BI Desktop.

---

## 📊 Power BI Dashboards

- `Stock_Market_Forecasting_Dashboard.pbix`
 ![Stock Market Forecasting Dashboard](<dashboard/Stock_Market_Forecasting_Dashboard.png>)
- `Product_Demand_Forecasting_Dashboard.pbix`
 ![Product Demand Forecasting Dashboard](<dashboard/Product_Demand_Forecasting_Dashboard.png>)
---



