import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_csv("E:\\Gam3a\\big data\\bd-a1\\diabetes.csv")

# Select suitable columns for K-means
# Let's assume 'Glucose' and 'BMI' are the columns selected for clustering
X = df[['Glucose', 'BMI']]

# Apply K-means algorithm with k=3 and n_init=10
kmeans = KMeans(n_clusters=3, n_init=10, random_state=42)
df['cluster'] = kmeans.fit_predict(X)

# Save the number of records in each cluster
cluster_counts = df['cluster'].value_counts()
cluster_counts.to_csv('k.txt', header=False)

#read_dataset()