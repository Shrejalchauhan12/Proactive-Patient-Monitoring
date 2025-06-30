
import pandas as pd

# Load the datasets
Diabetes_df = pd.read_csv("Data and EDA/diabetes.csv")

# Shape of datasets
print("Shape of Diabetes dataset: ", Diabetes_df.shape)

# Display the first few rows
print("\nDiabetes Dataset:")
print(Diabetes_df.head())

# Info for dataset
print("\nDiabetes Dataset Info:")
print(Diabetes_df.info())

## Diabetes Dataset EDA

# 1. Display column names and first few rows
print("Columns in Diabetes dataset:", Diabetes_df.columns)
print("\nFirst 5 rows:")
print(Diabetes_df.head())

# 2. Check for missing values
print("\nMissing values:\n", Diabetes_df.isnull().sum())

# 3. Check for duplicates
duplicates = Diabetes_df.duplicated().sum()
print(f"\nDuplicate rows: {duplicates}")
if duplicates > 0:
    Diabetes_df.drop_duplicates(inplace=True)

# 4. Data types and basic info
print("\nDataset info:")
print(Diabetes_df.info())

# 5. Summary statistics
print("\nSummary statistics:")
print(Diabetes_df.describe())

# 6. Unique values in object (categorical) columns, if any
for col in Diabetes_df.columns:
    if Diabetes_df[col].dtype == 'object':
        print(f"\nUnique values in '{col}': {Diabetes_df[col].unique()}")

# 7. Encoding target column (assumption: 'Outcome' column)
# 1 = diabetic, 0 = non-diabetic (already encoded in many diabetes datasets)
if 'Outcome' in Diabetes_df.columns:
    Diabetes_df['Outcome'] = Diabetes_df['Outcome'].astype(int)

# 8. Final cleaned data overview
print("\nCleaned Diabetes dataset shape:", Diabetes_df.shape)
print(Diabetes_df.head())

# Save cleaned datasets
Diabetes_df.to_csv("Cleaned_Diabetes.csv", index=False)
print(" cleaned datasets have been saved successfully.")
