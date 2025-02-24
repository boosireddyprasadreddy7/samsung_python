
# Generating 23 equally spaced values between 0 and 100

# Explanation: Using np.linspace() to generate specified number of values in a range

import numpy as np


values = np.linspace(0, 100, 23)
print("Generated values:", values)
print("Total count:", len(values))









# Creating a DataFrame

# Explanation: Using pandas to create a DataFrame from a dictionary

import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Salary': [50000, 60000, 70000]}
df = pd.DataFrame(data)
print(df)