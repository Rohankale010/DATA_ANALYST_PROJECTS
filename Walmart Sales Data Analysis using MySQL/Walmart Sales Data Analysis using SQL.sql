create database if not exists walmartsales;
Use walmartsales;

CREATE TABLE sales(
invoice_id VARCHAR(20) NOT NULL PRIMARY KEY,
branch VARCHAR(10) NOT NULL,
city VARCHAR(20) NOT NULL,
customer_type VARCHAR(30) NOT NULL,
gender VARCHAR(10) NOT NULL,
product_line VARCHAR(100) NOT NULL,
unit_price DECIMAL(10,2) NOT NULL,
quantity INT NOT NULL,
VAT FLOAT(6,4) NOT NULL,
total DECIMAL(10,2) NOT NULL,
date DATETIME NOT NULL,
time TIME NOT NULL,
payment_method VARCHAR(15) NOT NULL,
cogs DECIMAL(10,2),
gross_margin_percentage FLOAT(11,9),
gross_income DECIMAL(12,4),
rating FLOAT(2,1)
);


SELECT * FROM sales;

-- ------------------------------------------------------    FEATURE ENGINEERING    ------------------------------------------------------------------------------------------


SELECT 
time ,(CASE
      WHEN 'time' BETWEEN "00:00:00" AND "12:00:00" THEN "Morning"
      WHEN 'time' BETWEEN "12:00:01" AND "16:00:00" THEN "Afternoon"
      ELSE "Evening"
      END
      ) AS time_of_date
from sales;

ALTER TABLE sales ADD COLUMN time_of_day VARCHAR(20) ;

UPDATE sales 
SET time_of_day=(CASE
      WHEN `time` BETWEEN "00:00:00" AND "12:00:00" THEN "Morning"
      WHEN `time` BETWEEN "12:01:00" AND "16:00:00" THEN "Afternoon"
      ELSE "Evening"
      END
);


SELECT 
      date,
	  DAYNAME(date) as day 
FROM sales;

ALTER TABLE sales ADD COLUMN day VARCHAR(10);

UPDATE sales 
SET day=(DAYNAME(date));

SELECT date ,
	   MONTHNAME(date) AS month
       FROM sales;
       
ALTER TABLE sales ADD COLUMN month VARCHAR(10);

UPDATE sales
SET month = (MONTHNAME(date));


-- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-- ----------------------------------------------------------      Business Questions To Answer     --------------------------------------------------------------------------
-- Generic Question

-- How many unique cities does the data have?
SELECT COUNT(DISTINCT city) FROM sales;

-- In which city is each branch?
SELECT DISTINCT city,branch FROM sales;

-- ==========================================================             Product            =================================================================================
-- How many unique product lines does the data have?
SELECT COUNT(DISTINCT product_line) FROM sales;

-- What is the most common payment method?
SELECT payment_method,
       COUNT(payment_method) AS counts FROM sales 
       GROUP BY payment_method 
       ORDER BY counts DESC;
       
-- What is the most selling product line?
SELECT product_line,
       COUNT(quantity) AS counts FROM sales 
       GROUP BY product_line 
       ORDER BY counts DESC;
       
-- What is the total revenue by month?
SELECT month,
       SUM(total) AS total_revenue FROM sales 
       GROUP BY month
       ORDER BY total_revenue DESC;
       
-- What month had the largest COGS?
SELECT month,
	   SUM(cogs) AS largest_cogs FROM sales
       GROUP BY month
       ORDER BY largest_cogs DESC;
       
-- What product line had the largest revenue?
SELECT product_line,
       SUM(total) AS revenue FROM sales 
       GROUP BY product_line 
       ORDER BY revenue DESC ;
       
-- What is the city with the largest revenue?
SELECT city,
       SUM(total) AS revenue FROM sales 
       GROUP BY city 
       ORDER BY revenue DESC ;
       
-- What product line had the largest VAT?
SELECT product_line,
       SUM(VAT) AS VAT FROM sales
       GROUP BY product_line
       ORDER BY VAT DESC;
       
-- Fetch each product line and add a column to those product line showing "Good", "Bad". Good if its greater than average sales
SELECT product_line,AVG(total) AS avg_sales,SUM(total) AS total_sales FROM sales, 
IF avg_sales<total_sales THEN "Good" 
    ELSE "Bad" 
    END AS performance 
    GROUP BY product_line;

-- Which branch sold more products than average product sold?
SELECT branch,
       SUM(quantity) AS qty FROM sales
       GROUP BY branch 
       HAVING qty>(SELECT AVG(quantity) FROM sales);
       
-- What is the most common product line by gender?
SELECT gender,
       product_line,
       COUNT(gender) as counts FROM sales
       GROUP BY gender,product_line 
       ORDER BY counts DESC;
       
-- What is the average rating of each product line?
SELECT product_line,
       ROUND(AVG(rating), 2) as avg_ratings FROM sales
       GROUP BY product_line
       ORDER BY avg_ratings DESC;

-- ======================================================             Sales           ======================================================================================
-- Number of sales made in each time of the day per weekday
SELECT time_of_day,
       COUNT(*) AS total_sales FROM sales
       GROUP BY time_of_day;
       
-- Which of the customer types brings the most revenue?
SELECT customer_type,
       SUM(total) AS total_revenue FROM sales
       GROUP BY customer_type 
       ORDER BY total_revenue DESC ;
       
-- Which city has the largest tax percent/ VAT (Value Added Tax)?
SELECT city,
	ROUND(AVG(VAT), 2) AS tax_percent FROM sales
    GROUP BY city 
    ORDER BY tax_percent DESC;
    
-- Which customer type pays the most in VAT?
SELECT customer_type,
       ROUND(AVG(VAT),2) AS total_VAT FROM sales
       GROUP BY customer_type
       ORDER BY total_VAT DESC;

-- ===========================================================       Customer        ======================================================================================
-- How many unique customer types does the data have?
SELECT COUNT(DISTINCT(customer_type)) FROM sales;

-- How many unique payment methods does the data have?
SELECT COUNT(DISTINCT(payment_method)) FROM sales;

-- What is the most common customer type?
SELECT customer_type,COUNT(customer_type) AS counts FROM sales
       GROUP BY customer_type 
       ORDER BY counts DESC;
       
-- Which customer type buys the most?
SELECT customer_type,SUM(total) AS total FROM sales
       GROUP BY customer_type 
       ORDER BY total DESC;
       
-- What is the gender of most of the customers?
SELECT gender,COUNT(gender) AS counts FROM sales 
	GROUP BY gender
    ORDER BY counts DESC;
    
-- What is the gender distribution per branch?
SELECT branch,gender,COUNT(gender) AS counts FROM sales 
       GROUP BY branch,gender
       ORDER BY branch;
       
-- Which time of the day do customers give most ratings?
SELECT time_of_day,COUNT(rating) AS most_ratings FROM sales
      GROUP BY time_of_day
      ORDER BY most_ratings DESC;
      
-- Which time of the day do customers give most ratings per branch?
SELECT time_of_day,branch,COUNT(rating) AS most_ratings FROM sales
      GROUP BY time_of_day,branch
      ORDER BY most_ratings DESC;
      
-- Which day of the week has the best avg ratings?
SELECT day,
        ROUND(AVG(rating),2) AS avg_rating FROM sales
       GROUP BY day
       ORDER BY avg_rating DESC;

-- Which day of the week has the best average ratings per branch?
SELECT day,branch,
	   ROUND(AVG(rating),2) AS avg_rating FROM sales
       GROUP BY day,branch
       ORDER BY branch,avg_rating DESC;