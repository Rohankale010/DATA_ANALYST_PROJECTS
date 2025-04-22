
---

```markdown
# 📊 Power BI Automated Reporting System

This project demonstrates a simple automation system for opening Power BI dashboards using Python. It is particularly useful for analysts and teams who want to streamline the daily or scheduled review of business reports without manually opening Power BI and loading reports every time.

---

## 🚀 Project Overview

- **Goal**: Automate the opening and loading of Power BI reports using a Python script.
- **Tools Used**:
  - Power BI Desktop
  - Python (Automation)
- **Automation Functionality**:
  - Opens a `.pbix` file in Power BI Desktop.
  - Waits for a fixed time to allow manual refresh or verification.
  - Can be scheduled via Task Scheduler for daily execution.

---

## 📂 Folder Structure

```bash
powerbi_automated_reporting_system/
│
├── 📁 data/
│   └── sample_report_data.csv   
│
├── 📁 scripts/ 
│   └──  automate_refresh_publish.py       # Python script for automation
│
├── 📁 dashboard/
│   └── automated_dashboard.pbix           # Power BI Dashboard File
│
├── README.md                              # Project documentation
├── requirements.txt                       # Python dependencies
```

---

## ⚙️ Setup Instructions

1. **Install Power BI Desktop**  
   Download and install from: 
   [Power BI Desktop Download](https://powerbi.microsoft.com/desktop/)          # Standard Download not from store

2. **Install Python Libraries**

   ```bash
   pip install -r requirements.txt
   ```

3. **Update Script Paths**

   In `automate_refresh_publish.py`, update:

   ```python
   powerbi_path = r"C:\Path\To\PBIDesktop.exe"
   pbix_file_path = r"D:\Path\To\automated_dashboard.pbix"
   ```

4. **Run Script**

   ```bash
   python automate_refresh_publish.py
   ```

5. **Optional**: Add script to **Windows Task Scheduler** for daily or weekly automation.

---

## 📌 Notes

- This automation script **does not refresh or publish the report** to Power BI Service.
- For full automation including **auto-refresh and publish**, integration with **Power BI REST API** and a **Data Gateway** is recommended.

---

## ✅ Outcome

- One-click execution to load Power BI dashboards.
- Time-saving for daily review/reporting workflows.
- Reusable template for multiple dashboards.

---


