import pandas as pd

# Load CSV
df = pd.read_csv("data/powerball.csv")

# Standardize column names
df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

# Drop duplicates or NaN
df = df.dropna().drop_duplicates()

# Convert date column to datetime
df['draw_date'] = pd.to_datetime(df['draw_date'])

# Sort by date
df = df.sort_values(by='draw_date', ascending=True)

df.to_csv("data/powerball_clean.csv", index=False)
print("✅ Data cleaned and saved!")
