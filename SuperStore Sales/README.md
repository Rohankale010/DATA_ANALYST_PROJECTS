### SuperStore Sales Dashboard and Forecasting

## Table of Contents

- [Project Overview](#project-overview)
- [Project Structure](#project-structure)
- [Objective](#objective)
- [Dataset](#dataset)
- [Tools Used](#tools-used)
- [Key Insights](#key-insights)
- [Visualizations](#visualizations)
- [Conclusion](#conclusion)

## Project Overview
The SuperStore Sales Dashboard and Forecasting project aims to analyze sales data from a retail store to provide insights into sales performance, profit, and future sales predictions. This dashboard helps stakeholders make data-driven decisions to optimize sales strategies and improve profitability.

## Project Structure
```plaintext
SuperStore Sales Dashboard/
    ├── data/
    │   ├── SuperStore_Sales_Dataset.csv
    │
    ├── analysis/
    │   ├── analysis.md
    │
    ├── dashboard/
    │   ├── SuperStore Sales Dashboard.pbix
    │   ├── SuperStore Sales Forecasting.pbix
    │   ├── SuperStore Sales Dashboard.png
    │   ├── SuperStore Sales Forecasting.png
    │
    ├── README.md
    ├── requirements.txt
```

## Objective
To analyze sales data and provide actionable insights into sales performance, profitability, and future sales trends.

## Dataset
- **Source:** Retail Store Sales Data
- **Fields:** Order ID, Product ID, Category, Sub-Category, Sales, Quantity, Profit, Discount, Ship Mode, Region, State, Segment, Order Date, Ship Date

## Tools Used
- **Power BI:** Used for data visualization and analysis.

## Key Insights
1. **Sales by Payment Mode:**
   - Cards: 22%
   - COD: 43%
   - Online: 35%
2. **Sales by Segment:**
   - Home Office: 19%
   - Corporate: 43%
   - Consumer: 38%
3. **Sales by Region:**
   - South: 19%
   - West: 32%
   - Central: 29%
   - East: 20%
4. **Monthly Sales Year on Year:**
   - Sales show an increasing trend year on year.
5. **Monthly Profit Year on Year:**
   - Profit shows significant variations throughout the year.
6. **Sales by Category:**
   - Office Supplies: 0.64M
   - Technology: 0.47M
   - Furniture: 0.45M
7. **Sales by Sub-Category:**
   - Phones: 0.24M
   - Chairs: 0.18M
   - Binders: 0.17M
8. **Sales by Ship Mode:**
   - Standard Class: 0.91%
   - Second Class: 0.1%
   - First Class: 0.24%
   - Same Day: 0.1%
9. **Profit and Sales by Location:**
   - Highest sales and profit in specific locations.
10. **Sales Forecasting 15 Days:**
    - Predicts sales trends for the next 15 days.
11. **Sales by State:**
    - California: 0.34M
    - New York: 0.19M
    - Texas: 0.12M
    - Washington: 0.11M
    - Pennsylvania: 0.12M

## Visualizations
1. **SuperStore Sales Dashboard:**
   - Key indicators and comparisons of sales metrics.
   - Pie charts for sales by payment mode and segment.
   - Line charts for monthly sales and profit year on year.
   - Bar charts for sales by category and sub-category.
   - Map visualization for profit and sales by location.
   ![SuperStore Sales Dashboard](<dashboard/SuperStore Sales Dashboard.png>)

2. **SuperStore Sales Forecasting:**
   - Line charts for 15-day sales forecasting.
   - Bar chart for sales by state.
   ![SuperStore Sales Forecasting](<dashboard/SuperStore Sales Forecasting.png>)

## Conclusion
The SuperStore Sales Dashboard and Forecasting project provides a comprehensive analysis of sales data, identifying key trends and insights to help stakeholders optimize sales strategies and improve profitability. The visualizations in Power BI effectively present the data, making it easy to interpret and act upon.