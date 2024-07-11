# Olympic Data Analysis

## Table of Contents
- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Data](#data)
- [Analysis](#analysis)
- [Visualizations](#visualizations)
- [Requirements](#requirements)
- [Conclusion](#conclusion)

## Introduction
This Project involves analysis of Olympic data to derive insights about Olympic games.The analysis cover aspects such as athlete participation,age distribution,gender distribution,women participation,gold medal achievement across different country and seasons

## Project Structure
```
Olympic Data Analysis/
├── data/
│   ├── athlete_events.csv
│   └── noc_regions.csv
│   └── processed_athlete_events.csv
├── analysis/
│   ├── data_preprocessing.py
│   ├── overall_participation.py
│   ├── age_distribution.py
│   ├── gender_distribution.py
│   ├── women_participation.py
│   ├── gold_medal_analysis.py
│   └── rio_olympics_analysis.py
├── visualizations/
├── README.md
└── requirements.txt
```

## Data

The datasets used in this project are:

- [athlete_events.csv](https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results): Contains information about athletes and their performance in the Olympics.
- [noc_regions.csv](https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results): Contains information about the National Olympic Committees (NOCs) and their corresponding regions.

## Analysis 
1. Overall Participation by Country
This analysis shows the top 10 countries with the highest number of athlete participations in the Olympics.


2. Age Distribution of Athletes
This analysis shows the age distribution of athletes participating in the Olympics.


3. Gender Distribution
This analysis shows the gender distribution of athletes in the Olympics.


4. Women Participation in Summer and Winter Olympics
This analysis shows the participation of women athletes in the Summer and Winter Olympics over the years.


5. Gold Medal Analysis
This analysis shows the gold medals won by athletes over the age of 60 and the top 5 countries with the highest number of gold medals.



6. Rio Olympics Gold Medal Analysis
This analysis shows the countries that won gold medals in the Rio Olympics.


## Visualizations
The visualizations folder contains the following plots:
- `age_distribution.png`: Distribution of Age of Athlete.
- `gender_distribution.png`: Distribution of Gender of Athlete.
- `gold_medals_over_60.png`: Athlete who won Gold over age 60.
- `gold_medal_per_country.png`: Gold Medal win by Country.
- `overall_participation.png`: Participation of Athlete as per Country.
- `rio_olympics_gold_medals.png`: Gold Medal win in Rio Olympic.
- `women_participation_over_time.png`: Women participation across the season.
- `women_participation_summer.png`: Number of Women participation in Summer season.
- `women_participation_winter.png`: Number of Women participation in Winter season.

<<<<<<< HEAD
## Requirements
To run the analysis scripts, you need the following Python libraries:
- pandas
- numpy
- matplotlib
- seaborn

You can install the required libraries using:
```bash
pip install -r requirements.txt
```
=======
>>>>>>> d9fbd59 (Update Project)

## Conclusion
The Olympic Data Analysis project provides insights into various aspects of the Olympic Games, including participation trends, age and gender distribution, and medal achievements. These analyses help in understanding the dynamics and evolution of the Olympics over the years.