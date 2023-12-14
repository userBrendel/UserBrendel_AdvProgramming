# Making Bar graph
import matplotlib.pyplot as plt

# Info for the bar graph -------------------------------------------------------------------
# Brand names
brands = ["Amazon", "Apple", "Google", "Microsoft", "Walmart", "Samsung Group", "ICBC", "Verizon", "Tesla", "TikTok/Douyin"]
# Brand values in billion U.S. dollars
values = [299.28, 297.51, 281.38, 191.57, 113.78, 99.66, 69.55, 67.44, 66.21, 65.67]

# Creating the bar graph ---------------------------------------------------------
plt.figure(figsize=(10, 6)) # width and height of the figure in inches.
plt.bar(brands, values, color='pink')

# Adding the title and labels
plt.title("Most Valuable Brands Worldwide in 2023 (in billion U.S. dollars)")
plt.xlabel("Brands") # X axis label
plt.ylabel("Brand Value") # Y axis labe;

# Rotating x-axis labels for better readability of words
plt.xticks(rotation=40, ha="right") # x-axis = "brands"

# Displaying the values on top of each bar
# loop to add text annotations on top of each bar in the bar graph
for i, value in enumerate(values):
    plt.text(i, value + 1, f"{value:.2f}", ha='center', va='bottom') #value + 1: This is the y-coordinate of the text annotation. 

# Show the plot
plt.tight_layout()
plt.show()
