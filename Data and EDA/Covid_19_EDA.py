import pandas as pd
from fontTools.afmLib import kernRE

# Load the datasets
Covid_19_df = pd.read_csv("Covid_19.csv")

# Shape of datasets
print("Shape of Covid_19 dataset: ", Covid_19_df.shape)

# Display the first few rows
print("\nCovid_19 Dataset:")
print(Covid_19_df.head())

# Info for dataset
print("\nCovid_19 Dataset Info:")
print(Covid_19_df.info())

# 1. Display column names and first few rows
print("Columns in Covid_19 dataset:", Covid_19_df.columns)
print("\nFirst 5 rows:")
print(Covid_19_df.head())

# 2. Check for missing values
print("\nMissing values:\n", Covid_19_df.isnull().sum())

# 3. Check for duplicates
duplicates = Covid_19_df.duplicated().sum()
print(f"\nDuplicate rows: {duplicates}")
if duplicates > 0:
    Covid_19_df.drop_duplicates(inplace=True)

# 4. Data types and basic info
print("\nDataset info:")
print(Covid_19_df.info())

# 5. Summary statistics
print("\nSummary statistics:")
print(Covid_19_df.describe(include='all'))

# 6. Unique values in object (categorical) columns
for col in Covid_19_df.columns:
    if Covid_19_df[col].dtype == 'object':
        print(f"\nUnique values in '{col}': {Covid_19_df[col].unique()}")

# 7. Encoding target column if applicable
# (Assuming there's a target column like 'Severity' or 'Covid_Status', update accordingly)
# Example (adjust this based on actual column name):
# Covid_19_df['Severity'] = Covid_19_df['Severity'].map({'Mild': 0, 'Moderate': 1, 'Severe': 2})

# 8. Final cleaned data overview
print("\nCleaned Covid_19 dataset shape:", Covid_19_df.shape)
print(Covid_19_df.head())

# Save cleaned datasets
Covid_19_df.to_csv("Cleaned_Covid_19.csv", index=False)
print("cleaned datasets have been saved successfully.")




