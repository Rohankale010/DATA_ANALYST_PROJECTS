# web_scraper_naukri.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# Generate URL only for job title (Data Analyst), all locations
def generate_url(job_title, page_number=1):
    job_title_encoded = job_title.replace(" ", "-")
    return f'https://www.naukri.com/{job_title_encoded}-jobs-{page_number}?k={job_title_encoded}'

# Extract job listing data from the page
def scrape_jobs(driver, job_data):
    job_listings = driver.find_elements(By.CLASS_NAME, 'srp-jobtuple-wrapper')
    for listing in job_listings:
        try:
            job_title = listing.find_element(By.CLASS_NAME, 'title').text.strip()
            company_name = listing.find_element(By.CLASS_NAME, 'comp-name').text.strip()
            experience = listing.find_element(By.CLASS_NAME, 'exp-wrap').text.strip()
            salary = listing.find_element(By.CLASS_NAME, 'sal-wrap').text.strip()
            location = listing.find_element(By.CLASS_NAME, 'loc-wrap').text.strip()
            posted = listing.find_element(By.CLASS_NAME, 'job-post-day').text.strip()

            job_data.append({
                'Job Title': job_title,
                'Company Name': company_name,
                'Experience Required': experience,
                'Salary': salary,
                'Location': location,
                'Posted': posted
            })
        except Exception as e:
            print(f"Error extracting job listing: {e}")
    
    return job_data

# Main function to scrape jobs for "Data Analyst" only (all locations)
def scrape_job_data(job_title='data-analyst', max_pages=50):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    all_job_data = []

    for page in range(1, max_pages + 1):
        url = generate_url(job_title, page)
        print(f"Scraping Page {page}: {url}")
        driver.get(url)
        time.sleep(5)

        if not driver.find_elements(By.CLASS_NAME, 'srp-jobtuple-wrapper'):
            print(f"No more job listings found on page {page}. Stopping.")
            break

        all_job_data = scrape_jobs(driver, all_job_data)

    driver.quit()
    return all_job_data

# Run scraper
data = scrape_job_data()
df = pd.DataFrame(data)
df.to_csv('D:\Projects\DATA_ANALYST_PROJECTS\web_scraping_job_market_analysis\data/naukri_data_analyst_jobs.csv', index=False)
print("Saved scraped data to 'naukri_data_analyst_jobs.csv'")
