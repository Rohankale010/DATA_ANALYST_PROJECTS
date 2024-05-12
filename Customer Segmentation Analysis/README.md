<<<<<<< HEAD
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
```
5. View the generated visualizations and insights in your Python environment.

## Data Source

The dataset Mall_Customers.csv used in this project can be downloaded from [Kaggle Customer Segmentation Tutorial](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python).

## License
This project is licensed under the `MIT License`.

=======
**Documentation for Mall-Customer Dataset**

**1. Introduction:**
The Mall-Customer dataset provides information about customers' demographics and spending behavior. It consists of data collected from customers of a mall, including features such as CustomerID, Gender, Age, Annual Income (in thousands of dollars), and Spending Score (ranging from 1 to 100).

**2. Data Description:**
- **CustomerID:** Unique identifier for each customer.
- **Gender:** Gender of the customer (Male or Female).
- **Age:** Age of the customer.
- **Annual Income (k$):** Annual income of the customer in thousands of dollars.
- **Spending Score (1-100):** Spending score assigned to the customer based on their spending behavior and purchasing data.

**3. Data Source:**
The dataset was collected from customers visiting a mall, where their demographic information and spending habits were recorded for market analysis and customer segmentation purposes.

**4. Data Collection Process:**
The data collection process likely involved customer surveys, loyalty programs, or transaction records maintained by the mall. Customers may have voluntarily provided demographic information during registration or at the point of sale.

**5. Data Quality:**
The dataset appears to be relatively clean, with no missing values or obvious errors. However, further data validation and cleansing may be necessary depending on the specific analysis requirements.

**6. Conclusion:**
The Mall-Customer dataset provides valuable insights into customer demographics and spending behavior, offering opportunities for market analysis, segmentation, and personalized marketing strategies. However, it's essential to handle the data ethically and ensure its quality and integrity throughout the analysis process.
>>>>>>> 0b963da (Project)
