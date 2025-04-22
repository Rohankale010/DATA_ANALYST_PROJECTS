# scripts/automate_refresh_publish.py

import os
import subprocess
import time

# Path to your Power BI Desktop .pbix file
pbix_file_path = os.path.abspath(r"D:\Projects\DATA_ANALYST_PROJECTS\Powerbi_automated_reporting_system\dashboard\automated_dashboard.pbix"
)

# Optional: Path to Power BI Desktop executable (may vary depending on install location)
# Example for standard installation:
powerbi_path = r"D:\Power BI (exe)\bin\PBIDesktop.exe"

# Launch Power BI with the .pbix file
print("Opening Power BI Desktop with the report...")
subprocess.Popen([powerbi_path, pbix_file_path])

# Wait for user-defined time to allow refresh to complete
# NOTE: Make sure the file is set to auto-refresh on open if needed
refresh_wait_minutes = 5
print(f"Waiting {refresh_wait_minutes} minutes for data refresh to complete...")
time.sleep(refresh_wait_minutes * 60)

# Optional: Notify that the task is complete
print("Task completed. Please manually verify or publish from Power BI Desktop.")

# Optional: You can add automation to close Power BI or use tools like AutoHotkey
