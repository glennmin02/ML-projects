import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

df = pd.read_csv('Mall_Customers.csv')

# Select relevant features for clustering
x = df[['Annual_Income_k', 'Spending_Score']]

# Determine optimal number of clusters using Elbow Method
inertia_values = []
for k in range(1, 10):
    km = KMeans(n_clusters=k)
    km.fit(x)
    inertia_values.append(km.inertia_) # WCSS

# Elbow Method Plot
plt.figure(figsize=(8, 5))
plt.plot(range(1, 10), inertia_values)
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia (WCSS)')
plt.title('Elbow Method')
plt.show()

# K-Means Clustering with optimal k (assumed 5 from Elbow Method)
kmeans = KMeans(n_clusters=5, random_state=42)
kmeans.fit(x)
labels = kmeans.labels_

# Customer Segments Visualization
plt.figure(figsize=(10, 6))
plt.scatter(x['Annual_Income_k'], x['Spending_Score'], c=labels, cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1],
            s=300, c='red', marker='X', edgecolors='black', label='Centroids')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.title('Customer Segments')
plt.legend()
plt.colorbar(label='Cluster')
plt.show()

# Add cluster labels to dataframe
df['Cluster'] = labels

# See the characteristics of each cluster
print(df.groupby('Cluster')[['Annual_Income_k', 'Spending_Score']].mean())

print(df['Cluster'].value_counts().sort_index())

"""
Memo:
- The code performs K-Means clustering on a dataset of mall customers based on their annual income and spending score.
- It reads the data from a CSV file, selects relevant features, and fits a K-Means model with 5 clusters.
- The Elbow Method is used to determine the optimal number of clusters by plotting inertia values for k from 1 to 9.
- The customer segments are visualized in a scatter plot, with cluster centroids highlighted.
- Finally, the cluster labels are added to the original dataframe, and the mean characteristics of each cluster are printed along with the count of customers in each cluster.
- This analysis helps in understanding customer behavior and segmenting them for targeted marketing strategies.
"""