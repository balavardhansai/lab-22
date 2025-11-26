import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Salary': [50000.0, 60000.5, 70000.8],
    'Is_Manager': [True, False, True]
}
df = pd.DataFrame(data)
print(df.dtypes)
print(df.info())
