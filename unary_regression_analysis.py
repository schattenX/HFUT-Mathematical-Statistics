import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
import os

# Load the datasets
co2_data_path = 'data/co2_data.csv'
temperature_data_path = 'data/land_ocean_temperature_index.csv'

# Read CO2 data and temperature anomaly data
co2_data = pd.read_csv(co2_data_path)
temperature_data = pd.read_csv(temperature_data_path)

# Step 1: Process CO2 data
# Calculate the yearly average CO2 levels for each year (group by 'Year')
co2_data['Year'] = co2_data['Year'].astype(int)
co2_yearly_avg = co2_data.groupby('Year')['Monthly_Average'].mean().reset_index()

# Step 2: Filter for the last 20 years (1970-2023)
co2_recent = co2_yearly_avg[(co2_yearly_avg['Year'] >= 1970) & (co2_yearly_avg['Year'] <= 2023)]
temperature_recent = temperature_data[(temperature_data['Year'] >= 1970) & (temperature_data['Year'] <= 2023)]

# Merge the CO2 and temperature data on 'Year'
data = pd.merge(co2_recent, temperature_recent, on='Year')

# Export the processed data to CSV files
co2_recent.to_csv('data/co2_data_1970to2023.csv', index=False)
temperature_recent.to_csv('data/temperature_data_1970to2023.csv', index=False)
data.to_csv('data/temperature_co2_data_1970to2023.csv', index=False)

# Step 3: Perform linear regression analysis
# CO2 (independent variable) and temperature anomaly (dependent variable)
X = data[['Monthly_Average']].values  # CO2 levels
y = data['No_Smoothing'].values       # Temperature anomalies

# Initialize and fit the model
model = LinearRegression()
model.fit(X, y)

# Get the regression line parameters
slope = model.coef_[0]
intercept = model.intercept_

# Predicted y values based on the model
y_pred = model.predict(X)

# Step 4: Plot the results
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, y_pred, color='red', label=f'Regression Line (y = {slope:.4f}x + {intercept:.4f})')
plt.xlabel('CO2 Concentration (ppm)')
plt.ylabel('Temperature Anomaly (°C)')
plt.title('Linear Regression of CO2 Concentration vs. Global Temperature Anomaly (1970-2023)')
plt.legend()
plt.grid(True)

# Save the figure
save_dir = 'plots/'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)
plt.savefig(save_dir + 'linear_regression.png')
# plt.savefig(save_dir + 'temperature_co2_scatter.png')

plt.show()
