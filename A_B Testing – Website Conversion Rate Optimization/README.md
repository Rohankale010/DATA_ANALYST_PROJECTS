# A/B Testing – Website Conversion Rate Optimization

## 🚀 Project Objective
Assess whether a new landing page design increases the conversion rate compared to the existing page.

## 🧰 Tools & Technologies
- **Python:** pandas, Matplotlib, Seaborn, statsmodels
- **Power BI:** Interactive dashboard visualization

## 📁 Project Structure
```bash
A_B_Testing_Conversion_Rate_Optimization/
│
├── data/
│   └── ab_data.csv
│   └── ab_clean_data.csv
│
├── notebooks/
│   └── ab_testing_analysis.ipynb
│
├── scripts/
│   ├── data_cleaning.py
│   └── ab_testing_analysis.py
│
├── dashboard/
│   └── AB_Testing_Dashboard.pbix
│
├── visuals/
│   ├── AB_Testing_Dashboard.png
│   ├── Conversion Rate-Control vs Treatment.png
│   ├── Count-Converted vs Non - Converted by Group.png
│   ├── Daily Conversion Rate by Group.png
│   └── Distribution of Users in Control vs Treatment.png
│
├── README.md
└── requirements.txt
```

## 📝 Workflow

1. **Data Cleaning**  
   - Loaded `ab_data.csv`, filtered mismatched group-page pairs, and saved as `clean_ab_data.csv`.

2. **EDA & Visualization**  
   - Plotted overall and group-specific conversion rates, daily trends, and sample size proportions.

3. **Hypothesis Testing**  
   - **H₀:** Conversion rates are equal.  
   - **H₁:** Conversion rates differ.  
   - **Result:** z = −1.3116, p = 0.1897 → Fail to reject H₀.

4. **Power BI Dashboard**  
   - Built visuals: Conversion comparison, daily trends, sample size, key metrics, and interpretation.
   ![AB Testing Dashboard](<visuals/AB_Testing_Dashboard.png>)

## 🔍 Key Findings
- No significant difference in conversion rates (p = 0.1897).
- Recommend retaining the existing landing page or iterating further.
