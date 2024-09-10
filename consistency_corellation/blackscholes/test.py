import numpy as np
import pandas as pd

# Function to generate random data for options
def generate_random_option_data(num_rows):
    np.random.seed(0)  # For reproducibility
    data = []
    for _ in range(num_rows):
        S = np.random.uniform(20, 200)  # Stock price
        K = np.random.uniform(20, 200)  # Strike price
        r = np.random.uniform(0, 0.15)  # Risk-free interest rate
        q = np.random.uniform(0, 0.05)  # Dividend yield
        vol = np.random.uniform(0.1, 0.5)  # Volatility
        T = np.random.uniform(0.1, 2)  # Time to maturity
        option_type = np.random.choice(['C', 'P'])  # Call or Put
        Divs = 0.00  # Assuming no dividends
        DG_RefValue = np.random.uniform(0, 10)  # Placeholder for reference value
        data.append({
            "S": S, "K": K, "r": r, "q": q, "vol": vol, "T": T, "P/C": option_type, "Divs": Divs, "DG RefValue": DG_RefValue
        })
    return data

# Generate 4 rows of option data as an example
data = generate_random_option_data(800000)

# Optionally, generate more data
# random_data = generate_random_option_data(1000)
# data.extend(random_data)

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a TXT file
with open('option_data1.txt', 'w') as file:
    file.write(f"{len(df)}\n")
    for index, row in df.iterrows():
        file.write(f"{row['S']} {row['K']} {row['r']} {row['q']} {row['vol']} {row['T']} {row['P/C']} {row['Divs']} {row['DG RefValue']}\n")

# Display the DataFrame


