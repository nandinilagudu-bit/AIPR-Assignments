"""Task 3 — IoT Sensor Data Preparation

Produces `iot_sensor_prepared.csv` from `iot_sensor.csv`.

Steps implemented:
- Parse timestamp and sort
- Forward-fill missing values per sensor
- Remove sensor drift using rolling mean (window=6)
- Standard-scale (z-score) the detrended temperature and humidity per sensor
- Encode `sensor_id` as integer labels and one-hot columns
- Save prepared CSV

Run:
    python task3.py
"""

import os
import pandas as pd
import numpy as np

INPUT = 'iot_sensor.csv'
OUTPUT = 'iot_sensor_prepared.csv'

if not os.path.exists(INPUT):
    raise FileNotFoundError(f"Input file '{INPUT}' not found in working directory.")

print('Loading', INPUT)
df = pd.read_csv(INPUT)
print('Initial shape:', df.shape)

# Parse timestamp and sort
df['timestamp'] = pd.to_datetime(df['timestamp'])
df = df.sort_values('timestamp').reset_index(drop=True)

# Ensure numeric
for col in ['temperature', 'humidity']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Forward fill missing values per sensor
print('\nForward-filling missing values per sensor (groupby sensor_id)')
# Keep raw copies
df['temperature_raw'] = df['temperature']
df['humidity_raw'] = df['humidity']

# Forward fill within each sensor group
df[['temperature', 'humidity']] = df.groupby('sensor_id')[['temperature', 'humidity']].ffill()

# If any leading NaNs remain (no prior value), fill them with sensor median as a small fallback
for col in ['temperature', 'humidity']:
    mask_null = df[col].isnull()
    if mask_null.any():
        medians = df.groupby('sensor_id')[col].transform('median')
        df.loc[mask_null, col] = medians[mask_null]

print('Missing values after imputation:')
print(df[['temperature', 'humidity']].isnull().sum())

# Remove sensor drift using rolling mean (window in hours)
# We choose window=6 (6 readings) to capture short-term drift while preserving anomalies
ROLL_WINDOW = 6
print(f"\nRemoving sensor drift using rolling mean (window={ROLL_WINDOW})")

def remove_drift(group, col, window=ROLL_WINDOW):
    roll = group[col].rolling(window=window, min_periods=1).mean()
    detrended = group[col] - roll
    return detrended, roll

# Compute rolling mean and detrended signals per sensor
temp_detrended_list = []
hum_detrended_list = []
roll_temp_list = []
roll_hum_list = []

for sensor, g in df.groupby('sensor_id'):
    det_temp, roll_temp = remove_drift(g, 'temperature')
    det_hum, roll_hum = remove_drift(g, 'humidity')
    temp_detrended_list.append(det_temp)
    hum_detrended_list.append(det_hum)
    roll_temp_list.append(roll_temp)
    roll_hum_list.append(roll_hum)

# Reconstruct columns in original index order
df['temperature_roll_mean'] = pd.concat(roll_temp_list).sort_index()
df['humidity_roll_mean'] = pd.concat(roll_hum_list).sort_index()
df['temperature_detrended'] = pd.concat(temp_detrended_list).sort_index()
df['humidity_detrended'] = pd.concat(hum_detrended_list).sort_index()

# Standard-scale (z-score) the detrended readings per sensor
print('\nStandard-scaling (z-score) detrended readings per sensor')
df['temperature_z'] = np.nan
df['humidity_z'] = np.nan

for sensor, g in df.groupby('sensor_id'):
    t_mean = g['temperature_detrended'].mean()
    t_std = g['temperature_detrended'].std(ddof=0)
    h_mean = g['humidity_detrended'].mean()
    h_std = g['humidity_detrended'].std(ddof=0)

    if t_std == 0 or np.isnan(t_std):
        df.loc[g.index, 'temperature_z'] = 0.0
    else:
        df.loc[g.index, 'temperature_z'] = (g['temperature_detrended'] - t_mean) / t_std

    if h_std == 0 or np.isnan(h_std):
        df.loc[g.index, 'humidity_z'] = 0.0
    else:
        df.loc[g.index, 'humidity_z'] = (g['humidity_detrended'] - h_mean) / h_std

# Encode categorical sensor IDs
print('\nEncoding sensor IDs: label encoding and one-hot')
df['sensor_label'] = pd.factorize(df['sensor_id'])[0]
one_hot = pd.get_dummies(df['sensor_id'], prefix='sensor')
df = pd.concat([df, one_hot], axis=1)

# Reorder and save
cols = [
    'timestamp', 'sensor_id', 'sensor_label',
    'temperature_raw', 'humidity_raw',
    'temperature', 'humidity',
    'temperature_roll_mean', 'humidity_roll_mean',
    'temperature_detrended', 'humidity_detrended',
    'temperature_z', 'humidity_z'
]
# add one-hot cols
cols += list(one_hot.columns)

prepared = df[cols]
prepared.to_csv(OUTPUT, index=False)

print('\nSaved prepared data to', OUTPUT)
print('Final shape:', prepared.shape)
print(prepared.head(20))
