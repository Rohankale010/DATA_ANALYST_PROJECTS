CREATE DATABASE IF NOT EXISTS walmartsales;
USE walmartsales;

CREATE TABLE sales (
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
