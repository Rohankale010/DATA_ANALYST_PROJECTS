-- Create the database
CREATE DATABASE naukri_jobs;

-- Select the database
USE naukri_jobs;

-- Create the jobs_data table
CREATE TABLE jobs_data (
    Job_Title VARCHAR(255),
    Company_Name VARCHAR(255),
    Experience_Required VARCHAR(255),
    Salary VARCHAR(255),
    Location VARCHAR(255),
    Posted VARCHAR(255)
);
