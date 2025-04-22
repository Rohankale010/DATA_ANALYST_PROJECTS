import pandas as pd
import re

# Load the Dataset
df=pd.read_csv('D:\Projects\DATA_ANALYST_PROJECTS\web_scraping_job_market_analysis\data/naukri_data_analyst_jobs.csv')

# Drop Duplicates
df.drop_duplicates(inplace=True)

# Drop Null and Missing value
df.dropna(inplace=True)


df['Experience Required'] = df['Experience Required'].replace(
    to_replace=r'\d{2} [A-Za-z]{3} - \d{2} [A-Za-z]{3}', #\d{2} = two digits (like 09) ,[A-Za-z]{3} = three letters (like Apr)
    value=0, 
    regex=True
)
df['Experience Required']=df['Experience Required'].replace({'3 months duration':0.25,'6 months duration':0.5,'No fixed duration':0})
df['Experience Required']=df['Experience Required'].replace(to_replace='Yrs',value='',regex=True)


df['Salary']=df['Salary'].replace('(Including Variable: 10.0%)','',regex=True)
df['Salary']=df['Salary'].replace('(Including Variable: 30.0%)','',regex=True)

def convert_salary_range(salary):
    if isinstance(salary,str):      # is use to check we work in string format
        salary=salary.replace('PA','')
        salary=salary.replace('()','').strip()

    if '-' in salary:
        parts=salary.split('-')
        low=parts[0].strip()
        high=parts[1].strip()

        if ',' in low:
            low=low.replace(',','').strip()
        else:
            low=float(low)*100000

        if ',' in high:
            high=high.replace(',','').strip()
        else:
            high=float(high.replace('Lacs',''))*100000

        return str(int(low)) + '-' + str(int(high))
    
    elif '/month' in salary.lower():
        amounts=salary.replace('/month','').replace(',','').strip()
        return str(int(amounts)*12)
    
    else:
        return salary
    
df['Salary']=df['Salary'].apply(convert_salary_range)



df['Posted']=df['Posted'].replace({'Day Ago':'','Days Ago':'','Few Hours Ago':'today','Just Now':'today','Starts in 1-3 months':'later',"Starts : 17th Apr' 25":'later'},regex=True) 



df['Job Title']=df['Job Title'].apply(lambda x:x.split('-')[0].strip())
df['Job Title']=df['Job Title'].replace('Walk','MIS/Operations/Data Analyst')

df.to_csv('D:\Projects\DATA_ANALYST_PROJECTS\web_scraping_job_market_analysis\data/cleaned_naukri_jobs.csv',index=False)