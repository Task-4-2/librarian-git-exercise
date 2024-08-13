import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta

# Start from 30 days in the past
end_date = datetime.now().date()
start_date = end_date - timedelta(days=30)
dates = [start_date + timedelta(days=i) for i in range(31)]

# Generate random integers between 10 and 23
random_numbers = np.random.randint(10, 24, size=31)

# Create a DataFrame
df = pd.DataFrame({
    'date': dates,
    'transitions': random_numbers
})

# Ensure the 'results' directory exists
os.makedirs('01_raw_data', exist_ok=True)

# Save the DataFrame to a CSV file
df.to_csv('01_raw_data/20240813_3_state_transition_projection_algo3.csv', index=False)

print('Run finished.')