

import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the CSV file
df = pd.read_csv('\release_statsreview_release1\data_and_materials\gamma-ray.csv.csv')

# 2. Extract your X and Y columns by their header names
x = df['seconds']
y = df['count']

# 3. Create the plot
plt.plot(x, y, marker='o', linestyle='-', color='b', label='Data Trend')

# 4. Customize labels and title
plt.xlabel('X Axis Label')
plt.ylabel('Y Axis Label')
plt.title('My CSV Data Plot')
plt.legend()
plt.grid(True)

# 5. Display the graph
plt.show()
