from selenium.webdriver.common.by import By

def generate_url(job_title, location, page_number=1):
    job_title_encoded = job_title.replace(" ", "-")
    location_encoded = location.replace(" ", "-")
    return f'https://www.naukri.com/{job_title_encoded}-jobs-in-{location_encoded}-{page_number}?k={job_title_encoded}&l={location_encoded}'

def scrape_jobs(driver, job_data):
    job_listings = driver.find_elements(By.CLASS_NAME, 'srp-jobtuple-wrapper')
    for listing in job_listings:
        try:
            job_title_element = listing.find_element(By.CLASS_NAME, 'title')
            job_title = job_title_element.text.strip()

            company_name_element = listing.find_element(By.CLASS_NAME, 'comp-name')
            company_name = company_name_element.text.strip()

            experience_element = listing.find_element(By.CLASS_NAME, 'exp-wrap')
            experience = experience_element.text.strip()

            salary_element = listing.find_element(By.CLASS_NAME, 'sal-wrap')
            salary = salary_element.text.strip()

            location_element = listing.find_element(By.CLASS_NAME, 'loc-wrap')
            location = location_element.text.strip()

            posted_day_element = listing.find_element(By.CLASS_NAME, 'job-post-day')
            posted = posted_day_element.text.strip()

            # Append the job data to the list
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
