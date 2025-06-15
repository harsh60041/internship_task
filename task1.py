
import pandas as pd
import numpy as np
import seaborn as sns

# Load the dataset
df = sns.load_dataset('tips')

# Create some missing values
df.loc[0, 'total_bill'] = np.nan

# Identify and handle missing values
print("Missing values count:")
print(df.isnull().sum())

# Replace missing values with mean for numerical columns and mode for categorical columns
numerical_cols = ['total_bill', 'tip', 'size']
categorical_cols = ['sex', 'smoker', 'day', 'time']

for col in numerical_cols:
    df[col] = df[col].fillna(df[col].mean())

for col in categorical_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

# Remove duplicate rows
df = df.drop_duplicates()

# Standardize text values
df['sex'] = df['sex'].str.lower()
df['smoker'] = df['smoker'].str.lower()
df['day'] = df['day'].str.lower()
df['time'] = df['time'].str.lower()

# Rename column headers to be clean and uniform
df.columns = [col.lower().replace(' ', '_') for col in df.columns]

# Check and fix data types
print("Data types:")
print(df.dtypes)

# Save the cleaned dataset
df.to_csv('cleaned_tips.csv', index=False)
print("Cleaned dataset saved successfully.")

