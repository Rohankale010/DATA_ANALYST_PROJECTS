# Customer Segmentation Analysis

This project involves analyzing customer data from a mall to segment customers based on their annual income and spending score. Customer segmentation helps in identifying different groups of customers with similar behaviors, which can be used for targeted marketing strategies and personalized customer services.

## Project Overview

The project performs the following steps:

1. **Data Loading and Exploration**: 
   - Loads the dataset (`Mall_Customers.csv`) containing customer information from [Kaggle](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python).
   - Displays the first few rows of the dataset to understand its structure.
   - Prints the dimensions (number of rows and columns) of the dataset.
   - Summarizes statistics (mean, min, max, etc.) for numerical columns like Age, Annual Income, and Spending Score.
   - Checks for any missing values in the dataset and handles them if necessary.

2. **Data Visualization**:
   - Visualizes the distribution of customer age, annual income, and spending score using histograms and bar plots.
   - Provides insights into the distribution patterns among different age groups, income levels, and spending scores.

3. **Data Preprocessing**:
   - Standardizes numerical features (Age, Annual Income, Spending Score) using `StandardScaler` to bring them to the same scale.

4. **Customer Segmentation using K-means Clustering**:
   - Applies K-means clustering algorithm to segment customers based on their Annual Income and Spending Score.
   - Determines the optimal number of clusters using the Elbow method and the `KneeLocator` package.
   - Visualizes the clustering results using scatter plots to identify distinct customer segments.

5. **Cluster Analysis**:
   - Analyzes the characteristics of each customer segment (average age, annual income, spending score).
   - Provides insights and recommendations based on cluster analysis for marketing strategies and customer engagement.

## Requirements

Ensure you have the following Python libraries installed:
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- kneed

You can install the required libraries using the following command:
 ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Clone the repository and navigate into the project directory.
2. Ensure you have Python and required libraries installed.
3. Download `Mall_Customers.csv` file using Git LFS (`git lfs pull`) or access it from the [Kaggle dataset](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python).
4. Run the script `customer_segmentation_analysis.py` to execute the customer segmentation analysis.

```bash
python "Customer Segmentation Analysis/scripts/customer_segmentation_analysis.py"
