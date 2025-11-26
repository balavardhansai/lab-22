import pandas as pd
import numpy as np
data = {
    'Name': ['bala', 'vardhan', 'sai', 'hi'],
    'Age': [25, np.nan, 35, 40],
    'Salary': [50000, 60000, np.nan, 80000]
}
df = pd.DataFrame(data)
print("Before filling missing values:")
print(df)
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)
print("\nAfter filling missing values with mean:")
print(df)