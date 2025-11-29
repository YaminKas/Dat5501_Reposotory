#!/usr/bin/env python3
"""
Multilinear Regression + Actual vs Predicted Graph
Predict Divorce Rate using GDP, Years of Schooling, and Working Hours
"""

import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#File path
path_divorce = "/Users/yaminkashim/DAT5501_lab/project/divorces-per-1000-people.csv"
path_gdp = "/Users/yaminkashim/DAT5501_lab/project/gdp.csv"
path_school = "/Users/yaminkashim/DAT5501_lab/project/years-of-schooling.csv"
path_hours = "/Users/yaminkashim/DAT5501_lab/project/annual-working-hours-per-worker.csv"

#Read CSVs
divorce = pd.read_csv(path_divorce)
gdp = pd.read_csv(path_gdp)
school = pd.read_csv(path_school)
hours = pd.read_csv(path_hours)

#Filter for United Kingdom
country = "United Kingdom"
divorce = divorce[divorce["Entity"] == country]
gdp = gdp[gdp["Entity"] == country]
school = school[school["Entity"] == country]
hours = hours[hours["Entity"] == country]

#Select relevant columns
divorce = divorce[["Year", "Crude divorce rate"]]
gdp = gdp[["Year", "GDP per capita"]]
school = school[["Year", "Average years of schooling among women", "Average years of schooling among men"]]
hours = hours[["Year", "Working hours per worker"]]

#Merge all datasets on Year
df = divorce.merge(gdp, on="Year", how="inner")
df = df.merge(school, on="Year", how="inner")
df = df.merge(hours, on="Year", how="inner")

#Prepare predictors and target
X = df[["GDP per capita",
        "Average years of schooling among women",
        "Average years of schooling among men",
        "Working hours per worker"]]
y = df["Crude divorce rate"]

#Fit multilinear regression
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

#Print results
print("\n=== Multilinear Regression Results ===\n")
print("Intercept:", model.intercept_)
print("Coefficients:")
for name, coef in zip(X.columns, model.coef_):
    print(f"  {name}: {coef:.6f}")
print("\nR-squared:", model.score(X, y))

#Plot Actual vs Predicted Divorce Rate
plt.figure(figsize=(8,6))
plt.scatter(y_pred, y, color='blue', edgecolor='k')
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--', linewidth=2)  # 45° reference line
plt.xlabel("Predicted Divorce Rate")
plt.ylabel("Actual Divorce Rate")
plt.title("Actual vs Predicted Divorce Rate (Multilinear Regression)")
plt.grid(True)
plt.tight_layout()
plt.show()

#Save merged dataset for reference
out_path = "/Users/yaminkashim/DAT5501_lab/project/merged_divorce_dataset.csv"
df.to_csv(out_path, index=False)
print(f"\nMerged dataset saved as: {out_path}")