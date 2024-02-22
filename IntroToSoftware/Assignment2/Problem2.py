import pandas as pd

df = pd.read_csv('payroll.txt', sep = ' ', header = None)
df.columns = ['Name', 'Hourly Wage', 'Hours Worked']
df['Wages Paid'] = df['Hourly Wage'] * df['Hours Worked']
print(df)
