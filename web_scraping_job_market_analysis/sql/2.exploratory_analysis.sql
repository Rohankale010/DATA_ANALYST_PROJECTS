-- 1. Total Job Listings
SELECT COUNT(*) AS Job_Listing FROM jobs_data;

-- 2. Top 10 Most Common Job Locations
SELECT Location, COUNT(Location) AS job_counts 
FROM jobs_data
GROUP BY Location
ORDER BY job_counts DESC
LIMIT 10;

-- 3. Top 10 Companies Hiring
SELECT Company_Name, COUNT(Company_Name) AS job_counts 
FROM jobs_data
GROUP BY Company_Name
ORDER BY job_counts DESC 
LIMIT 10;

-- 4. Most Common Job Titles
SELECT Job_Title, COUNT(Job_Title) AS frequency 
FROM jobs_data
GROUP BY Job_Title
ORDER BY frequency DESC
LIMIT 10;

-- 5. Experience Level Breakdown
SELECT Experience_Required, COUNT(Experience_Required) AS job_counts 
FROM jobs_data
GROUP BY Experience_Required
ORDER BY job_counts DESC;

-- 6. Salary Range Distribution
SELECT Salary, COUNT(Salary) AS Counts 
FROM jobs_data
GROUP BY Salary
ORDER BY Counts DESC
LIMIT 10;

-- 7. Recently Posted Jobs (within the last 3 days)
SELECT Posted, COUNT(Posted) AS Counts 
FROM jobs_data
WHERE Posted IN ('today', '1', '2', '3')
GROUP BY Posted
ORDER BY Counts DESC;

-- 8. Posting Time Pattern
SELECT Posted, COUNT(*) AS count 
FROM jobs_data
GROUP BY Posted
ORDER BY count DESC;
