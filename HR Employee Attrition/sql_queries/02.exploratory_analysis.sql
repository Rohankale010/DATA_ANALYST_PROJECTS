-- OVERALL ATTRITION RATE
SELECT Attrition,
       COUNT(*) AS Total_Employees,
       ROUND((COUNT(*) * 100.0) / (SELECT COUNT(*) FROM employee_data), 2) AS Percentage
FROM employee_data
GROUP BY Attrition;

-- ATTRITION BY DEPARTMENT
SELECT Department,
       SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS Employee_left,
       ROUND(SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS Percentage
FROM employee_data
GROUP BY Department
ORDER BY Percentage DESC;

-- SALARY HIKE IMPACT ON ATTRITION
WITH employee_left AS (
    SELECT PercentSalaryHike FROM employee_data WHERE Attrition = 'Yes'
)
SELECT 
    CASE 
        WHEN PercentSalaryHike BETWEEN 10 AND 15 THEN 'Low'
        WHEN PercentSalaryHike BETWEEN 16 AND 20 THEN 'Moderate'
        ELSE 'High'
    END AS Salary_Hike_Category,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM employee_left), 2) AS Percentage
FROM employee_left
GROUP BY Salary_Hike_Category
ORDER BY Percentage DESC;

-- ATTRITION BY GENDER
SELECT Gender,
       SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS Employee_left,
       ROUND(SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS Percentage
FROM employee_data
GROUP BY Gender
ORDER BY Percentage DESC;

-- AVERAGE MONTHLY INCOME BY JOB ROLE
SELECT JobRole,
       ROUND(AVG(MonthlyIncome), 2) AS Avg_Income
FROM employee_data
GROUP BY JobRole
ORDER BY Avg_Income DESC;

-- ATTRITION VS JOB SATISFACTION
SELECT JobSatisfaction,
       SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS Employee_left,
       ROUND(SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS Percentage
FROM employee_data
GROUP BY JobSatisfaction
ORDER BY Percentage DESC;

--  MONTHLY INCOME DETAIL
SELECT Attrition,
       AVG(MonthlyIncome) AS AvgIncome,
       MIN(MonthlyIncome) AS MinIncome,
       MAX(MonthlyIncome) AS MaxIncome
FROM employee_data
GROUP BY Attrition;

-- OVERTIME VS ATTRITION
SELECT OverTime,
       SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS Employee_left,
       ROUND(SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS Percentage
FROM employee_data
GROUP BY OverTime
ORDER BY Percentage DESC;

-- ATTRITION BY AGE GROUP
WITH employee_left AS (
    SELECT Age, Attrition FROM employee_data
)
SELECT 
    CASE
        WHEN Age BETWEEN 18 AND 25 THEN 'Early Career (18-25)'
        WHEN Age BETWEEN 26 AND 35 THEN 'Young (26-35)'
        WHEN Age BETWEEN 36 AND 45 THEN 'Mid (36-45)'
        WHEN Age BETWEEN 46 AND 55 THEN 'Senior (46-55)'
        ELSE 'Late Career (56+)'
    END AS Age_Group,
    COUNT(*) AS Employee_Left,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM employee_left), 2) AS Percent
FROM employee_left
GROUP BY Age_Group
ORDER BY Employee_Left DESC;

-- ATTRITION BY YEARS AT COMPANY
SELECT YearsAtCompany,
       SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS Employee_left
FROM employee_data
GROUP BY YearsAtCompany
ORDER BY YearsAtCompany;
