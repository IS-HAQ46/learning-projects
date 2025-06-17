import numpy as np
import pandas as pd 
import math

# Load the dataset
df = pd.read_csv("test_scores.csv")

# Extract values
x = df[['math']].values
y = df[['cs']].values

# Normalize x and y
x = (x - x.mean()) / x.std()
y = (y - y.mean()) / y.std()

def gradient_descent(x, y):
    m_curr = b_curr = 0
    iterations = 1000000000
    n = len(x)
    learning_rate = 0.00001
    prev_cost = None

    for i in range(iterations):
        y_predicted = m_curr * x + b_curr

        # Use efficient numpy-based cost calculation
        cost = (1/n) * np.sum((y - y_predicted)**2)
        if prev_cost is not None and math.isclose(cost, prev_cost, abs_tol=1e-20):
            print(f"Converged at iteration {i}")
            break
        
        prev_cost = cost
       

        # Gradients
        md = -(2/n) * np.sum(x * (y - y_predicted))
        bd = -(2/n) * np.sum(y - y_predicted)

        # Update weights
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd

        print(f"m {m_curr}, b {b_curr}, cost {cost} iteration {i}")

# Run gradient descent
gradient_descent(x, y)