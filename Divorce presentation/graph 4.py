#!/usr/bin/env python3
"""
Birth Rate vs Divorce Rate
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#File paths
path_divorce = "/Users/yaminkashim/DAT5501_lab/project/divorces-per-1000-people.csv"
path_birth = "/Users/yaminkashim/DAT5501_lab/project/children-born-per-woman.csv"

#Read CSVs
divorce = pd.read_csv(path_divorce)
birth = pd.read_csv(path_birth)

#Filter for United Kingdom
country = "United Kingdom"
divorce = divorce[divorce["Entity"] == country]
birth = birth[birth["Entity"] == country]

#Select relevant columns
divorce = divorce[["Year", "Crude divorce rate"]]
birth = birth[["Year", "Birth rate"]]  # adjust column name if different

#Merge datasets on Year
df = divorce.merge(birth, on="Year", how="inner")

#Prepare predictor and target
X = df[["Birth rate"]]  # predictor
y = df["Crude divorce rate"]  # target

#Fit linear regression
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

#Print regression results
print("Intercept:", model.intercept_)
print("Coefficient (Birth rate):", model.coef_[0])
print("R-squared:", model.score(X, y))

#Plot Actual vs Predicted Divorce Rate
plt.figure(figsize=(8,6))
plt.scatter(df["Birth rate"], df["Crude divorce rate"], color='blue', edgecolor='k', label="Actual")
plt.plot(df["Birth rate"], y_pred, color='red', linewidth=2, label="Predicted")
plt.xlabel("Birth Rate (per 1000 people)")
plt.ylabel("Divorce Rate (per 1000 people)")
plt.title("Birth Rate vs Divorce Rate in UK")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()