import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

#Load datasets
education = pd.read_csv("/Users/yaminkashim/DAT5501_lab/project/years-of-schooling.csv")
divorce = pd.read_csv("/Users/yaminkashim/DAT5501_lab/project/divorces-per-1000-people.csv")

#Filter United Kingdom only
edu_uk = education[education["Entity"] == "United Kingdom"]
div_uk = divorce[divorce["Entity"] == "United Kingdom"]

#Compute average years of schooling (men & women combined)
edu_uk["Average schooling (total)"] = edu_uk[["Average years of schooling among women", 
                                              "Average years of schooling among men"]].mean(axis=1)

#Merge by Year
uk_data = pd.merge(edu_uk[["Year", "Average schooling (total)"]],
                   div_uk[["Year", "Crude divorce rate"]],
                   on="Year",
                   how="inner")

#Check
print(uk_data.head())
print(f"Data points: {len(uk_data)}")

#Correlation
corr = uk_data["Average schooling (total)"].corr(uk_data["Crude divorce rate"])
print(f"Correlation (Education vs Divorce): {corr:.3f}")

#Plot relationship
plt.figure(figsize=(10,6))
plt.scatter(uk_data["Average schooling (total)"], uk_data["Crude divorce rate"], label="UK Data Points")
plt.title("UK: Average Years of Schooling vs Divorce Rate")
plt.xlabel("Average Years of Schooling (Men & Women Combined)")
plt.ylabel("Divorces per 1000 People")

#Linear regression fit
X = uk_data["Average schooling (total)"].values.reshape(-1, 1)
y = uk_data["Crude divorce rate"].values
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

plt.plot(uk_data["Average schooling (total)"], y_pred, color="red", linewidth=2, label="Linear Fit")
plt.legend()
plt.grid(True)
plt.show()

#Time trend view
fig, ax1 = plt.subplots(figsize=(10,6))
ax1.plot(uk_data["Year"], uk_data["Average schooling (total)"], linewidth=2, label="Avg Schooling")
ax1.set_ylabel("Average Years of Schooling")
ax2 = ax1.twinx()
ax2.plot(uk_data["Year"], uk_data["Crude divorce rate"], color='red', linewidth=2, label="Divorce Rate")
ax2.set_ylabel("Divorces per 1000 People")
plt.title("UK: Education vs Divorce Rate Over Time")
fig.legend(loc="upper left", bbox_to_anchor=(0.1, 0.9))
plt.show()

from sklearn.preprocessing import PolynomialFeatures

poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)
model_poly = LinearRegression()
model_poly.fit(X_poly, y)
y_poly_pred = model_poly.predict(X_poly)

plt.scatter(uk_data["Average schooling (total)"], y, label="Data")
plt.plot(uk_data["Average schooling (total)"], y_poly_pred, color="red", label="Quadratic Fit")
plt.legend()
plt.title("UK: Quadratic Fit (Education vs Divorce Rate)")
plt.show()