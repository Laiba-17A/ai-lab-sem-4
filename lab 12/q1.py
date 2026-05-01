import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

print("Loading data...")
df = pd.read_csv('lab 12/Iris.csv')
print(f"Shape: {df.shape}")

print("\nFirst 5 rows:")
print(df.head())

print("\nInfo:")
print(df.info())

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())

if 'Id' in df.columns:
    df.drop(columns=['Id'], inplace=True)

dup_count = df.duplicated().sum()
print("Duplicates:", dup_count)

if dup_count > 0:
    df = df.drop_duplicates()
    print("Duplicates removed.")

print("Shape after cleaning:", df.shape)

print("\nTarget distribution:")
print(df['Species'].value_counts(normalize=True))

plt.figure(figsize=(6,4))
sns.countplot(x='Species', data=df)
plt.title("Species Distribution")
plt.show()

print("\nStatistical summary:")
print(df.describe())

num_cols = df.select_dtypes(include=np.number).columns

for col in num_cols:
    plt.figure(figsize=(6,4))
    sns.histplot(df[col], kde=True)
    plt.title(f"Distribution of {col}")
    plt.show()

for col in num_cols:
    plt.figure(figsize=(6,4))
    sns.boxplot(x='Species', y=col, data=df)
    plt.title(f"{col} vs Species")
    plt.show()

plt.figure(figsize=(6,5))
sns.heatmap(df[num_cols].corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()

sns.pairplot(df, hue='Species')
plt.show()

print("\nKey Observations:")
print("- Dataset is clean (no missing values).")
print("- Classes are balanced.")
print("- PetalLength & PetalWidth strongly separate species.")
print("- Setosa is linearly separable from others.")
print("- Some overlap between Versicolor and Virginica.")