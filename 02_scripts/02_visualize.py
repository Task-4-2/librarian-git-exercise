import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Read the CSV file
df = pd.read_csv('01_raw_data/20240813_4_state_transition_projection_algo4.csv')

# Convert the 'date' column to datetime
df['date'] = pd.to_datetime(df['date'])

# Set up the plot style
sns.set_style("whitegrid")
plt.figure(figsize=(12, 6))

# Create the line plot
sns.lineplot(x='date', y='transitions', data=df, marker='o')

# Customize the plot
plt.title('Transitions Over Time', fontsize=14)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Transitions', fontsize=12)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))
plt.xticks(rotation=90, ha='right')
plt.tight_layout()

# Save the plot
plt.savefig('03_graphics/20240813_4_state_transition_projection_algo4.png')
print("File successfully saved.")
