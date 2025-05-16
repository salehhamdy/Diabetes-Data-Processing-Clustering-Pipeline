import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("E:\\Gam3a\\big data\\bd-a1\\diabetes.csv")

# Create a histogram for the Outcome column
plt.figure(figsize=(10, 6))
df['Outcome'].hist(bins=50)
plt.title('Outcome Levels Distribution')
plt.xlabel('Outcome Level')
plt.ylabel('Number of Individuals')

# Specify the full path for the output file
output_directory = 'E:\\Gam3a\\big data\\bd-a1\\service-result\\'
output_filename = 'vis_1.png'
output_path = output_directory + output_filename

# Save the figure
plt.savefig(output_path)

# Create a histogram for the 'Glucose' column
plt.figure(figsize=(10, 6))
df['Glucose'].hist(bins=50)
plt.title('Glucose Levels Distribution')
plt.xlabel('Glucose Level')
plt.ylabel('Number of Individuals')
plt.savefig('vis.png')

# Specify the full path for the output file
output_directory = 'E:\\Gam3a\\big data\\bd-a1\\service-result\\'
output_filename = 'vis_2.png'
output_path = output_directory + output_filename

# Save the figure
plt.savefig(output_path)

#read_dataset ()