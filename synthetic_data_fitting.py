import os
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import unittest

# --------------------
# Configuration
# --------------------
filename = "synthetic_data.csv"  # your CSV
plot_filename = "fit_plot.png"
m_true = 2
b_true = 5
tolerance = 1.0  # acceptable delta for slope/intercept

# --------------------
# Tests
# --------------------
class TestDataPipeline(unittest.TestCase):

    def test_csv_saved(self):
        self.assertTrue(os.path.exists(filename), f"{filename} does not exist.")

    def test_plot_saved(self):
        self.assertTrue(os.path.exists(plot_filename), f"{plot_filename} does not exist.")

    def test_csv_numeric(self):
        df = pd.read_csv(filename)
        # Check for any non-numeric values
        self.assertTrue(np.all(np.isfinite(df['X'])), "Non-numeric values in X")
        self.assertTrue(np.all(np.isfinite(df['Y'])), "Non-numeric values in Y")

    def test_slope_intercept(self):
        df = pd.read_csv(filename)
        X = df['X'].values.reshape(-1, 1)
        Y = df['Y'].values
        model = LinearRegression()
        model.fit(X, Y)
        m_fit = model.coef_[0]
        b_fit = model.intercept_
        self.assertAlmostEqual(m_fit, m_true, delta=tolerance)
        self.assertAlmostEqual(b_fit, b_true, delta=tolerance)

# --------------------
# Run tests
# --------------------
if __name__ == "__main__":
    unittest.main()