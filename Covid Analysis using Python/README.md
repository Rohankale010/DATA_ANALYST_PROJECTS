# COVID Data Analysis Project

This project involves analyzing COVID-19 data in India using Python. The analysis includes data on COVID-19 cases and vaccination statistics across different states.

## Table of Contents

- [Project Overview](#project-overview)
- [Project Structure](#project-structure)
- [Installation and Setup](#installation-and-setup)
- [Data Sources](#data-sources)
- [Analysis](#analysis)
- [Visualizations](#visualizations)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The COVID Data Analysis project aims to explore and visualize the spread and impact of COVID-19 in India. The project includes:
- Data cleaning and preprocessing
- Calculation of active, cured, and death cases
- State-wise analysis of COVID-19 cases
- Vaccination statistics
- Visualization of the findings

## Project Structure
DATA_ANALYST_PROJECTS/
 ├── Covid Analysis using Python/
     ├── data/
     │   ├── covid_19_india.csv
     │   ├── covid_vaccine_statewise.csv
     ├── notebooks/
     │   ├── covid_data_analysis.ipynb
     ├── scripts/
     │   ├── covid_data_analysis.py
     ├── visualizations/
     │   ├── top_10_active_cases.png
     │   ├── top_10_death_cases.png
     │   ├── top_5_affected_states.png
     │   ├── top_5_vaccinated_states.png
     │   ├── least_5_vaccinated_states.png
     ├── README.md
     ├── requirements.txt


## Installation and Setup

To run the project, follow these steps:


1. **Clone the repository:**
    ```bash
    git clone https://github.com/Rohankale010/DATA_ANALYST_PROJECTS.git
    cd DATA_ANALYST_PROJECTS/Covid Analysis using Python
    ``

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS and Linux:
      ```bash
      source venv/bin/activate
      ```

4. **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```

5. **Run the analysis script:**
    ```bash
    python scripts/covid_data_analysis.py
    ```

## Data Sources

- [COVID-19 India Data](https://www.kaggle.com/sudalairajkumar/covid19-in-india)
- [COVID-19 Vaccination Data](https://www.kaggle.com/sudalairajkumar/covid19-in-india)

## Analysis

The analysis includes:
- Cleaning and preprocessing of the COVID-19 dataset.
- Calculation of active cases, recovery rates, and mortality rates.
- State-wise pivot tables and statistical summaries.
- Visualization of top states with active cases and deaths.
- Analysis and visualization of vaccination data.

## Visualizations

The project generates several visualizations, saved in the `visualizations/` directory:
- **Top 10 Active Cases in India:** `top_10_active_cases.png`
- **Top 10 Highest Death Cases in India:** `top_10_death_cases.png`
- **Top 5 Affected States in India:** `top_5_affected_states.png`
- **Top 5 Vaccinated States in India:** `top_5_vaccinated_states.png`
- **Least 5 Vaccinated States in India:** `least_5_vaccinated_states.png`

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
