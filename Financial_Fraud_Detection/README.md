# 💳 Financial Fraud Detection & Risk Analysis

---

## 📌 Project Objective

To detect and analyze fraudulent credit card transactions using real-time machine learning techniques, address data imbalance, and provide actionable insights through data visualizations and dashboards.

---

## 🧰 Tools & Technologies

- **Language:** Python (Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, XGBoost,LightBGM)
- **Modeling:** Logistic Regression, Random Forest, XGBoost, LightBGM, SMOTE (Imbalance Handling)
- **Visualization:** Power BI
- **IDE:** VS Code
- **Data Source:** [creditcard.csv](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)

---

## 📁 Folder Structure

📂 Financial_Fraud_Detection_Project
├── 📁 data
│   └── creditcard.csv
│   └── Fraud_Detection_result.csv
│   └── scaled_creditcard.csv
│   └── X_test.csv
│   └── X_train.csv
│   └── y_test.csv
│   └── y_train.csv
│   
├── 📁 notebooks
│   └── 01_data_exploration.ipynb
│   └── 02_data_preprocessing.ipynb
│   └── 03_feature_engineering.ipynb
│   └── 04_fraud_detection_models_selection.ipynb
│   └── 05_model_evaluation.ipynb
│   
├── 📁 dashboard
│   └── Fraud_Detection_Dashboard.pbix
│  
├── 📁 reports
│   └── fraud_detection_dashboard.png
│  
├── 📁 models
│   └── scaler_amount.pkl
│   └── scaler_time.pkl
│   
├── README.md
└── requirements.txt

---

## 🔎 Steps Performed

### 1. **Data Exploration**
- Loaded `creditcard.csv` with 284,807 rows and 31 columns.
- Verified no missing values and explored data structure.
- Visualized class distribution (highly imbalanced).
- Explored overall distributions and feature correlations.

### 2. **Data Preprocessing**
- Scaled `Time` and `Amount` using **StandardScaler**.
- Saved scalers using `joblib` for later use.
- Exported scaled data to `scaled_creditcard.csv`.

### 3. **Feature Engineering**
- Dropped `Time` column, defined features and target.
- Used **SMOTE** to balance the dataset (1:1 fraud vs legit).
- Split data into train and test sets (80-20).
- Exported processed data to CSV files.

### 4. **Model Selection**
- Built and evaluated models using:
  - Logistic Regression  
  - Random Forest  
  - XGBoost  
  - LightGBM
- Evaluated using Classification Report & AUC-ROC.

### 5. **Model Evaluation**
- Tuned models using **GridSearchCV**.
- Selected best model (Random Forest) based on AUC-ROC.
- Evaluated final model with classification report and confusion matrix.
- Inverse-transformed `Amount`, added `Time`, and saved results for Power BI.

### 6. **Dashboard with Power BI**
- Built an interactive fraud detection dashboard with:
  - Total & Fraud Transaction Cards
  - Fraud by Time of Day
  - Transaction Count by Risk Category
  - Transaction Amount Trend by Class
  - Filters for Class & Risk

![Fraud Detection Dashboard](<visual/fraud_detection_dashboard.png>)

---

## 📈 Business Insights

- 🚨 **50% fraud rate** after applying SMOTE (for modeling).
- 🔥 Fraud peaks during **morning hours (8 AM - 12 PM)**.
- 💵 Majority of frauds occur in **low-value transactions**—high volume but low amount.
- ⏱️ High-risk fraud hours: **9 AM to 7 PM** – need special monitoring.

---

## ✅ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Financial_Fraud_Detection_Project.git
   ```

2. Navigate to project directory:
   ```bash
   cd Financial_Fraud_Detection_Project
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run each notebook in sequence (`/notebooks`).

---

