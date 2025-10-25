import kagglehub
import pandas as pd
import os

print("📥 Downloading Powerball dataset...")

# Download dataset
path = kagglehub.dataset_download("ulrikthygepedersen/lottery-powerball-winning-numbers")
print("✅ Dataset downloaded to:", path)

# Find CSV file in dataset
for file in os.listdir(path):
    if file.endswith(".csv"):
        file_path = os.path.join(path, file)
        break

print("📂 Found dataset file:", file_path)

# Load dataset
df = pd.read_csv(file_path)

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Detect whether dataset is already cleaned
if all(col in df.columns for col in ["num_1", "num_2", "num_3", "num_4", "num_5", "powerball"]):
    print("🧹 Dataset already cleaned — skipping number split.")
    df_clean = df.copy()
else:
    # Fallback for raw versions
    date_col = [c for c in df.columns if "draw" in c][0]
    num_col = [c for c in df.columns if "winning" in c][0]
    numbers = df[num_col].str.split(" ", expand=True)
    numbers.columns = [f"num_{i+1}" for i in range(numbers.shape[1]-1)] + ["powerball"]
    df_clean = pd.concat([df[date_col], numbers], axis=1)
    df_clean[date_col] = pd.to_datetime(df_clean[date_col])

# Sort and save
df_clean = df_clean.dropna().sort_values(by=df_clean.columns[0])
os.makedirs("data", exist_ok=True)
save_path = "data/powerball_clean.csv"
df_clean.to_csv(save_path, index=False)
print(f"✅ Cleaned dataset saved to: {save_path}")
