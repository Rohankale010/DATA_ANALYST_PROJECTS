# Ecommerce (Flipkart) Data Analysis

This project involves analyzing ecommerce data from Flipkart to gain insights into product categories, brands, and discount patterns.

## Project Overview

The project performs the following steps:

1. **Data Loading and Exploration**:
   - Loads the dataset (`flipkart_com-ecommerce_sample.csv`) from [Kaggle](https://www.kaggle.com/datasets/PromptCloudHQ/flipkart-products).
   - Displays the first few rows and information about the dataset.
   - Checks and handles missing values.

2. **Feature Engineering**:
   - Creates new features such as `Discount_percentage`, `Date`, and `Time`.
   - Extracts the main category from the product category tree.

3. **Data Visualization**:
   - Visualizes top products and brands using pie charts.
   - Analyzes discount patterns and ratings distribution.

4. **Advanced Analysis**:
   - Creates funnel plots for product ratings.
   - Analyzes the relationship between retail prices and discounted prices over time.
   - Visualizes the number of clicks over time.

## Data Visualization

The project includes the following visualizations:

1. **Top Products and Brands Distribution**:
   - Pie charts to display the distribution of top products and brands (`top_products_brands_distribution.png`).

2. **Discount Percentage Distribution**:
   - Bar chart to show the brands with the highest average discount percentage (`brands_highest_discount.png`).

3. **Ratings Funnel**:
   - Funnel plot to illustrate the distribution of total products, products with ratings, and products with 5-star ratings (`ratings_funnel.png`).

4. **Ratings vs Count**:
   - Scatter plot to show the relationship between product ratings and the count of each rating (`ratings_vs_count.png`).

5. **Retail and Discounted Prices Over Time**:
   - Area chart to visualize the changes in retail and discounted prices over time (`price_over_time.png`).

6. **Clicks Over Time**:
   - Scatter plot to show the number of clicks over time (`clicks_vs_time.png`).

## Requirements

Ensure you have the following Python libraries installed:
- pandas
- numpy
- matplotlib
- seaborn
- plotly
- scikit-learn
- kaleido

You can install the required libraries using the following command:

```bash
pip install -r requirements.txt
```


## Usage

1. Clone the repository and navigate into the `ecommerce_flipkart_data_analysis` directory.
2. Ensure you have Python and the required libraries installed.
3. Download the dataset and place it in the `data` directory.
4. Run the script to perform data analysis.

```bash
python scripts/E-commerce_data_analysis.py
