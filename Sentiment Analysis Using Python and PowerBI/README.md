# Sentiment Analysis Project

This project analyzes the sentiment of tweets using the VADER sentiment analysis tool. The data is preprocessed to remove noise and then analyzed to determine the sentiment of each tweet

## Table of Contents
- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Data](#data)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Introduction
This project aims to perform sentiment analysis on a large dataset of tweets. The goal is to clean the text data, analyze the sentiment, and save the results for further analysis.

## Project Structure
```plaintext
Sentiment_Analysis
│
├── data
│   ├── raw
│   │   └── training.1600000.processed.noemoticon.csv
│   └── processed
│       └── cleaned-text.csv
│       └── tweets_sentiments.csv
│
├── notebooks
│   └── sentiment_analysis_notebook.ipynb
│
├── sentiment_analysis
│   ├── __init__.py
│   ├── data_preparation.py
│   └── sentiment_analysis.py
│
├── requirements.txt
└── README.md
```

## Setup Instructions
1. Clone the repository:
```bash
       git clone https://github.com/Rohankale010/DATA_ANALYST_PROJECTS.git
       cd Sentiment Analysis Using Python and PowerBI
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. **Run the Jupyter Notebook**: Navigate to the `notebooks` directory and open `Sentiment_Analysis_using_python_and_powerbi.ipynb`. This notebook will guide you through loading, preprocessing, analyzing sentiment, and saving the data.

2. **Run the Scripts**: Alternatively, you can run the individual scripts located in the `sentiment_analysis` directory.

## Data

The raw data file is downloaded from [Kaggle](https://www.kaggle.com/datasets/kazanova/sentiment140?select=training.1600000.processed.noemoticon.csv) and is located in the `data/raw` directory. After processing and sentiment analysis, the results are saved in the `data/processed` directory.

## Results

The final dataset with sentiment scores and labels is saved as `tweets_sentiments.csv` in the `data/processed` directory.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or new features.

## License
This project is licensed under the `MIT License`.