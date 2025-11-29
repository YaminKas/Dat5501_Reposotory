#!/usr/bin/env python3
"""
Divorce Rate vs Fertility Rate Regression
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#File path
path_data = "/Users/yaminkashim/DAT5501_lab/project/children-born-per-woman.csv"

#Read CSV
df = pd.read_csv(path_data)

#Strip whitespace from column names
df.columns = df.columns.str.strip()
print("Columns after stripping:", df.columns)

#Prepare predictor and target
X = df[["Fertility rate"]]  # predictor
y = df["Crude divorce rate"]  # target

#it linear regression
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

#Print regression results
print("\n=== Fertility Rate vs Divorce Rate Regression ===\n")
print("Intercept:", model.intercept_)
print("Coefficient (Fertility rate):", model.coef_[0])
print("R-squared:", model.score(X, y))

#Plot Actual vs Predicted Divorce Rate
plt.figure(figsize=(8,6))
plt.scatter(df["Fertility rate"], df["Crude divorce rate"], color='blue', edgecolor='k', label="Actual")
plt.plot(df["Fertility rate"], y_pred, color='red', linewidth=2, label="Predicted")
plt.xlabel("Fertility Rate (children per woman)")
plt.ylabel("Divorce Rate (per 1000 people)")
plt.title("Fertility Rate vs Divorce Rate in UK (1965-2017)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()