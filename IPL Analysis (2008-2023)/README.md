# IPL Data Analysis

## Table of Contents
- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Data](#data)
- [Analysis](#analysis)
- [Visualizations](#visualizations)
- [Requirements](#requirements)
<<<<<<< HEAD
=======
- [Usage](#usage)
>>>>>>> 984ba14 (Update Project)
- [Conclusion](#conclusion)

## Introduction
This project involves the analysis of IPL (Indian Premier League) cricket data to derive insights about player performances, team qualifications, and match outcomes. The analysis covers aspects such as top run-scorers, top wicket-takers, boundary hitters, team qualifications, and performance in IPL 2023.

## Project Structure
```
IPL Data Analysis(2008-2023)
│
├── data
│ ├── deliveries.csv
│ └── matches.csv
│
├── notebooks
│ └── IPL_Data_Analysis.ipynb
│
├── analysis
│ ├── runs_analysis.py
│ ├── wickets_analysis.py
│ ├── boundaries_analysis.py
│ ├── qualification_analysis.py
│ └── ipl_2023_analysis.py
│
├── visualizations
│ ├── top_run_scorers.png
│ ├── kohli_runs_by_season.png
│ ├── top_wicket_takers.png
│ ├── bravo_wickets_by_season.png
│ ├── top_boundary_scorers.png
│ ├── top_qualifying_teams.png
│ ├── top_run_scorers_2023.png
│ ├── top_wicket_takers_2023.png
│ └── trophy_wins.png
│
├── requirements.txt
└── README.md
```


## Data
The dataset used in this project includes two CSV files:
- [deliveries.csv](https://www.kaggle.com/datasets/patrickb1912/ipl-complete-dataset-20082020): Contains ball-by-ball details of all matches.
- [matches.csv](https://www.kaggle.com/datasets/patrickb1912/ipl-complete-dataset-20082020): Contains details of all matches played.

## Analysis
The analysis is divided into several scripts focusing on different aspects:
- `runs_analysis.py`: Analysis of top run-scorers.
- `wickets_analysis.py`: Analysis of top wicket-takers.
- `boundaries_analysis.py`: Analysis of boundary hitters.
- `qualification_analysis.py`: Analysis of team qualifications in the league.
- `ipl_2023_analysis.py`: Specific analysis of IPL 2023 season.

## Visualizations
The visualizations folder contains the following plots:
- `top_run_scorers.png`: Top run-scorers in IPL.
- `kohli_runs_by_season.png`: Runs scored by Virat Kohli across seasons.
- `top_wicket_takers.png`: Top wicket-takers in IPL.
- `bravo_wickets_by_season.png`: Wickets taken by DJ Bravo across seasons.
- `top_boundary_scorers.png`: Top boundary hitters.
- `top_qualifying_teams.png`: Teams with the most qualifications in IPL.
- `top_run_scorers_2023.png`: Top run-scorers in IPL 2023.
- `top_wicket_takers_2023.png`: Top wicket-takers in IPL 2023.
- `trophy_wins.png`: Number of trophy wins by each team.

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

## Conclusion
This project provides a comprehensive analysis of IPL data, highlighting key player performances and team achievements. The visualizations offer clear insights into the trends and patterns in the IPL over the years, making it easier to understand the dynamics of the league.