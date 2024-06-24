# Import Necessary Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from kneed import KneeLocator
import warnings

warnings.filterwarnings('ignore')

# Load the Dataset
df = pd.read_csv('D:\Projects\DATA_ANALYST_PROJECTS\Customer Segmentation Analysis\data\Mall_Customers.csv')

# Dropping unnecessary column (CustomerID)
df = df.drop('CustomerID', axis=1)

# Data Preprocessing
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df[['Age', 'Annual Income (k$)', 'Spending Score (1-100)']])
df_scaled = pd.DataFrame(df_scaled, columns=['Age', 'Annual Income (k$)', 'Spending Score (1-100)'])

# Clustering based on Age and Spending Score
X1 = df_scaled.loc[:, ['Age', 'Spending Score (1-100)']].values

kmeans_age_score = KMeans(n_clusters=4, init='k-means++', random_state=42)
cluster_age_score = kmeans_age_score.fit_predict(X1)

plt.figure(figsize=(8, 5))
plt.scatter(X1[:, 0], X1[:, 1], c=kmeans_age_score.labels_, cmap='viridis')
plt.scatter(kmeans_age_score.cluster_centers_[:, 0], kmeans_age_score.cluster_centers_[:, 1], color='black')
plt.title('Cluster of Customers based on Age and Spending Score')
plt.xlabel('Age')
plt.ylabel('Spending Score')
plt.savefig('D:\Projects\DATA_ANALYST_PROJECTS\Customer Segmentation Analysis/visualizations/cluster_age_spending.png')
plt.show()

# Clustering based on Annual Income and Spending Score
X2 = df_scaled.loc[:, ['Annual Income (k$)', 'Spending Score (1-100)']].values

kmeans_income_score = KMeans(n_clusters=5, init='k-means++', random_state=42)
cluster_income_score = kmeans_income_score.fit_predict(X2)

plt.figure(figsize=(8, 5))
plt.scatter(X2[:, 0], X2[:, 1], c=kmeans_income_score.labels_, cmap='plasma')
plt.scatter(kmeans_income_score.cluster_centers_[:, 0], kmeans_income_score.cluster_centers_[:, 1], color='black')
plt.title('Cluster of Customers based on Annual Income and Spending Score')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score')
plt.savefig('D:\Projects\DATA_ANALYST_PROJECTS\Customer Segmentation Analysis/visualizations/cluster_income_spending.png')
plt.show()

# Clustering based on all three features: Age, Annual Income, and Spending Score
X3 = df_scaled.iloc[:, :].values

wcss = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, init='k-means++', random_state=42)
    kmeans.fit(X3)
    wcss.append(kmeans.inertia_)

plt.figure(figsize=(8, 5))
plt.plot(range(1, 11), wcss, marker='8', color='red')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('Within-cluster Sum of Squares (WCSS)')
plt.title('Elbow Method for Optimal K')
plt.savefig('D:\Projects\DATA_ANALYST_PROJECTS\Customer Segmentation Analysis/visualizations/elbow_method.png')
plt.show()

# Using KneeLocator to find the best K value
kl = KneeLocator(range(1, 11), wcss, curve='convex', direction='decreasing')
optimal_k = kl.elbow

kmeans_final = KMeans(n_clusters=optimal_k, init='k-means++', random_state=42)
cluster_final = kmeans_final.fit_predict(X3)

df['Cluster'] = cluster_final

# Save clustered data to CSV (optional)
df.to_csv('D:\Projects\DATA_ANALYST_PROJECTS\Customer Segmentation Analysis\data\mall_customers_clustered.csv', index=False)

# Cluster Analysis
cluster_analysis = df.groupby('Cluster').mean()

# Plotting average characteristics of each cluster
plt.figure(figsize=(10, 6))
sns.barplot(data=cluster_analysis, x=cluster_analysis.index, y='Age', palette='viridis')
plt.title('Average Age by Cluster')
plt.xlabel('Cluster')
plt.ylabel('Average Age')
plt.savefig('D:\Projects\DATA_ANALYST_PROJECTS\Customer Segmentation Analysis/visualizations/average_age_by_cluster.png')
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(data=cluster_analysis, x=cluster_analysis.index, y='Annual Income (k$)', palette='viridis')
plt.title('Average Annual Income by Cluster')
plt.xlabel('Cluster')
plt.ylabel('Average Annual Income (k$)')
plt.savefig('D:\Projects\DATA_ANALYST_PROJECTS\Customer Segmentation Analysis/visualizations/average_income_by_cluster.png')
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(data=cluster_analysis, x=cluster_analysis.index, y='Spending Score (1-100)', palette='mako')
plt.title('Average Spending Score by Cluster')
plt.xlabel('Cluster')
plt.ylabel('Average Spending Score')
plt.savefig('D:\Projects\DATA_ANALYST_PROJECTS\Customer Segmentation Analysis/visualizations/average_spending_score_by_cluster.png')
plt.show()

# Print insights and recommendations
print("\nInsights and Recommendations:")
for i, row in cluster_analysis.iterrows():
    print(f'\nCluster {i}:')
    print(f"Average Age: {row['Age']:.2f}")
    print(f"Average Annual Income (k$): {row['Annual Income (k$)']:.2f}")
    print(f"Average Spending Score: {row['Spending Score (1-100)']:.2f}")

print("\nConclusion:")
print("These segments can be used to tailor different marketing strategies and product offers to meet the needs of customer groups.")
