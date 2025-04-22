
---

```markdown
# HR Analytics: Employee Attrition & Performance Dashboard 📊

A pure analytics project using **SQL** and **Excel** to explore key factors influencing employee attrition, performance, and satisfaction. This project demonstrates how structured data analysis and interactive Excel dashboards can help HR teams make informed retention and workforce optimization decisions.

---

## 📌 Project Objective

To analyze employee data and uncover actionable insights regarding:

- Employee attrition patterns
- Department-wise performance and satisfaction
- Factors contributing to high or low attrition
- Demographic trends (age, gender, marital status)
- The relationship between overtime, income, and job satisfaction

---

## 📁 Dataset Overview

The dataset includes fields such as:

- `EmployeeID`, `Age`, `Gender`, `Department`, `JobRole`
- `MonthlyIncome`, `YearsAtCompany`, `Attrition`
- `JobSatisfaction`, `EnvironmentSatisfaction`, `OverTime`
- `Education`, `MaritalStatus`, `PerformanceRating`
  and more ...
---

## 🧰 Tools & Technologies Used

| Tool       | Purpose                          |
|------------|----------------------------------|
| SQL (MySQL) | Data cleaning, transformation, and querying |
| Excel       | Dashboard creation, charts, KPIs, and interactivity |
| ODBC        | Direct SQL-to-Excel connection for live data updates |

---

## 📊 Dashboard Overview

![HR Analytics Dashboard](<visuals/HR_Analytics_Employee_Attrition_Dashboard.png>)

### Key Features:

- **Attrition KPIs**: Total employees, number & rate of attrition
- **Demographics Analysis**: Age distribution, gender, marital status
- **Department & Role Insights**: Attrition & satisfaction by department/job role
- **Satisfaction Trends**: Cross-analysis of environment/job satisfaction
- **Key Drivers**: Overtime, income level, years at company vs. attrition

---

### 📁 Folder Structure 

```bash
HR_Analytics_Attrition_Performance/
│
├── 📁 data/
│   └── HR-Employee-Attrition.csv                        # Raw dataset used in the project
│
├── 📁 sql_queries/
│   ├── 01_data_cleaning.sql              # SQL queries for data cleaning/preparation
│   └── 02_exploratory_analysis.sql       # SQL queries for EDA
│
├── 📁 excel_dashboard/
│   └── HR_Employee_Attrition.xlsx       # Final Excel dashboard 
│
├── 📁 visuals/
│   └── HR_Analytics_Employee_Attrition_Dashboard.png  # Dashboard image (for README or portfolio)
│
├── README.md
└── requirements.txt
```

---

## 🔍 Analysis Workflow

1. **Data Cleaning & Preprocessing (SQL)**  
   - Handled nulls, duplicates, and data formatting
   - Standardized column names and data types

2. **Exploratory Data Analysis (SQL)**  
   - Age group distributions, department-level attrition
   - Salary Hike Category and satisfaction levels
   - Attrition rates by gender, overtime, job role

3. **KPI Development & Dashboard Integration (Excel)**  
   - PivotTables & Slicers connected via ODBC
   - Dynamic charts, conditional formatting for visuals
   - Interactive filters for department, role, and more

---

## ✅ Key Insights

- **High Attrition** observed among employees with:
  - 1–2 years at the company
  - Overtime responsibilities
  - Low job/environment satisfaction
- **Job Roles & Departments** like Sales and R&D show higher turnover
- **Younger Employees (20–30)** show higher attrition
- **Performance rating alone** isn’t always tied to attrition risk

---


## 🎯 Outcome

- Built an **automated Excel dashboard** connected to SQL via ODBC
- Delivered clear, department-specific **attrition insights**
- Helped simulate **real-world HR reporting scenarios**

---

## 📎 Project Type

- 💼 Industry Simulation: HR Analytics
- 🧠 Skills Applied: Data Cleaning, EDA, KPI Reporting, Dashboard Design
- 📁 Tools: SQL (ODBC), Excel (PivotTables, Slicers)

---


