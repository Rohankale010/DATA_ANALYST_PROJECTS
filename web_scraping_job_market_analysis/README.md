
---


```markdown
# 📊 Web Scraping & Job Market Analysis (Data Analyst Roles)

This project is an end-to-end data analytics case study focused on analyzing the **Data Analyst job market** using real-time data from **Naukri.com**. The goal is to extract, clean, analyze, and visualize key insights from job listings across India using Python, SQL, and Power BI.

---

## 🔍 Problem Statement

The job market for Data Analysts in India is growing rapidly. However, it's challenging for job seekers and recruiters to track real-time trends such as:

- What companies are hiring the most Data Analysts?
- What is the average experience required?
- What salary ranges are commonly offered?
- Which cities are hiring the most?
- How often are new jobs posted?

This project answers these questions by scraping live job data and analyzing patterns to uncover actionable insights.

---

## 🧱 Project Structure

```bash
📂 web_scraping_job_market_analysis/
│
├── data/
│   ├── naukri_data_analyst_jobs.csv       # Raw scraped dataset
│   └── cleaned_naukri_jobs.csv            # Cleaned dataset ready for analysis
│
├── notebooks/
│   └── data_cleaning.ipynb                # Perform Data Cleaning before writing in python file
│
├── sql/
│   ├── 1.schema_setup.sql
│   └── 2.exploratory_analysis.sql    # SQL queries for EDA
│
├── scripts/
│   ├── 1.web_scraper.py              # Selenium-based scraper script
│   └── 2.data_cleaning.py            # Cleaning using Pandas and Regex(Regular Expression)
│
├── dashboard/
│   └── Web_Scraping_Data_Analyst_Job_Market_Dashboard.pbix       # Power BI dashboard
│
├── visuals/
│   └── Web_Scraping_Data_Analyst_Job_Market_Dashboard.png         # Dashboard screenshot
│
├── requirements.txt
└── README.md
```

---

## 🔧 Tools & Technologies Used

| Tool             | Purpose                           |
|------------------|-----------------------------------|
| **Python**       | Web scraping, data cleaning       |
| **Selenium**     | Automated job listing extraction  |
| **Pandas**       | Data manipulation and processing  |
| **Regex**        | Text normalization                |
| **MySQL**        | Data exploration and queries      |
| **Power BI**     | Interactive dashboard             |
| **VS Code**      | Development environment           |
| **GitHub**       | Version control and collaboration |

---

## 📥 Data Collection

- **Source:** [Naukri.com](https://www.naukri.com/)
- **Method:** Selenium-based browser automation
- **Role Scraped:** "Data Analyst"
- **Fields Extracted:**  
  `Job Title`, `Company`, `Location`, `Experience Required`, `Salary`, `Posted Date`

---

## 🧹 Data Cleaning

- Removed duplicates and nulls
- Standardized experience values (e.g., "3 months" → 0.25 years)
- Transformed salary formats (e.g., "3L – 6L PA" → numeric range)
- Normalized posting time (e.g., "Just now", "Few hours ago" → "today")
- Cleaned job titles and text fields

Output saved as: `cleaned_naukri_jobs.csv`

---

## 📊 Data Exploration & Analysis (SQL)

Performed SQL-based EDA on cleaned dataset to answer:

- Total Number of Active Job Listings
- Top hiring locations
- Companies with the most job openings
- Distribution of job experience requirements
- Salary range segmentation
- Posting trends over time

Queries stored in: `exploratory_analysis.sql`

---

## 📈 Dashboard Visualization (Power BI)

Built an interactive dashboard in Power BI showing:

### 📌 Dashboard Highlights:
- **Total Jobs Scraped:** `968`
- **Companies Hiring:** `724`
- **Average Experience Required:** `4 years`
- **Top Hiring Cities:** Bengaluru, Hyderabad, Gurgaon
- **Top Hiring Companies:** JPMorgan Chase, Wipro, Capgemini
- **Salary Insights:** Majority of listings did not disclose salary; disclosed ones range from ₹3L–₹20L+

### 📷 Dashboard Preview:

![Data Analyst Job Market Dashboard](<visuals/Web_Scraping_Data_Analyst_Job_Market_Dashboard.png>)

---

## 📚 Key Insights

| Category                  | Insight                                    |
|---------------------------|--------------------------------------------|
| 🔢 **Job Volume**        | 968 Active Data Analyst Job Listings        |
| 🏢 **Top Employers**     | JPMorgan Chase, Wipro, Capgemini            |
| 🌆 **Top Locations**     | Bengaluru, Hyderabad, Gurgaon               |
| 💸 **Salary Range**      | ₹3L–₹20L (where disclosed)                  |
| ⏳ **Experience Level**  | Most roles require 2–5 years of experience  |
| ⏱️ **Job Posting Trend** | High activity in recent days                |


---

## ✅ Project Outcomes

- Automated web scraping pipeline for job data
- Cleaned and structured dataset
- SQL-based EDA for answering business questions
- Professional Power BI dashboard with real-time insights

---


