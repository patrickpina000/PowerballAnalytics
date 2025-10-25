import pandas as pd

# Load data
df = pd.read_csv("data/powerball_clean.csv")

# Combine all number columns into one list
nums = df[['num_1', 'num_2', 'num_3', 'num_4', 'num_5']].values.flatten()

# Calculate frequency of each number
freq = pd.Series(nums).value_counts(normalize=True)

# Expected value (simplified statistical weight)
emv = (freq * 100).round(2).sort_values(ascending=False)

# Save results
emv.to_csv("reports/emv_ranking.csv")

print("✅ EMV ranking generated! Check reports/emv_ranking.csv")
