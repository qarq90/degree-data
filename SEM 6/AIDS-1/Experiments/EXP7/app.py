import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler

X, y_true = make_blobs(n_samples=500, centers=4, cluster_std=0.90, random_state=50)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

inertia_values = []
K_range = range(1, 11)

for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    inertia_values.append(kmeans.inertia_)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(K_range, inertia_values, 'bo-', markersize=8, linewidth=2)
plt.xlabel('Number of Clusters (K)', fontsize=12)
plt.ylabel('Inertia (Within-Cluster SSE)', fontsize=12)
plt.title('Elbow Method for Optimal K', fontsize=14)
plt.grid(True, alpha=0.3)
plt.xticks(K_range)

plt.axvline(x=4, color='red', linestyle='--', alpha=0.7, label='Optimal K=4')
plt.legend()

optimal_k = 4
kmeans_final = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
cluster_labels = kmeans_final.fit_predict(X_scaled)
centroids = kmeans_final.cluster_centers_

centroids_original = scaler.inverse_transform(centroids)

plt.subplot(1, 2, 2)
scatter = plt.scatter(X[:, 0], X[:, 1], c=cluster_labels, cmap='viridis', 
                      s=50, alpha=0.7, edgecolors='black', linewidth=0.5)

plt.scatter(centroids_original[:, 0], centroids_original[:, 1], 
            c='red', marker='X', s=200, linewidths=3, 
            edgecolors='white', label='Centroids')

plt.xlabel('Feature 1', fontsize=12)
plt.ylabel('Feature 2', fontsize=12)
plt.title(f'K-Means Clustering (K={optimal_k}) with Centroids', fontsize=14)
plt.colorbar(scatter, label='Cluster Label')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()



unique, counts = np.unique(cluster_labels, return_counts=True)
for cluster, count in zip(unique, counts):
    percentage = (count / len(cluster_labels)) * 100

centroid_df = pd.DataFrame(centroids_original, 
                          columns=['Feature 1', 'Feature 2'])
centroid_df.index.name = 'Cluster'

from sklearn.metrics import silhouette_score
sil_score = silhouette_score(X_scaled, cluster_labels)

elbow_data = pd.DataFrame({
    'K': list(K_range),
    'Inertia': [round(val, 2) for val in inertia_values],
    'Inertia_Drop': [0] + [round(inertia_values[i-1] - inertia_values[i], 2) 
                           for i in range(1, len(inertia_values))]
})

centroid_df.to_csv('kmeans_centroids.csv')