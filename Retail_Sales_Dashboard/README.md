# **Retail Sales & Revenue Insights Dashboard**  

## **📌 Project Overview**  
This project analyzes **retail sales performance** using **SQL and Power BI** to extract actionable insights for business decision-making. The goal is to provide a **data-driven strategy** for revenue optimization, product performance analysis, and customer behavior understanding.  

The insights are presented through an **interactive Power BI dashboard**, enabling businesses to monitor key metrics such as **total revenue, sales trends, best-selling products, and customer spending patterns**.  

---

## **📊 Business Questions Answered**  

✅ **What is the total revenue, and how has it changed over time?**  
✅ **Which product categories generate the highest sales?**  
✅ **What are the seasonal trends in sales performance?**  
✅ **Which customer age groups contribute the most revenue?**  
✅ **Which days of the week drive the most sales?**  

These insights help retailers **optimize inventory, improve targeted marketing, and enhance revenue strategies**.  

---

## **🛠️ Tools & Technologies Used**  

- **SQL (MySQL)** → Data extraction, cleaning, and transformation  
- **Power BI** → Data visualization & dashboard creation  
- **VS Code** → Query execution & project setup  
- **Excel (optional)** → Data validation & preprocessing  

---

## **📁 Dataset Overview**  

The dataset consists of **customer transactions from a retail business**, with key attributes:  

| Column Name        | Description                            |
|--------------------|----------------------------------------|
| Transaction ID     | Unique ID for each transaction         |
| Date               | Purchase date                          |
| Customer ID        | Unique customer identifier             |
| Gender             | Customer gender (Male/Female)          |
| Age                | Customer age                           |
| Product Category   | Category of purchased product          |
| Quantity           | Number of units purchased              |
| Price per Unit     | Price of a single unit                 |
| Total Amount       | Revenue generated from the transaction |

---

## **📈 Key Insights & Visualizations**  

### **1️⃣ Total Revenue & Monthly Sales Trends**  
🔹 **Insight:** Revenue patterns reveal seasonal trends, helping businesses prepare for high-demand periods.  

### **2️⃣ Top-Selling Product Categories**  
🔹 **Insight:** Identifies which product categories drive the most sales, guiding inventory planning and promotions.  

### **3️⃣ Revenue Contribution by Age Group**  
🔹 **Insight:** Shows which customer demographics contribute the most revenue, helping in personalized marketing.  

### **4️⃣ Sales Performance by Weekday (Newly Added Visual)**  
🔹 **Insight:** Analyzes sales trends across different weekdays to optimize staffing and marketing strategies.  

---

## **🛠 Project Workflow**  

1️⃣ **Data Cleaning & Preprocessing (SQL in MySQL & VS Code)**  
   - Removed duplicates and handled missing values  
   - Standardized product categories for consistency  
   - Calculated total revenue using:  
     ```sql
     SELECT Product_Category, SUM(Total_Amount) AS Total_Revenue  
     FROM sales_data  
     GROUP BY Product_Category;  
     ```
   - Extracted additional columns for analysis, such as weekdays and monthly sales trends  

2️⃣ **Data Visualization (Power BI)**  
   - Connected MySQL to Power BI for real-time insights  
   - Designed interactive dashboards with filters for **date range, product category, and customer segment**  
   - Implemented **KPI cards, bar charts, and trend lines** to highlight key metrics  

---

## **🛠 Folder Structure**  

```
Retail_Sales_Insights/
│── data/  
│   ├── sales_data.csv  
│── sql_queries/  
│   ├── data_cleaning.sql  
│   ├── sales_analysis.sql  
│── powerbi_dashboard/  
│   ├── Retail_Sales_Dashboard.pbix  
│── README.md  
│── requirements.txt  (optional)
```

---

## **💡 How to Use This Repository?**  

1️⃣ **Clone the repository**  
```bash
git clone 
```  
2️⃣ **Run SQL queries in MySQL** (`sql/data_cleaning.sql` & `sql/sales_analysis.sql`)  
3️⃣ **Open `Retail_Sales_Dashboard.pbix` in Power BI**  
4️⃣ **Analyze the insights and explore filters**  

---

## **🎯 Business Impact**  

🚀 **Inventory Optimization:** Helps businesses stock the right products based on demand.  
📊 **Marketing Strategy:** Targets high-value customers based on spending habits.  
📅 **Sales Planning:** Identifies peak sales days to adjust staffing and promotions.  

---



