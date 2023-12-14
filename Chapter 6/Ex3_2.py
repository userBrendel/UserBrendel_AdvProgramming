#LINE GRAPH

import matplotlib.pyplot as plt 
# 2D plotting library for Python that allows you to create a variety of static, animated, 
# and interactive plots and visualizations. 

# Line 1: (1, 2) to (6, 8) 
x1 = [1, 6] # point of x1 (x,y)
y1 = [2, 8] # point of x2 (x,y)

# Line 2: (1, 3) to (2, 8) to (6, 1) to (8, 10)
x2 = [1, 2, 6, 8]
y2 = [3, 8, 1, 10]

# Plotting Line 1
plt.plot(x1, y1, label="Line 1", marker='o') #shows style

# Plotting Line 2 as a dotted line
plt.plot(x2, y2, label="Line 2", linestyle='dotted', marker='o')

# Adding labels and title
plt.xlabel('X-axis') # sets the label for the X-axis of the plot. 
plt.ylabel('Y-axis') #  sets the label for the Y-axis of the plot
plt.title('Line Graph') # title of plot

# Adding legend
# automatically picks up the labels
plt.legend()

# Display the plot
plt.show()
