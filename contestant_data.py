import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Insert import of csv file here
# Define the path to Excel file
# excel_file = "survivor_data.xlsx"

# Read the data from the Excel file
# df = pd.read_excel(excel_file)

contestant_data = [
    {"season": "Season44", "contestant": "Contestant1", "placement": 1, "strategy": "Alliance"},
    {"season": "Season44", "contestant": "Contestant2", "placement": 2, "strategy": "Challenge Beast"},
    {"season": "Season44", "contestant": "Contestant3", "placement": 3, "strategy": "Social Game"},
    {"season": "Season44", "contestant": "Contestant4", "placement": 4, "strategy": "Social Game"},
    {"season": "Season44", "contestant": "Contestant5", "placement": 5, "strategy": "Social Game"},
    {"season": "Season44", "contestant": "Contestant6", "placement": 6, "strategy": "Social Game"},
    {"season": "Season44", "contestant": "Contestant7", "placement": 7, "strategy": "Social Game"},
    {"season": "Season44", "contestant": "Contestant8", "placement": 8, "strategy": "Social Game"},
    {"season": "Season44", "contestant": "Contestant9", "placement": 9, "strategy": "Social Game"},
    {"season": "Season44", "contestant": "Contestant10", "placement": 10, "strategy": "Social Game"},
    {"season": "Season44", "contestant": "Contestant11", "placement": 11, "strategy": "Social Game"},
    {"season": "Season44", "contestant": "Contestant12", "placement": 12, "strategy": "Social Game"},
    {"season": "Season44", "contestant": "Contestant13", "placement": 13, "strategy": "Social Game"},
    {"season": "Season44", "contestant": "Contestant14", "placement": 14, "strategy": "Social Game"},
    {"season": "Season44", "contestant": "Contestant15", "placement": 15, "strategy": "Social Game"},
    {"season": "Season44", "contestant": "Contestant16", "placement": 16, "strategy": "Social Game"},
    {"season": "Season44", "contestant": "Contestant17", "placement": 17, "strategy": "Social Game"},
    {"season": "Season44", "contestant": "Contestant18", "placement": 18, "strategy": "Social Game"},
    {"season": "Season44", "contestant": "Contestant19", "placement": 19, "strategy": "Social Game"},
    {"season": "Season44", "contestant": "Contestant20", "placement": 20, "strategy": "Social Game"},
    {"season": "Season44", "contestant": "Contestant21", "placement": 21, "strategy": "Social Game"},
    {"season": "Season44", "contestant": "Contestant22", "placement": 22, "strategy": "Social Game"},
    {"season": "Season44", "contestant": "Contestant23", "placement": 23, "strategy": "Social Game"},
    {"season": "Season44", "contestant": "Contestant24", "placement": 24, "strategy": "Social Game"},
    {"season": "Season44", "contestant": "Contestant25", "placement": 25, "strategy": "Social Game"},
    {"season": "Season44", "contestant": "Contestant26", "placement": 26, "strategy": "Social Game"},
    {"season": "Season44", "contestant": "Contestant27", "placement": 27, "strategy": "Social Game"},
    {"season": "Season44", "contestant": "Contestant28", "placement": 28, "strategy": "Social Game"},
    {"season": "Season44", "contestant": "Contestant29", "placement": 29, "strategy": "Social Game"},
    {"season": "Season44", "contestant": "Contestant30", "placement": 30, "strategy": "Social Game"},
    {"season": "Season43", "contestant": "Contestant1", "placement": 1, "strategy": "Alliance"},
    {"season": "Season43", "contestant": "Contestant2", "placement": 2, "strategy": "Challenge Beast"},
    {"season": "Season43", "contestant": "Contestant3", "placement": 3, "strategy": "Social Game"},
    {"season": "Season43", "contestant": "Contestant4", "placement": 4, "strategy": "Alliance"},
    {"season": "Season43", "contestant": "Contestant5", "placement": 5, "strategy": "Alliance"},
    {"season": "Season43", "contestant": "Contestant6", "placement": 6, "strategy": "Social Game"},
    {"season": "Season43", "contestant": "Contestant7", "placement": 7, "strategy": "Alliance"},
    {"season": "Season43", "contestant": "Contestant8", "placement": 8, "strategy": "Alliance"},
    {"season": "Season43", "contestant": "Contestant9", "placement": 9, "strategy": "Social Game"},
    {"season": "Season43", "contestant": "Contestant10", "placement": 10, "strategy": "Social Game"},
    {"season": "Season43", "contestant": "Contestant11", "placement": 11, "strategy": "Social Game"},
    {"season": "Season43", "contestant": "Contestant12", "placement": 12, "strategy": "Social Game"},
    {"season": "Season43", "contestant": "Contestant13", "placement": 13, "strategy": "Social Game"},
    {"season": "Season43", "contestant": "Contestant14", "placement": 14, "strategy": "Social Game"},
    {"season": "Season43", "contestant": "Contestant15", "placement": 15, "strategy": "Social Game"},
    {"season": "Season43", "contestant": "Contestant16", "placement": 16, "strategy": "Social Game"},
    {"season": "Season43", "contestant": "Contestant17", "placement": 17, "strategy": "Social Game"},
    {"season": "Season43", "contestant": "Contestant18", "placement": 18, "strategy": "Social Game"},
    {"season": "Season43", "contestant": "Contestant19", "placement": 19, "strategy": "Social Game"},
    {"season": "Season43", "contestant": "Contestant20", "placement": 20, "strategy": "Social Game"},
    {"season": "Season43", "contestant": "Contestant21", "placement": 21, "strategy": "Social Game"},
    {"season": "Season43", "contestant": "Contestant22", "placement": 22, "strategy": "Social Game"},
    {"season": "Season43", "contestant": "Contestant23", "placement": 23, "strategy": "Social Game"},
    {"season": "Season43", "contestant": "Contestant24", "placement": 24, "strategy": "Social Game"},
    {"season": "Season43", "contestant": "Contestant25", "placement": 25, "strategy": "Social Game"},
    {"season": "Season43", "contestant": "Contestant26", "placement": 26, "strategy": "Social Game"},
    {"season": "Season43", "contestant": "Contestant27", "placement": 27, "strategy": "Social Game"},
    {"season": "Season43", "contestant": "Contestant28", "placement": 28, "strategy": "Social Game"},
    {"season": "Season43", "contestant": "Contestant29", "placement": 29, "strategy": "Social Game"},
    {"season": "Season43", "contestant": "Contestant30", "placement": 30, "strategy": "Social Game"},
]

# Create a DataFrame from the contestant data
# Remove this if using an Excel file with contestant data
df = pd.DataFrame(contestant_data)

# Calculate average placement for each strategy
strategy_avg_placement = df.groupby(['season', 'strategy'])['placement'].mean().reset_index()

# Pivot the data to make it sutiable for a stacked bar chart
stacked_data = strategy_avg_placement.pivot(index='season', columns='strategy', values='placement').fillna(0)

# Count the number of contestants in each strategy category
# strategy_counts = df['strategy'].value_counts().reset_index()

# Set the style of the plot
#sns.set_style("whitegrid")

# Create a stacked horizontal bar chart
plt.figure(figsize=(12,8))
stacked_data.plot(kind='barh', stacked=True)
plt.xlabel('Average Placement')
plt.ylabel('Season')
plt.title('Average Placement by Strategy in Survivor for Multiple Seasons')
plt.legend(title='Strategy')
plt.show()

# Create a horizontal grouped bar chart
#plt.figure(figsize=(10,6))
#sns.barplot(x='placement', y='season', hue='strategy', data=strategy_avg_placement, ci=None)
#plt.xlabel('Average Placement')
#plt.ylabel('Strategy')
#plt.title('Average Placement by Strategy in Survivor for Multiple Seasons')
#plt.legend(title='Season')
#plt.show()

# Plot average placement by strategy as a horizontal graph
#plt.figure(figsize=(10, 6))
#plt.barh(strategy_avg_placement['strategy'], strategy_avg_placement['placement'])
#plt.ylabel('Strategy', fontsize=14)
#plt.xlabel('Average Placement', fontsize=14)
#plt.title('Average Placement by Strategy in Survivor', fontsize=18)
#plt.xticks(rotation=0, fontsize=9)
#plt.show()
