import pandas as pd

df = pd.read_csv('sales_data.csv')
total = df['price'].sum()
avg = df['price'].mean()
print(f'Общий доход: {total}')
print(f'Средний чек: {avg:.0f}')