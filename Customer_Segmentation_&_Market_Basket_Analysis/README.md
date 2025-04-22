# Customer Segmentation & Market Basket Analysis

## 📌 Project Overview
This project applies data analytics techniques to segment customers based on their shopping behaviors and identify purchasing patterns using market basket analysis. The goal is to provide actionable insights for personalized marketing, customer retention, and revenue optimization.

## 📊 Datasets Used
1. **Mall Customer Segmentation Dataset**
   - Columns: `CustomerID`, `Gender`, `Age`, `Annual Income (k$)`, `Spending Score (1-100)`
   - Purpose: Used to cluster customers based on demographic and spending patterns.

2. **Market Basket Analysis Dataset**
   - Columns: `BillNo`, `Itemname`, `Quantity`, `Date`, `Price`, `CustomerID`, `Country`
   - Purpose: Used to uncover frequently bought-together items and generate association rules.

## 🔄 Implementation Steps
### **Phase 1: Customer Segmentation**
1. **Data Exploration & Preprocessing**
   - Checked for missing values and outliers
   - Visualized distributions of age, income, and spending scores
   - Identified correlations among features
2. **Clustering using K-Means**
   - Determined the optimal number of clusters using the Elbow Method and Knee Locator
   - Applied K-Means clustering to segment customers
3. **Cluster Analysis & Visualization**
   - Analyzed demographic characteristics of each cluster
   - Created dashboards and visualizations in Power BI
   - Developed key performance indicators (KPIs):
     - Customer distribution across clusters
     - Spending behavior across different income levels
     - Gender distribution per cluster
     - High-value customer identification
     - Income vs. Spending Score analysis
4. **Power BI Dashboard Development**
   - Designed interactive visualizations for cluster insights
   - Created filters for dynamic customer segmentation analysis
   - Published dashboard for business use

### **Phase 2: Market Basket Analysis**
1. **Data Cleaning & Preprocessing**
   - Handled missing and duplicate values
   - Transformed transactional data for frequent pattern mining
2. **Frequent Pattern Mining using FP-Growth**
   - Extracted frequent itemsets using the FP-Growth algorithm
   - Generated association rules with metrics such as support, confidence, and lift
3. **Business Insights & Visualization**
   - Visualized product associations using network graphs and heatmaps
   - Provided data-driven recommendations for product bundling and promotions


## 📌 Key Insights & Business Recommendations
- **Customer Segmentation:** Identified five distinct customer segments with unique spending and income characteristics, enabling more effective marketing strategies.
- **Market Basket Analysis:** Discovered strong item associations that help in upselling and cross-selling strategies.
- **Actionable Recommendations:**
  - Design targeted promotions for high-spending customers.
  - Optimize store layouts and online recommendations based on purchase patterns.
  - Implement personalized discount strategies to increase customer retention.
  - Enhance loyalty programs using customer segmentation insights.
  - Improve product placement based on association rule mining results.
  - Utilize Power BI dashboards for data-driven decision-making and dynamic customer insights.

## 📁 Repository Structure
```
📂 Customer_Segmentation_Market_Basket_Analysis
│── 📂 dashboard
│   ├── Customer_Segmentation.pbix
│   
│── 📂 data
│   ├── Mall_Customers_Clustered.csv
│   ├── Mall_Customers_processed.csv
│   ├── Mall_Customers.csv
│   ├── Market_Basket_Cleaned.csv
│   ├── Market_Basket_Processed.csv
│   ├── Market_Basket_Rules.csv
│   ├── Market_Basket.csv
│   
│── 📂 notebooks
│   ├── Customer_Segmentation
│   │   ├── 01_data_exploration.ipynb
│   │   ├── 02_data_preprocessing.ipynb
│   │   ├── 03_optimal_clusters.ipynb
│   │   ├── 04_kmeans_clustering.ipynb
│   │
│   ├── Market_Basket_Analysis
│   │   ├── 01_data_exploration.ipynb
│   │   ├── 02_data_preprocessing.ipynb
│   │   ├── 03_data_exploration(Cleaned_Data).ipynb
│   │   ├── 04_data_preprocessing(Cleaned_Data).ipynb
│   │   ├── 05_market_basket_analysis.ipynb
│   ├───├── 06_visualizing_rules.ipynb
│   
│── 📂 reports
│   ├── Market_Basket_Analysis_Report.md
│   ├── Customer_Segmentation_Report.md
│
│── 📂 visuals
│   ├── Association Rules Graph.png
│   ├── Customer Segmentation Dashboard.png
│   ├── Customer Insights (Customer Segmentation).png
│
│── README.md
│── requirements.txt
```

## 🛠️ How to Run the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Customer_Segmentation_Market_Basket_Analysis.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Customer_Segmentation_Market_Basket_Analysis
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Open Jupyter Notebook and execute the relevant notebooks.
5. Open Power BI and load `Customer_Segmentation.pbix`  to explore interactive dashboards.




