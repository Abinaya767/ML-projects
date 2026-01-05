# ===============================
# Ice Cream Profits vs Temperature (Two Graphs with Explanations)
# ===============================

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load dataset
file_path = r"C:\Users\Admin\OneDrive\Desktop\ML WORKS\Ice Cream Sales - temperatures.csv"
df = pd.read_csv(file_path)

# Prepare data
X = df[['Temperature']]
y = df['Ice Cream Profits']

# Fit Linear Regression model
model = LinearRegression()
model.fit(X, y)

# ------------------------------
# Graph 1: Scatter plot of actual data
# ------------------------------
plt.figure(figsize=(10,6))
plt.scatter(df['Temperature'], df['Ice Cream Profits'], color='orange')
plt.xlabel('Temperature (°C)', fontsize=12)
plt.ylabel('Ice Cream Profits ($)', fontsize=12)
plt.title('Graph 1: Temperature vs Ice Cream Profits', fontsize=14)
plt.grid(True)
plt.show()

# Explanation of Graph 1
print("Graph 1 Explanation:")
print("- Each orange dot represents the ice cream profit at a specific temperature.")
print("- We can see a general upward trend: as temperature increases, profits tend to increase.")
print("- This graph shows the raw data without any model applied.\n")

# ------------------------------
# Graph 2: Scatter plot + Regression line
# ------------------------------
plt.figure(figsize=(10,6))
plt.scatter(df['Temperature'], df['Ice Cream Profits'], color='orange', label='Actual Data')

# Regression line
plt.plot(df['Temperature'], model.predict(X), color='blue', linewidth=2, label='Regression Line')

# Example prediction for a specific temperature (no warning)
temp_example = 85
temp_df = pd.DataFrame({'Temperature':[temp_example]})
predicted_profit = model.predict(temp_df)
plt.scatter(temp_example, predicted_profit, color='red', s=100,
            label=f'Predicted at {temp_example}°C: ${predicted_profit[0]:.2f}')

# Labels and styling
plt.xlabel('Temperature (°C)', fontsize=12)
plt.ylabel('Ice Cream Profits ($)', fontsize=12)
plt.title('Graph 2: Temperature vs Ice Cream Profits with Regression Line', fontsize=14)
plt.legend()
plt.grid(True)
plt.show()

# Explanation of Graph 2
print("Graph 2 Explanation:")
print("- Orange dots: actual ice cream profits for each temperature.")
print("- Blue line: regression line fitted to the data (shows trend).")
print("- Red dot: predicted profit for 85°C using the linear regression model.")
print("- This graph helps visualize how profits increase with temperature and allows us to predict profits for any temperature.\n")


