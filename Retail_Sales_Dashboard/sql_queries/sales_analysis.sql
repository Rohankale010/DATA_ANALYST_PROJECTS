USE RetailSales;

-- Total Revenue and Total Quantity Sold
SELECT 
    SUM(Total_Amount) AS Total_Revenue,
    SUM(Quantity) AS Total_Quantity_Sold
FROM sales_data;

-- Monthly Sales Trend
SELECT
    DATE_FORMAT(Date, '%Y-%m') AS Month,
    SUM(Total_Amount) AS Total_Revenue
FROM sales_data
GROUP BY Month
ORDER BY Month;

-- Top Best-Selling Product Category
SELECT 
    Product_Category,
    SUM(Total_Amount) AS Total_Sales
FROM sales_data
GROUP BY Product_Category
ORDER BY Total_Sales DESC;

-- Sales by Customer Age Group
SELECT 
    CASE
        WHEN Age BETWEEN 18 AND 25 THEN '18-25'
        WHEN Age BETWEEN 26 AND 35 THEN '26-35'
        WHEN Age BETWEEN 36 AND 45 THEN '36-45'
        WHEN Age BETWEEN 46 AND 60 THEN '46-60'
        ELSE '60+'
    END AS Age_Group,
    SUM(Total_Amount) AS Total_Sales
FROM sales_data
GROUP BY Age_Group
ORDER BY Age_Group;

-- Sales by Gender
SELECT
    Gender,
    SUM(Total_Amount) AS Total_Sales
FROM sales_data
GROUP BY Gender;

-- New vs Repeat Customers
SELECT Customer_Type, COUNT(DISTINCT Customer_ID) AS Customer_Count 
FROM (
    SELECT Customer_ID,
        CASE
            WHEN COUNT(Transaction_ID) > 1 THEN 'Repeat Customer'
            ELSE 'New Customer'
        END AS Customer_Type
    FROM sales_data
    GROUP BY Customer_ID
) AS subquery
GROUP BY Customer_Type;

-- Sales Distribution by Day of the Week
SELECT 
    MONTHNAME(Date) AS Month_Name, 
    DAYNAME(Date) AS Day_Name, 
    SUM(Total_Amount) AS Total_Revenue  
FROM sales_data
GROUP BY Month_Name, Day_Name, MONTH(Date), DAYOFWEEK(Date)
ORDER BY MONTH(Date), DAYOFWEEK(Date);
