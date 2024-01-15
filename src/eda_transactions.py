"""
exploring the transactions dataset
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

script_path = __file__
project_path = os.path.dirname(os.path.dirname(script_path))
data_file = os.path.join(project_path, "data", "transactions.tsv")
data = pd.read_csv(data_file, delimiter="\t")

# Convert 'Date' to datetime type
data['Date'] = pd.to_datetime(data['Date'])

# Plot 'Balance' line per 'Id'
plt.figure(figsize=(10, 6))

for id_value, group in data.groupby('Id'):
    plt.plot(group['Date'], group['Balance'], label=f'Id {id_value}')

plt.title('Balance per Id Over Time')
plt.xlabel('Date')
plt.ylabel('Balance')
plt.legend()

output_file = os.path.join(project_path, "docs", "images", "balance_per_id_plot.png")
plt.savefig(output_file)
