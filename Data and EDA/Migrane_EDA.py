import pandas as pd
from fontTools.afmLib import kernRE

# Load the datasets
Migraine_df = pd.read_csv("Migraine.csv")

# Shape of datasets
print("Shape of Migraine dataset: ", Migraine_df.shape)

# Display the first few rows
print("\nMigraine Dataset:")
print(Migraine_df.head())

# Info for dataset
print("\nMigraine Dataset Info:")
print(Migraine_df.info())

## EDA of migrane dataset
# 1. Display column names and first few rows
print("Columns in Migraine dataset:", Migraine_df.columns)
print("\nFirst 5 rows:")
print(Migraine_df.head())

# 2. Check for missing values
print("\nMissing values:\n", Migraine_df.isnull().sum())

# 3. Check for duplicates
duplicates = Migraine_df.duplicated().sum()
print(f"\nDuplicate rows: {duplicates}")
if duplicates > 0:
    Migraine_df.drop_duplicates(inplace=True)

# 4. Data types and basic info
print("\nDataset info:")
print(Migraine_df.info())

# 5. Summary statistics
print("\nSummary statistics:")
print(Migraine_df.describe(include='all'))

# 6. Unique values in object (categorical) columns
for col in Migraine_df.columns:
    if Migraine_df[col].dtype == 'object':
        print(f"\nUnique values in '{col}': {Migraine_df[col].unique()}")


# 7. Encode target column if applicable
# Let's assume the target column is 'Migraine' or something similar
# You may update based on the exact column
if 'Migraine' in Migraine_df.columns:
    Migraine_df['Migraine'] = Migraine_df['Migraine'].map({'Yes': 1, 'No': 0})

# 8. Final cleaned data overview
print("\nCleaned Migraine dataset shape:", Migraine_df.shape)
print(Migraine_df.head())

# Save cleaned datasets
Migraine_df.to_csv("Cleaned_Migraine.csv", index=False)
print(" cleaned datasets have been saved successfully.")




