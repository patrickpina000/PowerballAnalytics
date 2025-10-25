import pandas as pd
import matplotlib.pyplot as plt
import os

# Create reports folder if it doesn't exist
os.makedirs("reports", exist_ok=True)

# Load cleaned Powerball CSV
df = pd.read_csv(
    "/Users/patrickpina/.cache/kagglehub/datasets/ulrikthygepedersen/lottery-powerball-winning-numbers/versions/1/cleaned_powerball.csv"
)

# Strip whitespace from columns
df.columns = [c.strip() for c in df.columns]

# Rename 'draw date' to 'draw_date' if needed
if "draw date" in df.columns:
    df = df.rename(columns={"draw date": "draw_date"})

# Convert draw_date to datetime and sort
df["draw_date"] = pd.to_datetime(df["draw_date"])
df = df.sort_values("draw_date")

# Melt numbers into long format for analysis
numbers = df.melt(
    id_vars="draw_date",
    value_vars=["num_1", "num_2", "num_3", "num_4", "num_5"],
    value_name="number"
)

# Rolling frequency trends
window_size = 50

def rolling_count(group):
    group = group.copy()
    group = group.set_index("draw_date")
    group["frequency"] = group["number"].rolling(window=window_size).count()
    return group.reset_index()

trends = numbers.groupby("number", group_keys=False, as_index=False).apply(rolling_count)

# Latest frequency per number
latest_freq = trends.groupby("number", as_index=False).last().sort_values(by="frequency", ascending=False)

# Top 10 hot numbers
top_numbers = latest_freq.head(10)
top_numbers.to_csv("reports/top_hot_numbers.csv", index=False)

# Top 10 cold numbers
cold_numbers = latest_freq.tail(10)
cold_numbers.to_csv("reports/top_cold_numbers.csv", index=False)

# EMV calculation (simplified)
ticket_cost = 2
avg_prize = 50  # simplified placeholder
emv = (avg_prize * (1/69)) - ticket_cost
print(f"🎯 Estimated EMV per ticket: ${emv:.2f}")

# Plot trends
plt.figure(figsize=(12,6))
for num in trends["number"].unique():
    subset = trends[trends["number"] == num]
    plt.plot(subset["draw_date"], subset["frequency"], alpha=0.1, color="blue")
plt.title("Rolling Frequency Trends (window=50 draws)")
plt.xlabel("Draw Date")
plt.ylabel("Frequency")
plt.savefig("reports/number_trends.png", dpi=300)
plt.close()

print("📈 Running Trend and EMV Analysis... Done!")
print("🏆 Top 10 Hot Numbers:\n", top_numbers)
print("🥶 Top 10 Cold Numbers:\n", cold_numbers)
print("✅ Reports saved to 'reports/' folder")
