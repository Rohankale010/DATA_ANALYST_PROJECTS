import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from plotly.subplots import make_subplots
from datetime import datetime
import warnings

warnings.filterwarnings('ignore')

# Load the datasets
covid_df = pd.read_csv('D:\Projects\DATA_ANALYST_PROJECTS\Covid Analysis using Python\data\covid_19_india.csv')
vaccine_df = pd.read_csv('D:\Projects\DATA_ANALYST_PROJECTS\Covid Analysis using Python\data\covid_vaccine_statewise.csv')

# Display the first few rows of dataset
print(covid_df.head())
print(vaccine_df.head())

# Display the information of Dataset
print(covid_df.info())
print(vaccine_df.info())

# Summary Statistics
print(covid_df.describe())
print(vaccine_df.describe())

# Dropping Unnecessary columns
covid_df.drop(labels=['Sno', 'Time', 'ConfirmedIndianNational', 'ConfirmedForeignNational'], inplace=True, axis=1)

# Converting Date column to date type
covid_df['Date'] = pd.to_datetime(covid_df['Date'], format='%Y-%m-%d')

# Finding number of active cases
covid_df['Active_cases'] = covid_df['Confirmed'] - (covid_df['Cured'] + covid_df['Deaths'])

# Creating pivot table
statewise = pd.pivot_table(data=covid_df, values=['Confirmed', 'Cured', 'Deaths'], index='State/UnionTerritory')

# Creating Recovery rate and Mortality rate column
statewise['Recovery_rate'] = statewise['Cured'] * 100 / statewise['Confirmed']
statewise['Mortality_rate'] = statewise['Deaths'] * 100 / statewise['Confirmed']
statewise = statewise.sort_values(by='Confirmed', ascending=False)
print(statewise.style.background_gradient(cmap='cubehelix'))

# Top 10 Active case based on states
top_10_active_cases = covid_df.groupby('State/UnionTerritory')[['Active_cases', 'Date']].max().sort_values(by='Active_cases', ascending=False).reset_index()

# Visualize the top 10 active cases 
plt.figure(figsize=(10, 6))
sns.barplot(data=top_10_active_cases.iloc[:10, :], x='State/UnionTerritory', y='Active_cases')
plt.title('Top 10 Active Cases in India')
plt.xlabel('States')
plt.xticks(rotation=65)
plt.ylabel('Active Cases')
plt.savefig('D:\Projects\DATA_ANALYST_PROJECTS\Covid Analysis using Python/visualizations/top_10_active_cases.png')
plt.show()

# Top states with highest deaths
top_10_death_cases = covid_df.groupby('State/UnionTerritory')[['Deaths', 'Date']].max().sort_values(by='Deaths', ascending=False).reset_index()

# Visualize the top 10 highest death cases 
plt.figure(figsize=(10, 6))
sns.barplot(data=top_10_death_cases.iloc[:12, :], x='State/UnionTerritory', y='Deaths')
plt.title('Top 10 Highest Cases in India')
plt.xlabel('States')
plt.xticks(rotation=65)
plt.ylabel('Death Cases')
plt.savefig('D:\Projects\DATA_ANALYST_PROJECTS\Covid Analysis using Python/visualizations/top_10_death_cases.png')
plt.show()

# Growth Trend
plt.figure(figsize=(15, 7))
sns.lineplot(data=covid_df[covid_df['State/UnionTerritory'].isin(['Maharashtra', 'Karnataka', 'Kerala', 'Tamil Nadu', 'Uttar Pradesh'])], x='Date', y='Active_cases', hue='State/UnionTerritory')
plt.title('Top 5 Affected States in India')
plt.xlabel('Date')
plt.ylabel('Active Case')
plt.savefig('D:\Projects\DATA_ANALYST_PROJECTS\Covid Analysis using Python/visualizations/top_5_affected_states.png')
plt.show()

# Renaming columns in the vaccine dataset
vaccine_df.rename(columns={'Updated On': 'vaccine_date'}, inplace=True)
vaccine_df = vaccine_df[vaccine_df['State'] != 'India']  # Removing Value error row in State Column
vaccine_df.rename(columns={'Total Individuals Vaccinated': 'Total'}, inplace=True)

# Display the information of dataset
print(vaccine_df.info())

# Visualizing the male and female vaccination
male = vaccine_df['Male(Individuals Vaccinated)'].sum()
female = vaccine_df['Female(Individuals Vaccinated)'].sum()
fig = px.pie(names=['Male', 'Female'], values=[male, female], title='Male and Female Vaccination')
fig.show()

# Most Vaccinated State in India
most_vacc = vaccine_df.groupby('State')['Total'].sum().sort_values(ascending=False).reset_index()

# Visualizing top 5 vaccinated states in India
plt.figure(figsize=(10, 5))
sns.barplot(data=most_vacc.iloc[:5, :], x='State', y='Total')
plt.title('Top 5 Vaccinated State in India')
plt.xlabel('States')
plt.ylabel('Vaccinations')
plt.savefig('D:\Projects\DATA_ANALYST_PROJECTS\Covid Analysis using Python/visualizations/top_5_vaccinated_states.png')
plt.show()

# Visualizing least 5 vaccinated states in India
plt.figure(figsize=(10, 5))
sns.barplot(data=most_vacc.iloc[-5:, :], x='State', y='Total')
plt.title('Least 5 Vaccinated State in India')
plt.xlabel('States')
plt.xticks(rotation=65)
plt.ylabel('Vaccinations')
plt.savefig('D:\Projects\DATA_ANALYST_PROJECTS\Covid Analysis using Python/visualizations/least_5_vaccinated_states.png')
plt.show()