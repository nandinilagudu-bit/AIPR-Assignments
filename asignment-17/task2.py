"""Task 2 — Financial Data Preprocessing

Produces `financial_data_preprocessed.csv` from `financial_data.csv`.

Steps:
- Parse date index and sort
- Handle missing values in `closing_price` and `volume` (forward-fill then median/backfill)
- Create lag return features: `ret_1d` and `ret_7d` (percent change)
- Log-scale `volume` into `volume_log` using `log1p`
- Detect outliers in `closing_price` using IQR and flag `is_outlier`
- Save final CSV

Run:
    python task2.py

"""

import pandas as pd
import numpy as np
import os

INPUT = 'financial_data.csv'
OUTPUT = 'financial_data_preprocessed.csv'

if not os.path.exists(INPUT):
    raise FileNotFoundError(f"Input file '{INPUT}' not found in working directory.")

print('Loading', INPUT)
df = pd.read_csv(INPUT)

print('Initial shape:', df.shape)
print(df.head(5))

# Parse date and sort
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values('date').reset_index(drop=True)

# Ensure numeric columns
for col in ['closing_price', 'volume']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Handle missing values
# For time-series, prefer forward-fill then backward-fill; finally fill any remaining with median
print('\nHandling missing values: forward-fill then backfill, then median fallbacks')
df['closing_price'] = df['closing_price'].ffill().bfill()
if df['closing_price'].isnull().any():
    median_close = df['closing_price'].median()
    df['closing_price'] = df['closing_price'].fillna(median_close)

# For volume, forward-fill/backfill and then fill with median
df['volume'] = df['volume'].ffill().bfill()
if df['volume'].isnull().any():
    median_vol = df['volume'].median()
    df['volume'] = df['volume'].fillna(median_vol)

print('Missing values after imputation:')
print(df[['closing_price', 'volume']].isnull().sum())

# Create lag features: 1-day and 7-day returns (percent change)
print('\nCreating lag return features: ret_1d, ret_7d')
df['ret_1d'] = df['closing_price'].pct_change(periods=1)
df['ret_7d'] = df['closing_price'].pct_change(periods=7)

# Normalize volume using log-scaling
print('\nLog-scaling volume into volume_log (using log1p)')
df['volume_log'] = np.log1p(df['volume'])

# Detect outliers in closing_price using IQR
print('\nDetecting outliers in closing_price using IQR method')
Q1 = df['closing_price'].quantile(0.25)
Q3 = df['closing_price'].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df['is_outlier'] = ((df['closing_price'] < lower) | (df['closing_price'] > upper))
num_outliers = df['is_outlier'].sum()
print(f'Outliers detected: {num_outliers}')

# Optional: cap outliers (winsorize) — commented out; we keep a flag for modeling
# df['closing_price_capped'] = df['closing_price'].clip(lower=lower, upper=upper)

# Final ordering and save
cols = ['date', 'closing_price', 'volume', 'volume_log', 'ret_1d', 'ret_7d', 'is_outlier']
final = df[cols]
final.to_csv(OUTPUT, index=False)

print('\nSaved preprocessed data to', OUTPUT)
print('Final shape:', final.shape)
print(final.head(10))
