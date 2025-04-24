import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.stats.proportion import proportions_ztest

# Load Dataset
df=pd.read_csv('D:\Projects\DATA_ANALYST_PROJECTS\A_B Testing – Website Conversion Rate Optimization\data/ab_cleaned_data.csv',parse_dates=['timestamp'])

# Overall Conversion Rate
overall_conv=df['converted'].mean()
print(f'Overall Conversion Rate : {overall_conv:.2%}')

# Conversion Rate by Group
group_rates=df.groupby('group')['converted'].mean().reset_index()

sns.barplot(data=group_rates,x='group',y='converted')
plt.title('Conversion Rate : Control vs Treatment')
plt.xlabel('Group')
plt.ylabel('Conversion Rate')
plt.savefig('D:\Projects\DATA_ANALYST_PROJECTS\A_B Testing – Website Conversion Rate Optimization/visuals/Conversion Rate-Control vs Treatment.png')
plt.show()

# Conversion Rate by Group over time
df['date']=df['timestamp'].dt.date

daily=df.groupby(['date','group'])['converted'].mean().reset_index()

plt.figure(figsize=(12,5))
sns.lineplot(data=daily,x='date',y='converted',hue='group')
plt.title('Daily Conversion Rate by Group')
plt.xlabel('Date')
plt.ylabel('Conversion Rate')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('D:\Projects\DATA_ANALYST_PROJECTS\A_B Testing – Website Conversion Rate Optimization/visuals/Daily Conversion Rate by Group.png')
plt.show()

# Distribution of Converter vs Non converter
sns.countplot(data=df,x='converted',hue='group')
plt.title('Count : Converted vs Non - Converted by Group')
plt.xlabel('Converted')
plt.ylabel('Count')
plt.savefig('D:\Projects\DATA_ANALYST_PROJECTS\A_B Testing – Website Conversion Rate Optimization/visuals/Count-Converted vs Non - Converted by Group.png')
plt.show()

# Group Distribution
counts=df['group'].value_counts().reset_index()

plt.pie(x=counts['group'],labels=counts['index'],autopct="%.2f%%")
plt.title('Distribution of Users in Control vs Treatment')
plt.tight_layout()
plt.savefig('D:\Projects\DATA_ANALYST_PROJECTS\A_B Testing – Website Conversion Rate Optimization/visuals/Distribution of Users in Control vs Treatment.png')
plt.show()

# Hypothesis Testing 
control=df[df['group']=='control']
treatment=df[df['group']=='treatment']

n_control=control.shape[0]
n_treatment=treatment.shape[0]

conv_control=control['converted'].sum()
conv_treatment=treatment['converted'].sum()
print(f"Control: {conv_control}/{n_control} conversions")
print(f"Treatment: {conv_treatment}/{n_treatment} conversions")

# Perform Two Proportion Z test
# Counts and Sample sizes
counts=[conv_treatment,conv_control]
nobs=[n_treatment,n_control]

stats,pval=proportions_ztest(count=counts,nobs=nobs,alternative='two-sided')

print(f'Z-Statistics:{stats:0.4f}')
print(f'P-value:{pval:0.4f}')

#Interpret Results

##If p-value < 0.05, we reject H₀ and conclude there is a significant difference in conversion rates.

##If p-value ≥ 0.05, we fail to reject H₀ and conclude there is no significant difference.
