-- Basic:
--       Retrieve the total number of orders placed.
SELECT distinct(COUNT(order_id)) FROM orders;

-- Calculate the total revenue generated from pizza sales.
select cast(sum(order_details.quantity * pizzas.price) as decimal(10,2)) as 'Total Revenue'
from order_details 
join pizzas on pizzas.pizza_id = order_details.pizza_id;

-- Identify the highest-priced pizza.
with cte as
    (SELECT pizzas.price AS Price, pizza_types.name AS Pizza_Name,
           RANK() OVER (ORDER BY pizzas.price DESC) AS ranks
    FROM pizzas
    JOIN pizza_types ON pizzas.pizza_type_id = pizza_types.pizza_type_id
) 
SELECT Pizza_Name,Price from cte where ranks=1;

-- Identify the most common pizza size ordered.
select pizzas.size, count(distinct order_id) as 'No of Orders', sum(quantity) as 'Total Quantity Ordered' 
from order_details
join pizzas on pizzas.pizza_id = order_details.pizza_id
-- join pizza_types on pizza_types.pizza_type_id = pizzas.pizza_type_id
group by pizzas.size
order by count(distinct order_id) desc;

-- List the top 5 most ordered pizza types along with their quantities.
 select pizza_types.name as Pizza_name,sum(order_details.quantity) as Total_ordered 
 from order_details
 join pizzas on pizzas.pizza_id=order_details.pizza_id
 join pizza_types on pizza_types.pizza_type_id=pizzas.pizza_type_id 
 group by Pizza_name
 order by Total_ordered desc
 limit 5;

-- Intermediate:
-- Find the total quantity of each pizza category ordered (this will help us to understand the category which customers prefer the most).
 select pizza_types.category,sum(order_details.quantity) as Total_quantity 
 from order_details
 join pizzas on pizzas.pizza_id=order_details.pizza_id
 join pizza_types on pizza_types.pizza_type_id=pizzas.pizza_type_id
 group by pizza_types.category
 order by Total_quantity desc;
 
-- Determine the distribution of orders by hour of the day (at which time the orders are maximum (for inventory management and resource allocation).
select hour(time) as Hour_of_day,count(distinct(order_id)) as Total_ordered
from orders 
group by Hour_of_day
order by Total_ordered desc;

-- Find the category-wise distribution of pizzas (to understand customer behaviour).
select category,count(distinct(pizza_type_id)) as No_of_Pizza
from pizza_types 
group by category;

-- Group the orders by date and calculate the average number of pizzas ordered per day.
with cte as (
select orders.date as order_date,sum(order_details.quantity) as Total_orders 
from order_details
join orders on orders.order_id=order_details.order_id
group by order_date)

select avg(Total_orders) as Average_Pizza_orders_per_day from cte;

-- Determine the top 3 most ordered pizza types based on revenue (let's see the revenue wise pizza orders to understand from sales perspective which pizza is the best selling)
select pizza_types.name as Pizza_type,sum(pizzas.price*order_details.quantity) as Price 
from order_details
join pizzas on pizzas.pizza_id=order_details.pizza_id 
join pizza_types on pizza_types.pizza_type_id=pizzas.pizza_type_id
group by Pizza_type 
order by Price Desc 
limit 3;

-- Advanced:
-- Calculate the percentage contribution of each pizza type to total revenue (to understand % of contribution of each pizza in the total revenue)

-- Analyze the cumulative revenue generated over time.
WITH cte as (
SELECT orders.`date` as dates, orders.`time`as times,SUM(order_details.quantity*pizzas.price) as revenue 
FROM orders 
JOIN order_details on orders.order_id= order_details.order_id
JOIN pizzas on order_details.pizza_id=pizzas.pizza_id
GROUP BY orders.`date`, orders.`time`
order by orders.`date`, orders.`time`),
cumulative_revenue as ( 
SELECT dates,
times,
SUM(revenue) OVER(ORDER BY dates,times ) as revenue
from cte)
SELECT dates,hour(times),revenue as times FROM cumulative_revenue;
-- Determine the top 3 most ordered pizza types based on revenue for each pizza category (In each category which pizza is the most selling)