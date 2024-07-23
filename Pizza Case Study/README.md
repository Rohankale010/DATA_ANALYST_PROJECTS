# Pizza Sales Analysis

## Table of Contents
- [Project Overview](#project-overview)
- [Project Structure](#project-structure)
- [Database Schema](#database-schema)
- [Objectives](#objectives)
- [Tools Used](#tools-used)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Conclusion](#conclusion)

## Project Overview
This project involves analyzing pizza sales data to derive insights related to order volumes, revenue, popular pizza types and sizes, order distribution by time, and more. The analysis uses SQL queries to perform the data analysis.

## Project Structure
```plaintext
Pizza Sales Analysis/
├── data/
│    ├── order_details.csv
│    ├── orders.csv
│    ├── pizza_types.csv
│    └── pizzas.csv
├── database/
│    ├── create_database_and_tables.sql
│    ├── exploratory_data_analysis.sql
│    └── analysis_queries.sql
├── README.md
└── requirements.txt
```

## Database Schema
1. **Database Name:** `pizza_project`
2. **Tables:**
   - `pizza_types`: Contains information about different types of pizzas.
   - `pizzas`: Contains information about individual pizzas including their types, sizes, and prices.
   - `orders`: Contains information about customer orders.
   - `order_details`: Contains details about each order, including the pizzas ordered and their quantities.

## Objectives
- To analyze the pizza sales data and provide insights into various aspects such as total orders, revenue, popular pizza types, and order distribution.
- To perform exploratory data analysis to extract meaningful information from the data.

## Tools Used
- **MySQL:** Used for database management and executing SQL queries.

## Exploratory Data Analysis
1. **Retrieve the total number of orders placed:**
  
2. **Calculate the total revenue generated from pizza sales:**

3. **Identify the highest-priced pizza:**

4. **Identify the most common pizza size ordered:**

5. **List the top 5 most ordered pizza types along with their quantities:**

6. **Find the total quantity of each pizza category ordered:**

7. **Determine the distribution of orders by hour of the day:**

8. **Find the category-wise distribution of pizzas:**

9. **Group the orders by date and calculate the average number of pizzas ordered per day:**

10. **Determine the top 3 most ordered pizza types based on revenue:**

11. **Calculate the percentage contribution of each pizza type to total revenue:**

12. **Analyze the cumulative revenue generated over time:**

13. **Determine the top 3 most ordered pizza types based on revenue for each pizza category:**

## Conclusion
This project provided a comprehensive analysis of pizza sales data, offering valuable insights into customer preferences, revenue generation, and order patterns. By leveraging SQL queries, we were able to extract meaningful information that can help in making informed business decisions for optimizing operations and enhancing customer satisfaction.
