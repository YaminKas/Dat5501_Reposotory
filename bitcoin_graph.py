import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression


# LOAD DATA


df = pd.read_csv('bitcoin.csv')

# Convert Date ---> datetime
df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y', errors='coerce')

# Remove rows with bad dates or bad numeric values
#df = df.dropna(subset=['Date', 'Close/Last'])

# Ensure Close/Last is numeric
df['Close/Last'] = pd.to_numeric(df['Close/Last'], errors='coerce')
df = df.dropna(subset=['Close/Last'])

# Sort oldest → newest
df = df.sort_values('Date').reset_index(drop=True)


# PLOT PRICE DATA

plt.figure(figsize=(14,7))
plt.plot(df['Date'], df['Close/Last'], marker='o', linestyle='-', color='blue', label='Close Price')

plt.title("Bitcoin Prices Over Time")
plt.xlabel("Date")
plt.ylabel("Price")
plt.grid(True)
plt.legend()

plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %d %y'))
plt.gcf().autofmt_xdate()

plt.tight_layout()
plt.savefig("bitcoin_plot.png", dpi=150)
plt.show()


# POLYNOMIAL REGRESSION (1–10)


# Convert dates → numerical day index
df['DayIndex'] = (df['Date'] - df['Date'].min()).dt.days

# Split last X days as test data
#test_days = 30
#train_df = df[:-test_days]
#test_df = df[-test_days:]

#X_train = train_df['DayIndex'].values.reshape(-1, 1)
#y_train = train_df['Close/Last'].values

#X_test = test_df['DayIndex'].values.reshape(-1, 1)
#y_test = test_df['Close/Last'].values

X_train = df['DayIndex'].values.reshape(-1, 1)
y_train = df['Close/Last'].values
X_test = X_train


plt.figure(figsize=(14,7))

# Actual price line
plt.plot(df['Date'], df['Close/Last'], label="Actual Price", color="black", linewidth=2)


# Fit polynomial models
for degree in range(1, 11):
    poly = PolynomialFeatures(degree=degree)
    X_train_poly = poly.fit_transform(X_train)

    model = LinearRegression()
    model.fit(X_train_poly, y_train)

    X_test_poly = poly.transform(X_test)
    y_pred = model.predict(X_test_poly)

    # Plot predictions on test period
    plt.plot(df['Date'], y_pred, label=f"Degree {degree}")


plt.title("Polynomial Regression (1-10) - Prediction vs Actual")
plt.xlabel("Date")
plt.ylabel("Price")
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.savefig("poly_predictions.png", dpi=150)
plt.show()

#FIND BEST POLYNOMIAL USING R2

from sklearn.metrics import r2_score

r2_scores = []

for degree in range(1, 11):
    poly = PolynomialFeatures(degree)
    X_poly = poly.fit_transform(X_train)

    model = LinearRegression()
    model.fit(X_poly, y_train)

    y_pred = model.predict(X_poly)
    score = r2_score(y_train, y_pred)
    r2_scores.append(score)
    print(f"Degree {degree} → R² = {score:.5f}")

# Plot R² scores
plt.figure(figsize=(10,5))
plt.plot(range(1,11), r2_scores, marker='o', linewidth=2)
plt.title("Polynomial Fit Quality (R² Score)")
plt.xlabel("Polynomial Degree")
plt.ylabel("R² Score")
plt.grid(True)
plt.tight_layout()
plt.savefig("best_r2_plot.png", dpi=150)
plt.show()
