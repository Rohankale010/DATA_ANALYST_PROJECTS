from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd
from utils import generate_url, scrape_jobs

def scrape_job_data(job_titles, locations, max_pages=200):
    # Initialize the WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    all_job_data = []
    for job_title in job_titles:
        for location in locations:
            print(f"Scraping jobs for {job_title} in {location}...")
            page = 1

            while page <= max_pages:
                url = generate_url(job_title, location, page)
                print(f"Scraping URL: {url}")
                driver.get(url)
                time.sleep(5)  # Adjust the sleep time as necessary

                all_job_data = scrape_jobs(driver, all_job_data)
                
                # If no jobs are found on the page, break out of the loop
                if not driver.find_elements(By.CLASS_NAME, 'srp-jobtuple-wrapper'):
                    print(f"No more job listings found on page {page}. Stopping.")
                    break

                page += 1

    # Close the WebDriver
    driver.quit()

    return all_job_data

if __name__ == "__main__":
    job_titles = ['data-analyst', 'data-scientist', 'data-engineer']
    locations = ['india']  # ['mumbai', 'pune', 'bangalore']
    max_pages = 200

    job_data = scrape_job_data(job_titles, locations, max_pages)

    # Convert the list to a pandas DataFrame
    df = pd.DataFrame(job_data)

    # Save the DataFrame to a CSV file
    df.to_csv('D:\Projects\DATA_ANALYST_PROJECTS\Job Market Insight\data/naukri_job_listings.csv', index=False)

    # Display the DataFrame
    print(df.head())
