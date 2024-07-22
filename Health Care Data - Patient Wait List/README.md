# Healthcare Data - Patient Wait List Analysis

## Table of Contents

- [Project Overview](#project-overview)
- [Project Structure](#project-structure)
- [Objective](#objective)
- [Dataset](#dataset)
- [Dataset](#dataset)
- [Tools Used](#tools-used)
- [Key Insights](#key-insights)
- [Visualizations](#visualizations)
- [Conclusion](#conclusion)


## Project Overview
This project analyzes patient waitlist data from healthcare facilities to provide insights into waitlist volumes, bifurcation by case type, monthly trends, and detailed views by specialty and case type.

## Project Structure
```plaintext
 Healthcare Data - Patient Wait List /
     ├── data/
     │   ├── Inpatient
     │   │    ├──IN_WL 2018.csv
     │   │    ├──IN_WL 2019.csv 
     │   │    ├──IN_WL 2020.csv 
     │   │    ├──IN_WL 2021.csv       
     │   ├── Outpatient
     │   │    ├──Op_WL 2018.csv
     │   │    ├──Op_WL 2019.csv
     │   │    ├──Op_WL 2020.csv
     │   │    ├──Op_WL 2021.csv
     │   ├── Mapping_Specialty.csv
     │
     ├── analysis/
     │   ├── analysis.md
     │
     ├── dashboard/
     │   ├── Healthcare Data - Patient Wait List.pbix
     │   ├── Summary - Health Care Data.png
     │   ├── Detailed View - Health Care Data.png
     │   ├── Drilled Down - Health Care Data.png
     │
     ├── README.md
     ├── requirements.txt
```

## Objective
To analyze patient wait list data to provide actionable insights and identify key trends that can help in managing and reducing wait times.

## Dataset
- **Source:** Healthcare Data
- **Time Frame:** 31-01-2018 to 31-03-2021
- **Fields:** Archive_Date, Specialty_Name, Case_Type, Time_Bands, Age_Profile, Total

## Tools Used
- **Power BI:** Used for data visualization and analysis.

## Key Insights
1. **Wait List Comparison:**
   - Latest Month Wait List: 709K
   - Previous Year Month Wait List: 640K

2. **Waitlist Bifurcation by Case Type:**
   - Outpatient: 12 (10.62%)
   - Day Case: 19 (16.98%)
   - Inpatient: 80 (72.4%)

3. **Time Band vs Age Profile:**
   - Age Profiles: 0-15, 16-45, 46-64, 65+
   - Time Bands: 0-3 months, 3-6 months, 6-9 months, 9-12 months, 12-15 months, 15-18 months, 18+ months

4. **Top 4 Wait List by Specialty:**
   - Accident & Emergency: 111
   - Paed Orthopaedic: 115
   - Paediatric Dermatology: 168
   - Paediatric ENT: 148

5. **Monthly Trend Analysis:**
   - Monthly trend of waitlist volume by case type (Outpatient, Day Case, Inpatient)

6. **Detailed Grid View:**
   - Detailed breakdown by Archive Date, Specialty, Case Type, and Total waitlist volume.

7. **Total Waitlist and Specialty Group Breakup:**
   - Total Waitlist: 25M
   - Breakdown by Specialty: Orthopaedics, Ophthalmology, General Surgery, etc.

## Visualizations
1. **Summary Dashboard:**
   - Key indicators and comparisons of waitlist volumes
   - Donut chart for waitlist bifurcation by case type
   - Bar charts for time band vs age profile and top waitlist by specialty
   - Line chart for monthly trend analysis
   
   ![Summary](<Dashboard/Summary - Health Care Data.png>)

2. **Detailed View:**
   - Filter criteria: Archive Date, Specialty Name, Case Type, Time Bands, Age Profile
   - Grid view for detailed breakdown by specialty and case type

   ![Detailed View](<Dashboard/Detailed View - Health Care Data.png>)

3. **Drill Down:**
   - Total waitlist and specialty group breakup bar chart

   ![Drill Down](<Dashboard/Drilled Down - Health Care Data.png>)

## Conclusion
This project provides a comprehensive analysis of the patient waitlist data, identifying key trends and insights that can help in better understanding and managing the waitlists in healthcare facilities. The visualizations created in Power BI effectively summarize the data and present it in an easily interpretable manner.