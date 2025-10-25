import pandas as pd
import matplotlib.pyplot as plt
import os

print("📊 Starting frequency analysis...")

# Load cleaned dataset
data_path = "data/powerball_clean.csv"
if not os.path.exists(data_path):
    raise FileNotFoundError(f"❌ Dataset not found: {data_path}. Run clean_powerball_data.py first.")

df = pd.read_csv(data_path)

# Melt into one long list of numbers
main_numbers = df[["num_1", "num_2", "num_3", "num_4", "num_5"]].melt(value_name="number")["number"].astype(int)
powerball_numbers = df["powerball"].astype(int)

# Count frequency
main_counts = main_numbers.value_counts().sort_index()
power_counts = powerball_numbers.value_counts().sort_index()

# Create reports folder
os.makedirs("reports", exist_ok=True)

# Save frequency tables
main_counts.to_csv("reports/main_number_frequency.csv", header=["frequency"])
power_counts.to_csv("reports/powerball_number_frequency.csv", header=["frequency"])
print("✅ Frequency data saved to reports/")

# Plot main numbers
plt.figure(figsize=(14,6))
plt.bar(main_counts.index, main_counts.values)
plt.title("Main Number Frequency (Powerball)")
plt.xlabel("Number")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("reports/main_number_frequency.png")
plt.close()

# Plot Powerball numbers
plt.figure(figsize=(10,5))
plt.bar(power_counts.index, power_counts.values, color="red")
plt.title("Powerball Number Frequency")
plt.xlabel("Powerball")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("reports/powerball_number_frequency.png")
plt.close()

# Display top 10
print("🏆 Top 10 Main Numbers:")
print(main_counts.sort_values(ascending=False).head(10))
print("\n🔴 Top 5 Powerball Numbers:")
print(power_counts.sort_values(ascending=False).head(5))
