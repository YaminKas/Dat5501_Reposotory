import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import unittest
import time

# --------------------
# Step 1: Generate synthetic data
# --------------------
m_true = 2   # slope
b_true = 5   # intercept
n_points = 10

X = np.linspace(0, 50, n_points)
#noise = np.random.normal(0, 5, n_points)
Y = m_true * X + b_true #+ noise

# Save to CSV with timestamped filename
filename = f"synthetic_dat_{int(time.time())}.csv"
df = pd.DataFrame({'X': X, 'Y': Y})
df.to_csv(filename, index=False)
print(f"Data saved to {filename}")

# --------------------
# Step 2: Load data + fit line
# --------------------
df_loaded = pd.read_csv(filename)
X_loaded = df_loaded['X'].values.reshape(-1, 1)
Y_loaded = df_loaded['Y'].values

model = LinearRegression()
model.fit(X_loaded, Y_loaded)

m_fit = model.coef_[0]
b_fit = model.intercept_

print(f"Fitted slope: {m_fit:.2f}, Fitted intercept: {b_fit:.2f}")

# --------------------
# Step 3: Unit test with tolerance
# --------------------
tolerance = 1.0  # adjust if needed

class TestFit(unittest.TestCase):
    def test_slope(self):
        self.assertAlmostEqual(m_fit, m_true, delta=tolerance)
    def test_intercept(self):
        self.assertAlmostEqual(b_fit, b_true, delta=tolerance)

unittest.main(argv=[''], exit=False)

# --------------------
# Step 4: Plot and save
# --------------------
X_line = np.linspace(min(X_loaded), max(X_loaded), 100).reshape(-1,1)
Y_line_true = m_true * X_line + b_true
Y_line_fit = model.predict(X_line)

plt.scatter(X_loaded, Y_loaded, label="Data", alpha=0.6)
plt.plot(X_line, Y_line_true, 'g--', label="True line")
plt.plot(X_line, Y_line_fit, 'r-', label="Best fit")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.savefig("fit_plot.png", dpi=150)
plt.show()
print("Plot saved as fit_plot.png")