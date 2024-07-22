import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.io as pio  # use to save plotly visualizations
from sklearn.impute import SimpleImputer
import warnings
warnings.filterwarnings('ignore')

# Load the dataset
df = pd.read_csv('D:\Projects\DATA_ANALYST_PROJECTS\E-commerce Product\E-commerce_(Flipkart)_data_analysis\data/flipkart_com-ecommerce_sample.csv')

# Displaying the first few rows of dataset
print(df.head())

# Dimension of dataset
print('Dimension :', df.shape)

# Display the Information of Dataset
print('Info:')
print(df.info())

# Checking for Missing value
print('Missing values:')
print(df.isna().sum())

# Filling missing value
imputer = SimpleImputer(strategy='median')
df[['retail_price', 'discounted_price']] = imputer.fit_transform(df[['retail_price', 'discounted_price']])

# Finding out the Discount percentage from retail and discounted price
x = df['retail_price'] - df['discounted_price']
y = (x / df['retail_price']) * 100
df['Discount_percentage'] = round(y, 3)

# Converting dtype of crawl_timestamp then creating separate date and time feature
df['timestamp'] = pd.to_datetime(df['crawl_timestamp'])
df['Time'] = df['timestamp'].apply(lambda x: x.time())
df['Date'] = df['timestamp'].apply(lambda x: x.date())
df.drop('crawl_timestamp', axis=1, inplace=True)

# Filtering out main category through category tree
df['main_category'] = df['product_category_tree'].apply(lambda x: x.split('>>')[0][2:].strip())

top_products = pd.DataFrame(df['main_category'].value_counts()[:10]).reset_index()
top_products.rename(columns={'index': 'Top_Products', 'main_category': 'Total_Count'}, inplace=True)
top_brands = pd.DataFrame(df['brand'].value_counts()[:10]).reset_index()
top_brands.rename(columns={'index': 'Top_Brands', 'brand': 'Total_Count'}, inplace=True)

# Create subplots
fig_both = make_subplots(rows=1, cols=2, specs=[[{'type': 'domain'}, {'type': 'domain'}]])
fig_both.add_trace(go.Pie(labels=top_products['Top_Products'], values=top_products['Total_Count'], name='Top Products', pull=[0.3, 0, 0, 0]), 1, 1)
fig_both.add_trace(go.Pie(labels=top_brands['Top_Brands'], values=top_brands['Total_Count'], name='Top Brands', pull=[0.3, 0, 0, 0]), 1, 2)

# Use hole to create a donut-like pie chart
fig_both.update_traces(hole=0.4, hoverinfo='label+percent+name')
fig_both.update_layout(title_text='Top products and brands distribution',
                       annotations=[dict(text='Product', x=0.18, y=0.5, font_size=20, showarrow=False),
                                    dict(text='Brand', x=0.82, y=0.5, font_size=20, showarrow=False)])

# Save the figure as PNG
#pio.write_image(fig_both,"D:\Projects\DATA_ANALYST_PROJECTS\E-commerce Product\E-commerce_(Flipkart)_data_analysis/visualizations/top_products_brands_distribution.png")

# Additional analysis and visualizations
df['brand'].replace('FashBlush', 'Fash Blush', inplace=True)
df_discount = df.query('Discount_percentage > 90').dropna()
max_discount = pd.DataFrame(round(df_discount.groupby('brand')['Discount_percentage'].mean().sort_values(ascending=False).reset_index(), 3))
fig_bar = px.bar(max_discount, x='brand', y='Discount_percentage', color='brand', title='Brands with Highest Average Discount Percentage')
#pio.write_image(fig_bar,"D:\Projects\DATA_ANALYST_PROJECTS\E-commerce Product\E-commerce_(Flipkart)_data_analysis/visualizations/brands_highest_discount.png")

# Funnel plot
total_prod = len(df['pid'])
total_ratings = len(df[df['product_rating'] != 'No rating available'])
top_ratings = len(df[df['product_rating'] == '5'])
df_funnel_1 = dict(
    number=[total_prod, total_ratings, top_ratings],
    stage=['Total Products', 'Product with Ratings', 'Product with 5 Star Ratings']
)
funnel_1_fig = px.funnel(df_funnel_1, x='number', y='stage')
#pio.write_image(funnel_1_fig,"D:\Projects\DATA_ANALYST_PROJECTS\E-commerce Product\E-commerce_(Flipkart)_data_analysis/visualizations/ratings_funnel.png")

# Ratings vs Count plot
df1 = df[df['product_rating'] != 'No rating available']
ratings = pd.DataFrame(df1['product_rating'].value_counts().reset_index())
ratings['index'] = ratings['index'].astype('float')
ratings.rename(columns={'index': 'Ratings', 'product_rating': 'Counts'}, inplace=True)

fig_dot2 = go.Figure()
fig_dot2.add_trace(go.Scatter(x=ratings['Ratings'], y=ratings['Counts'], mode='markers', name='ratings', marker=dict(color='crimson', size=12)))
fig_dot2.update_layout(title='Ratings vs Count', xaxis_title='Ratings', yaxis_title='Count')
#pio.write_image(fig_dot2,"D:\Projects\DATA_ANALYST_PROJECTS\E-commerce Product\E-commerce_(Flipkart)_data_analysis/visualizations/ratings_vs_count.png")

# Price over Time plot
df_date_retail = pd.DataFrame(df.groupby('Date')['retail_price'].mean().reset_index())
df_date_discount = pd.DataFrame(df.groupby('Date')['discounted_price'].mean().reset_index())
<<<<<<< HEAD
<<<<<<< HEAD
df_date_price = pd.concat([df_date_retail, df_date_discount], axis=1)
df_date_price=df_date_price.loc[:, ~df_date_price.columns.duplicated()]
=======
df_date_price = pd.concat([df_date_retail, df_date_discount], axis=1).loc[:, ~df_date_price.columns.duplicated()]
>>>>>>> 4aa3ec5 (Update Project)
=======
df_date_price = pd.concat([df_date_retail, df_date_discount], axis=1)
df_date_price=df_date_price.loc[:, ~df_date_price.columns.duplicated()]
>>>>>>> 6ef0776 (Added Project)

fig_area2 = go.Figure()
fig_area2.add_trace(go.Scatter(x=df_date_price['Date'], y=df_date_price['retail_price'], fill='tozeroy', name='retail price', line=dict(width=0.5, color='crimson')))
fig_area2.add_trace(go.Scatter(x=df_date_price['Date'], y=df_date_price['discounted_price'], fill='tozeroy', name='discount price', line=dict(width=0.5, color='darkslategray')))
fig_area2.update_layout(xaxis_title='Dates', yaxis_title='Price (in 1000s)', plot_bgcolor='white')
#pio.write_image(fig_area2,"D:\Projects\DATA_ANALYST_PROJECTS\E-commerce Product\E-commerce_(Flipkart)_data_analysis/visualizations/price_over_time.png")

# Clicks vs Time plot
scat2 = px.scatter(x=df['Time'].sort_values(ascending=True), y=df['product_url'])
scat2.update_layout(title_text='No of Clicks vs time', xaxis_title='Time', yaxis_title='No of Clicks')
#pio.write_image(scat2,"D:\Projects\DATA_ANALYST_PROJECTS\E-commerce Product\E-commerce_(Flipkart)_data_analysis/visualizations/clicks_vs_time.png")

# we have save image manually