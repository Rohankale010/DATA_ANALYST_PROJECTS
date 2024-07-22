-- Step 1: Create Database and Use it
CREATE DATABASE IF NOT EXISTS pizza_project;
USE pizza_project;

-- Step 2: Create pizza_types Table
CREATE TABLE pizza_types(
    pizza_type_id VARCHAR(150) PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    category VARCHAR(10) NOT NULL,
    ingredients VARCHAR(150) NOT NULL
);

-- Step 3: Create pizzas Table
CREATE TABLE pizzas(
    pizza_id VARCHAR(20) PRIMARY KEY NOT NULL,
    pizza_type_id VARCHAR(150) NOT NULL,
    size VARCHAR(4) NOT NULL,
    price DECIMAL(7,2) NOT NULL,
    FOREIGN KEY (pizza_type_id) REFERENCES pizza_types(pizza_type_id)
);

-- Step 4: Create orders Table
CREATE TABLE orders (
    order_id INT PRIMARY KEY NOT NULL,
    date DATE,
    time TIME
);

-- Step 5: Create order_details Table
CREATE TABLE order_details(
    order_details_id INT NOT NULL,
    order_id INT NOT NULL,
    pizza_id VARCHAR(20) NOT NULL,
    quantity INT NOT NULL,
    PRIMARY KEY (order_details_id),
    FOREIGN KEY (pizza_id) REFERENCES pizzas(pizza_id),
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);