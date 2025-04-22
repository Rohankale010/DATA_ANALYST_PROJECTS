-- CREATE DATABASE (Only needed once)
CREATE DATABASE RetailSales;
USE RetailSales;

-- CREATE TABLE
CREATE TABLE sales_data(
    Transaction_ID INT PRIMARY KEY,
    Date DATE,
    Customer_ID VARCHAR(20),
    Gender VARCHAR(10),
    Age INT,
    Product_Category VARCHAR(50),
    Quantity INT,
    Price_per_Unit DECIMAL(10,2),
    Total_Amount DECIMAL(10,2)
);

-- CHECK TABLE DATA
SELECT * FROM sales_data;

-- CHECKING FOR MISSING AND NULL VALUES
SELECT 'Transaction_ID' AS Column_name ,COUNT(*) FROM sales_data WHERE Transaction_ID IS NULL
UNION ALL 
SELECT 'Date',COUNT(*) FROM sales_data WHERE Date IS NULL
UNION ALL
SELECT 'Customer_ID' ,COUNT(*) FROM sales_data WHERE Customer_ID IS NULL
UNION ALL
SELECT 'Gender',COUNT(*) FROM sales_data WHERE Gender IS NULL
UNION ALL
SELECT 'Age' ,COUNT(*) FROM sales_data WHERE Age IS NULL
UNION ALL
SELECT 'Product_Category' ,COUNT(*) FROM sales_data WHERE Product_Category IS NULL
UNION ALL
SELECT 'Quantity' ,COUNT(*) FROM sales_data WHERE Quantity IS NULL
UNION ALL
SELECT 'Price_per_unit' ,COUNT(*) FROM sales_data WHERE Price_per_Unit IS NULL
UNION ALL
SELECT 'Total_Amount' ,COUNT(*) FROM sales_data WHERE Total_Amount IS NULL;

-- FINDING DUPLICATE VALUES
SELECT 
    Transaction_ID, Date, Customer_ID, Gender, Age, Product_Category, Quantity, Price_per_Unit, Total_Amount, COUNT(*) 
FROM sales_data
GROUP BY Transaction_ID, Date, Customer_ID, Gender, Age, Product_Category, Quantity, Price_per_Unit, Total_Amount
HAVING COUNT(*) > 1;

-- DELETING DUPLICATE RECORDS
DELETE FROM sales_data
WHERE Transaction_ID NOT IN (
    SELECT Transaction_ID FROM (
        SELECT MIN(Transaction_ID) FROM sales_data 
        GROUP BY Transaction_ID
    ) AS temp_table
);
