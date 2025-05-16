import pandas as pd
from load import read_dataset

# Load the dataset
df = pd.read_csv("E:\\Gam3a\\big data\\bd-a1\\diabetes.csv")

# Output directory path
output_dir = r'E:\\Gam3a\\big data\\bd-a1\\service-result\\'

# Insight 1: Mean value of a feature
mean_glucose_eda = df['Glucose'].mean()
with open(output_dir + 'eda-in-1.txt', 'w') as f:
    f.write(f'Mean Glucose Level: {mean_glucose_eda}\n')

# Insight 2: Correlation between two features
correlation_eda = df['Age'].corr(df['Glucose'])
with open(output_dir + 'eda-in-2.txt', 'w') as f:
    f.write(f'Correlation between Age and Glucose: {correlation_eda}\n')

# Insight 3: Count of a categorical variable
outcome_count_eda = df['Outcome'].value_counts()
with open(output_dir + 'eda-in-3.txt', 'w') as f:
    f.write(f'Outcome Count:\n{outcome_count_eda}\n')

# Insight 4: Count of a categorical variable
blood_pressure_eda = df['BloodPressure'].value_counts()
with open(output_dir + 'eda-in-4.txt', 'w') as f:
    f.write(f'Blood Pressure Count:\n{blood_pressure_eda}\n')

# Insight 5: Count of a categorical variable
pregnancies_eda = df['Pregnancies'].value_counts()
with open(output_dir + 'eda-in-5.txt', 'w') as f:
    f.write(f'Pregnancies Count:\n{pregnancies_eda}\n')