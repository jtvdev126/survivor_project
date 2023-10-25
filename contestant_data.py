contestant_data = [
    {"season": "Season44", "contestant": "Contestant1", "placement": 1, "strategy": "Alliance"},
    {"season": "Season44", "contestant": "Contestant2", "placement": 2, "strategy": "Challenge Beast"},
    # Add data for the remaining contestants
    # ...
    {"season": "Season10", "contestant": "Contestant30", "placement": 10, "strategy": "Social Game"},
]
import pandas as pd

# Create a DataFrame from the contestant data
df = pd.DataFrame(contestant_data)

# Calculate average placement for each strategy
strategy_avg_placement = df.groupby('strategy')['placement'].mean().reset_index()

# Count the number of contestants in each strategy category
strategy_counts = df['strategy'].value_counts().reset_index()

# You can perform more analysis as needed

import matplotlib.pyplot as plt

# Plot average placement by strategy
plt.figure(figsize=(10, 6))
plt.bar(strategy_avg_placement['strategy'], strategy_avg_placement['placement'])
plt.xlabel('Strategy')
plt.ylabel('Average Placement')
plt.title('Average Placement by Strategy in Survivor')
plt.xticks(rotation=45)
plt.show()
