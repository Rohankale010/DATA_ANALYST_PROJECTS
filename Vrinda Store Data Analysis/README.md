# Vrinda Store Data Analysis

## Table of Contents

- [Project Overview](#project-overview)
- [Project Structure](#project-structure)
- [Data Source](#data-source)
- [Step Involved](#step-involved)

## Project Overview
This project involves analyzing the sales data of Vrinda Store to derive meaningful insights and visualizations. The analysis includes data cleaning, exploratory data analysis, and the creation of a comprehensive sales dashboard to understand sales performance and identify key trends.

## Project Structure
```plaintext
Vrinda Store Data Analysis 
│
├── data
│   └── Vrinda Store Data.xlsx
│
├── analysis
│   └── pivot_table.md
│
├── dashboard
│   └── Vrinda Store Data-Analysis.xlsx
│
├── requirements.txt
└── README.md

```


## Data Source
The data for this project is sourced from two Excel files:
- `Vrinda Store Data.xlsx` (original data)
- `Vrinda Store Data-Analysis.xlsx` (cleaned and analyzed data)

## Steps Involved

### 1. Data Cleaning
- **Loading Data:** Imported data from the Excel files.
- **Handling Missing Values:** Identified and handled missing values.
- **Data Formatting:** Ensured correct data formats for dates, numerical values, and categories.
- **Duplicates Removal:** Checked for and removed duplicate records.
- **Data Enrichment:** Added relevant columns such as month and age group .

### 2. Exploratory Data Analysis (EDA)
- **Summary Statistics:** Calculated mean, median, mode, and standard deviation for numerical columns.
- **Sales Trends:** Analyzed monthly and yearly sales trends.
- **State-wise Analysis:** Examined sales performance by state.
- **Top Channel:** Identified the highest sales achieving channel.
- **Customer Insights:** Analyzed sales distribution by gender and age group.
- **Order Status:** Assessed the distribution of order statuses (delivered, refunded, canceled).

### 3. Data Visualization and Dashboard Creation
The following visualizations were created to build a comprehensive sales dashboard:

- **Orders vs Sales (Line and Bar Chart):** Displays the monthly sales trends and the number of orders.
  - **Insight:** There is a noticeable decline in sales and orders from January to December, with a slight increase in May and September.

- **Gender-Based Sales Insights (Pie Chart):** Shows the distribution of sales between men and women.
  - **Insight:** Women make up 64% of the sales, while men contribute 36%.

- **Order Status (Pie Chart):** Visualizes the breakdown of order statuses.
  - **Insight:** The majority of orders (92%) are delivered, with a small percentage being refunded (2%) or canceled (3%).

- **Top 5 States by Sales (Bar Chart):** Highlights the top-performing states by sales volume.
  - **Insight:** Maharashtra leads with 2.65M in sales, followed by Gujarat (2.39M), Uttar Pradesh (2.10M), Telangana (1.71M), and Tamil Nadu (1.68M).

- **Age and Gender Order Statistics (Bar Chart):** Provides insights into the distribution of sales by age groups and gender.
  - **Insight:** Adults (34.99%) are the largest customer group, followed by teenagers (21.13%), seniors (13.70%), and young adults (15.47%).

- **Channel-Wise Order Sales (Donut Chart):** Displays the percentage of sales from different sales channels.
  - **Insight:** Amazon is the leading sales channel (35.48%), followed by Myntra (23.88%), Flipkart (21.82%), and others.

### 4. Insights and Conclusions
- **Seasonal Trends:** Sales and orders peak in January and gradually decline towards December, with slight peaks in May and September.
- **Customer Demographics:** Women are the primary customers, and adults make up the largest age group.
- **Order Channels:** Amazon is the most significant sales channel, indicating a strong online presence.
- **Geographical Performance:** Maharashtra, Gujarat, and Uttar Pradesh are the top-performing states, suggesting focused marketing strategies in these regions.



