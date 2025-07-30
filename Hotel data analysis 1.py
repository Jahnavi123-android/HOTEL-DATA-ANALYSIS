import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Full path to your CSV file
file_path = r'C:\Users\AK\OneDrive\Desktop\Data analysis\notes\ADVANCE PYTHON\Project 1\tips.csv'

# Load the CSV
df = pd.read_csv(file_path)

# Show the first few rows
print(df.head())

# Hotel Data Analysis Project
# Converted from Jupyter Notebook to Python script for VS Code


# Display first 5 rows
print("\nFirst 5 rows of the data:")
print(df.head())

# Display dataset info
print("\nDataset Info:")
print(df.info())



# Statistical summary
print("\nStatistical Summary:")
print(df.describe())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Analyzing 'day' column (instead of 'room_type')
print("\nDay Distribution:")
print(df['day'].value_counts())

# Plotting Day Distribution
plt.figure(figsize=(8,5))
sns.countplot(data=df, x='day', palette='Set2')
plt.title('Distribution of Days')
plt.xlabel('Day')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

# Average tip by day
avg_tip_per_day = df.groupby('day')['tip'].mean()
print("\nAverage Tip per Day:")
print(avg_tip_per_day)

# Plotting Average Tip per Day
avg_tip_per_day.plot(kind='bar', color='skyblue')
plt.title('Average Tip per Day')
plt.xlabel('Day')
plt.ylabel('Average Tip')
plt.tight_layout()
plt.show()

# Relationship between total bill and tip
plt.figure(figsize=(8,5))
sns.scatterplot(data=df, x='total_bill', y='tip')
plt.title('Tip vs Total Bill')
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.tight_layout()
plt.show()

# Correlation heatmap
plt.figure(figsize=(10,7))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.show()

print("\nTips Data Analysis Completed Successfully!")
