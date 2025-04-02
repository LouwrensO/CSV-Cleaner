import pandas as pd

# Replace this with the path to your CSV file
file_path = r"C:\Users\user\Desktop\Coding\CSVCleaner\messy_data.csv"

# Load the CSV file
df = pd.read_csv(file_path)

# Drop completely empty rows
df.dropna(how="all", inplace=True)

# Drop duplicate rows
df.drop_duplicates(inplace=True)

# Save the cleaned file
cleaned_path = "C:/Users/user/Desktop/cleaned_data.csv"
df.to_csv(cleaned_path, index=False)

print("✅ CSV cleaned and saved to:", cleaned_path)
