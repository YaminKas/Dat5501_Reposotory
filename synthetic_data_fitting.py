import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# --------------------
# Configuration
# --------------------
filename = "synthetic_data.csv"
plot_filename = "fit_plot.png"
m_true = 2
b_true = 5

# --------------------
# Data Generation
# --------------------
def generate_data(n=100, noise_std=1.0):
    X = np.linspace(0, 10, n)
    noise = np.random.normal(0, noise_std, n)
    Y = m_true * X + b_true + noise
    return pd.DataFrame({"X": X, "Y": Y})

def save_csv(df):
    df.to_csv(filename, index=False)

def plot_data(df):
    plt.scatter(df["X"], df["Y"], label="Data")
    plt.plot(df["X"], m_true * df["X"] + b_true, color="red", label="True line")
    plt.legend()
    plt.savefig(plot_filename)
    plt.close()

# --------------------
# Pipeline Runner
# --------------------
def run_pipeline():
    df = generate_data()
    save_csv(df)
    plot_data(df)

if __name__ == "__main__":
    run_pipeline()