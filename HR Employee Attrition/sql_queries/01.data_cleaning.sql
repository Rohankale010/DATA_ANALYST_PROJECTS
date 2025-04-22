-- CREATE DATABASE AND TABLE
CREATE DATABASE hr_analytics;
USE hr_analytics;

CREATE TABLE employee_data (
    EmployeeID INT PRIMARY KEY,
    Age INT,
    Attrition VARCHAR(5),
    BusinessTravel VARCHAR(50),
    DailyRate INT,
    Department VARCHAR(50),
    DistanceFromHome INT,
    Education INT,
    EducationField VARCHAR(50),
    EmployeeCount INT,
    EnvironmentSatisfaction INT,
    Gender VARCHAR(10),
    HourlyRate INT,
    JobInvolvement INT,
    JobLevel INT,
    JobRole VARCHAR(50),
    JobSatisfaction INT,
    MaritalStatus VARCHAR(50),
    MonthlyIncome INT,
    MonthlyRate INT,
    NumCompaniesWorked INT,
    Over18 VARCHAR(2),
    OverTime VARCHAR(10),
    PercentSalaryHike INT,
    PerformanceRating INT,
    RelationshipSatisfaction INT,
    StandardHours INT,
    StockOptionLevel INT,
    TotalWorkingYears INT,
    TrainingTimesLastYear INT,
    WorkLifeBalance INT,
    YearsAtCompany INT,
    YearsInCurrentRole INT,
    YearsSinceLastPromotion INT,
    YearsWithCurrManager INT
);

-- CHECK FOR NULL/MISSING VALUES
SELECT 'EmployeeID' AS Column_names, COUNT(*) FROM employee_data WHERE EmployeeID IS NULL
UNION ALL
SELECT 'Age', COUNT(*) FROM employee_data WHERE Age IS NULL
UNION ALL 
SELECT 'Attrition', COUNT(*) FROM employee_data WHERE Attrition IS NULL
UNION ALL 
SELECT 'BusinessTravel', COUNT(*) FROM employee_data WHERE BusinessTravel IS NULL
UNION ALL 
SELECT 'DailyRate', COUNT(*) FROM employee_data WHERE DailyRate IS NULL
UNION ALL 
SELECT 'Department', COUNT(*) FROM employee_data WHERE Department IS NULL
UNION ALL 
SELECT 'DistanceFromHome', COUNT(*) FROM employee_data WHERE DistanceFromHome IS NULL
UNION ALL 
SELECT 'Education', COUNT(*) FROM employee_data WHERE Education IS NULL
UNION ALL 
SELECT 'EducationField', COUNT(*) FROM employee_data WHERE EducationField IS NULL
UNION ALL 
SELECT 'EmployeeCount', COUNT(*) FROM employee_data WHERE EmployeeCount IS NULL
UNION ALL 
SELECT 'EnvironmentSatisfaction', COUNT(*) FROM employee_data WHERE EnvironmentSatisfaction IS NULL
UNION ALL 
SELECT 'Gender', COUNT(*) FROM employee_data WHERE Gender IS NULL
UNION ALL 
SELECT 'HourlyRate', COUNT(*) FROM employee_data WHERE HourlyRate IS NULL
UNION ALL 
SELECT 'JobInvolvement', COUNT(*) FROM employee_data WHERE JobInvolvement IS NULL
UNION ALL 
SELECT 'JobLevel', COUNT(*) FROM employee_data WHERE JobLevel IS NULL
UNION ALL 
SELECT 'JobRole', COUNT(*) FROM employee_data WHERE JobRole IS NULL
UNION ALL 
SELECT 'JobSatisfaction', COUNT(*) FROM employee_data WHERE JobSatisfaction IS NULL
UNION ALL 
SELECT 'MaritalStatus', COUNT(*) FROM employee_data WHERE MaritalStatus IS NULL
UNION ALL 
SELECT 'MonthlyIncome', COUNT(*) FROM employee_data WHERE MonthlyIncome IS NULL
UNION ALL 
SELECT 'MonthlyRate', COUNT(*) FROM employee_data WHERE MonthlyRate IS NULL
UNION ALL 
SELECT 'NumCompaniesWorked', COUNT(*) FROM employee_data WHERE NumCompaniesWorked IS NULL
UNION ALL 
SELECT 'Over18', COUNT(*) FROM employee_data WHERE Over18 IS NULL
UNION ALL 
SELECT 'OverTime', COUNT(*) FROM employee_data WHERE OverTime IS NULL
UNION ALL 
SELECT 'PercentSalaryHike', COUNT(*) FROM employee_data WHERE PercentSalaryHike IS NULL
UNION ALL 
SELECT 'PerformanceRating', COUNT(*) FROM employee_data WHERE PerformanceRating IS NULL
UNION ALL 
SELECT 'RelationshipSatisfaction', COUNT(*) FROM employee_data WHERE RelationshipSatisfaction IS NULL
UNION ALL 
SELECT 'StandardHours', COUNT(*) FROM employee_data WHERE StandardHours IS NULL
UNION ALL 
SELECT 'StockOptionLevel', COUNT(*) FROM employee_data WHERE StockOptionLevel IS NULL
UNION ALL 
SELECT 'TotalWorkingYears', COUNT(*) FROM employee_data WHERE TotalWorkingYears IS NULL
UNION ALL 
SELECT 'TrainingTimesLastYear', COUNT(*) FROM employee_data WHERE TrainingTimesLastYear IS NULL
UNION ALL 
SELECT 'WorkLifeBalance', COUNT(*) FROM employee_data WHERE WorkLifeBalance IS NULL
UNION ALL 
SELECT 'YearsAtCompany', COUNT(*) FROM employee_data WHERE YearsAtCompany IS NULL
UNION ALL 
SELECT 'YearsInCurrentRole', COUNT(*) FROM employee_data WHERE YearsInCurrentRole IS NULL
UNION ALL 
SELECT 'YearsSinceLastPromotion', COUNT(*) FROM employee_data WHERE YearsSinceLastPromotion IS NULL
UNION ALL 
SELECT 'YearsWithCurrManager', COUNT(*) FROM employee_data WHERE YearsWithCurrManager IS NULL;

-- REMOVE DUPLICATE EMPLOYEE RECORDS
WITH duplicates AS (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY EmployeeID ORDER BY EmployeeID) AS row_num
    FROM employee_data
)
DELETE FROM employee_data
WHERE EmployeeID IN (
    SELECT EmployeeID FROM duplicates WHERE row_num > 1
);

-- CHECK FOR INVALID NUMERIC VALUES
SELECT Age, DailyRate, HourlyRate, MonthlyIncome, MonthlyRate
FROM employee_data
WHERE Age <= 0 OR DailyRate <= 0 OR HourlyRate <= 0 OR MonthlyIncome <= 0 OR MonthlyRate <= 0;

-- CHECK DISTINCT VALUES FOR CATEGORICAL COLUMNS
SELECT DISTINCT Attrition FROM employee_data;
SELECT DISTINCT BusinessTravel FROM employee_data;
SELECT DISTINCT Department FROM employee_data;
SELECT DISTINCT Education FROM employee_data;
SELECT DISTINCT EducationField FROM employee_data;
SELECT DISTINCT Gender FROM employee_data;
SELECT DISTINCT JobRole FROM employee_data;
SELECT DISTINCT MaritalStatus FROM employee_data;
SELECT DISTINCT Over18 FROM employee_data;
SELECT DISTINCT OverTime FROM employee_data;
