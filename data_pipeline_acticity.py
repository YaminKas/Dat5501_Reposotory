#this imports the needed libraries
import numpy as np
import pandas as pd

#this is setting the slope, intercept and then the number of data points
m = 2     # slope
b = 5     # intercept
number_of_points = 100  # number of data points

# X values between 0 and 50
X = np.linspace(0, 50, number_of_points)

#this generates the  Y numbers with a bit of randomness
randomness = np.random.normal(0, 5, number_of_points)  # mean=0, std=5
Y = m * X + b + randomness

#saving the data to a CSV file
df = pd.DataFrame({'X': X, 'Y': Y})
df.to_csv('synthetic_data.csv', index=False)