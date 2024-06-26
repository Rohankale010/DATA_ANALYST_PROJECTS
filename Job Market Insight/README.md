# WebScraping Naukri.com for Job Insights

This project involves scraping job listings from Naukri.com to gather job insights for various positions in different locations. The project is structured to be modular and maintainable.

## Table of Contents

- [Project Structure](#project-structure)
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
  - [Running the Scraper](#running-the-scraper)
  - [Using the Jupyter Notebook](#using-the-jupyter-notebook)
- [Project Modules](#project-modules)
  - [`job_scraper/scraper.py`](#job_scraperscraperpy)
  - [`job_scraper/utils.py`](#job_scraperutilspy)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)
- [Contact](#contact)

## Project Structure

<<<<<<< HEAD
<<<<<<< HEAD
```plaintext
Job Market Insight
│
├── job_scraper
│   ├── __init__.py
│   ├── scraper.py
│   └── utils.py
│
├── data
│   └── naukri_job_listings.csv
│
├── notebooks
│   └── WebScraping_(Naukri.com)_Website_for_Job_Insights.ipynb
│
├── requirements.txt
└── README.md
```
<<<<<<< HEAD
=======
WebScraping_Naukri
=======
```plaintext
Job Market Insight
>>>>>>> 7ae394d (Update Project)
│
├── job_scraper
│   ├── __init__.py
│   ├── scraper.py
│   └── utils.py
│
├── data
│   └── naukri_job_listings.csv
│
├── notebooks
│   └── WebScraping_(Naukri.com)_Website_for_Job_Insights.ipynb
│
├── requirements.txt
└── README.md

>>>>>>> e584371 (Update Project)
=======
>>>>>>> 4a99618 (Update Project)

## Overview

The goal of this project is to scrape job data from Naukri.com, including job title, company name, experience required, salary, location, and the date the job was posted. This data can then be used for various analyses and insights into the job market.

## Installation

1. **Clone the repository:**
```bash
    git clone https://github.com/Rohankale010/DATA_ANALYST_PROJECTS.git
<<<<<<< HEAD
<<<<<<< HEAD
    cd Job Market Insight
=======
    cd WebScraping_Naukri
>>>>>>> e584371 (Update Project)
=======
    cd Job Market Insight
>>>>>>> 7ae394d (Update Project)
```

2. **Create a virtual environment:**
```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. **Install the dependencies:**
```bash
    pip install -r requirements.txt
```

## Usage

### Running the Scraper

To run the scraper and collect job data, you can execute the script directly:

```bash
python naukri_scraper/scraper.py
```

## Project Modules

`job_scraper/scraper.py`
This module contains the main scraping logic. It uses Selenium to navigate Naukri.com and collect job listings based on specified job titles and locations.

`job_scraper/utils.py`
This module contains utility functions used by the scraper, such as generating URLs and extracting job data from HTML elements.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request. For any issues or feature requests, please open an issue on GitHub.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgements

This project uses the following open-source packages:

pandas
selenium
webdriver_manager