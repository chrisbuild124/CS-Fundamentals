# Name: Christopher Sexton
# OSU Email: sextonch@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 
# Due Date: 1/17/2024
# Description: *

import matplotlib.pyplot as plt

# Data
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [10, 20, 15, 25]

# Create bar graph
plt.bar(categories, values)

# Add labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Graph Example')

# Display the plot
plt.show()
