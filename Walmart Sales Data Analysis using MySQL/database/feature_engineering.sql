-- Add time_of_day column
ALTER TABLE sales ADD COLUMN time_of_day VARCHAR(20);
UPDATE sales 
SET time_of_day=(CASE
      WHEN `time` BETWEEN "00:00:00" AND "12:00:00" THEN "Morning"
      WHEN `time` BETWEEN "12:01:00" AND "16:00:00" THEN "Afternoon"
      ELSE "Evening"
      END);

-- Add day column
ALTER TABLE sales ADD COLUMN day VARCHAR(10);
UPDATE sales 
SET day=(DAYNAME(date));

-- Add month column
ALTER TABLE sales ADD COLUMN month VARCHAR(10);
UPDATE sales
SET month = (MONTHNAME(date));
