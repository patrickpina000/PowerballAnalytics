import subprocess
import os

print("🚀 Starting Powerball Analytics Pipeline...\n")

# Step 1: Download & clean
print("🔹 Step 1: Downloading and cleaning data...")
subprocess.run(["python3", "scripts/clean_powerball_data.py"], check=True)

# Step 2: Frequency analysis
print("\n🔹 Step 2: Performing frequency analysis...")
subprocess.run(["python3", "scripts/frequency_analysis.py"], check=True)

# Step 3: EMV calculation
print("\n🔹 Step 3: Calculating EMV ranking...")
subprocess.run(["python3", "scripts/emv_calculator.py"], check=True)

print("\n✅ All steps completed successfully!")
print("📂 Check the 'reports/' folder for results.")
#!/usr/bin/env python3
import subprocess
import os

# Activate virtual environment if not already
print("🚀 Starting Powerball Analytics Pipeline...")

# Ensure folders exist
os.makedirs("scripts", exist_ok=True)
os.makedirs("data", exist_ok=True)
os.makedirs("reports", exist_ok=True)

# Step 1: Clean/download data
print("\n🔹 Step 1: Downloading and cleaning data...")
subprocess.run(["python3", "scripts/clean_powerball_data.py"], check=True)

# Step 2: Trend and EMV analysis
print("\n🔹 Step 2: Running Trend and EMV Analysis...")
subprocess.run(["python3", "scripts/trend_analysis.py"], check=True)

# Step 3: Generate PDF report
print("\n🔹 Step 3: Generating PDF report...")
subprocess.run(["python3", "scripts/generate_report.py"], check=True)

print("\n✅ Powerball Analytics Pipeline Complete! Reports are in 'reports/' folder.")
