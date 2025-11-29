import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

#Load datasets
gdp = pd.read_csv("/Users/yaminkashim/DAT5501_lab/project/gdp.csv")
divorce = pd.read_csv("/Users/yaminkashim/DAT5501_lab/project/divorces-per-1000-people.csv")

#Filter for United Kingdom
gdp_uk = gdp[gdp["Entity"] == "United Kingdom"][["Year", "GDP per capita"]]
divorce_uk = divorce[divorce["Entity"] == "United Kingdom"][["Year", "Crude divorce rate"]]

# erge on Year
uk_data = pd.merge(gdp_uk, divorce_uk, on="Year", how="inner")

#Correlation Analysis
corr = uk_data["GDP per capita"].corr(uk_data["Crude divorce rate"])
print(f"Correlation between GDP per capita and divorce rate (UK): {corr:.3f}")

#Plot the Relationship
plt.figure(figsize=(10,6))
plt.scatter(uk_data["GDP per capita"], uk_data["Crude divorce rate"], label="Data Points")
plt.title("UK GDP per Capita vs Divorce Rate")
plt.xlabel("GDP per Capita (USD, Maddison Project)")
plt.ylabel("Divorces per 1000 People")

#Fit Linear Regression
X = uk_data["GDP per capita"].values.reshape(-1, 1)
y = uk_data["Crude divorce rate"].values
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)
plt.plot(uk_data["GDP per capita"], y_pred, label="Linear Fit", linewidth=2)

plt.legend()
plt.grid(True)
plt.show()

#Optional: Plot Trends Over Time
fig, ax1 = plt.subplots(figsize=(10,6))
ax1.plot(uk_data["Year"], uk_data["GDP per capita"], label="GDP per Capita", linewidth=2)
ax1.set_ylabel("GDP per Capita (USD)")
ax2 = ax1.twinx()
ax2.plot(uk_data["Year"], uk_data["Crude divorce rate"], color='red', label="Divorce Rate", linewidth=2)
ax2.set_ylabel("Divorces per 1000 People")
plt.title("UK GDP vs Divorce Rate Over Time")
fig.legend(loc="upper left", bbox_to_anchor=(0.1, 0.9))
plt.show()

from sklearn.preprocessing import PolynomialFeatures

poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)
model_poly = LinearRegression()
model_poly.fit(X_poly, y)
y_poly_pred = model_poly.predict(X_poly)

plt.scatter(uk_data["GDP per capita"], y, label="Data")
plt.plot(uk_data["GDP per capita"], y_poly_pred, color='red', label="Quadratic Fit")
plt.legend()
plt.title("Quadratic Fit: GDP vs Divorce Rate (UK)")
plt.show()