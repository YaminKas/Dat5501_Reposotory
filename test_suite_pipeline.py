import os
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import unittest

# Import config values from main.py
from synthetic_data_fitting import filename, plot_filename, m_true, b_true, run_pipeline

tolerance = 1.0  # acceptable delta for slope/intercept

class TestDataPipeline(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Ensure data and plot exist before running tests
        run_pipeline()

    def test_csv_saved(self):
        self.assertTrue(os.path.exists(filename), f"{filename} does not exist.")

    def test_plot_saved(self):
        self.assertTrue(os.path.exists(plot_filename), f"{plot_filename} does not exist.")

    def test_csv_numeric(self):
        df = pd.read_csv(filename)
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

if __name__ == "__main__":
    unittest.main()