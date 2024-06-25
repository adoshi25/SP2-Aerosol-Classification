# -*- coding: utf-8 -*-
"""prop_color_ratio.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-Z5DGDR-UeiJVjPjRCo0VE5NA0F4COnx
"""

incandescent_max = []
incandescent_max = original_max_X_train[:, 1]

new_incandescent_max = np.expand_dims(incandescent_max, axis = 1)
new_incandescent_max.shape

scattering = []
scattering = original_max_X_train[:, 0]

new_scattering = np.expand_dims(scattering, axis = 1)
new_scattering.shape

color_channel_ratio.shape
color_channel_ratio = np.array(color_channel_ratio)
color_channel_ratio = np.expand_dims(color_channel_ratio, axis = 1)

color_channel_ratio.shape

np.count_nonzero(np.isinf(color_channel_ratio))
bad_data = np.isinf(color_channel_ratio)
bad_data = bad_data[:, 0]
bad_data.shape

from sklearn.preprocessing import MinMaxScaler
X_all = np.concatenate((z_mean.numpy(), z_mean_1.numpy(), new_scattering, new_incandescent_max, color_channel_ratio), axis = 1)
X_filtered = X_all[~bad_data,:]
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X_filtered)
X_scaled.shape

# X_scaled contains X_train without outliers
# X_scaled contains those three properties as well

# Removing the Outliers
Y_filtered = Y_train[~bad_data]
Y_filtered
Y_filtered.shape

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

n_clusters = 10
kmeans = KMeans(n_clusters=n_clusters, random_state=42).fit(X_scaled)

kmeans_labels = kmeans.labels_
kmeans_centers = kmeans.cluster_centers_

data = pd.DataFrame(X_scaled, columns=['z1', 'z2', 'z3', 'z4', 'scattering_max', 'incandescent_max', 'color_ratio'])
data['Cluster'] = kmeans_labels

sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 8), dpi=300)
sns.scatterplot(data=data, x='color_ratio', y='incandescent_max', hue='Cluster', palette='viridis', alpha=0.6)

for center in kmeans_centers:
    plt.scatter(center[6], center[5], s=200, c='red', marker='X')

plt.title('K-means Clustering in 2D Latent Space')
plt.xlabel('Color Ratio')
plt.ylabel('Incandescent Max')
plt.xlim(0, 0.2)
plt.legend(title='Cluster')

plt.savefig('kmeans_clustering_high_res.png', dpi=300)
plt.show()

# HIGH Resolution Download
# from google.colab import files
# files.download('kmeans_clustering_high_res.png')

from google.colab import files

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 8), dpi=300)
plt.xlim(0, 0.2)
plt.scatter(data['color_ratio'], data['incandescent_max'], c=data['z1'], s=1, cmap='viridis', alpha=0.6)
plt.colorbar()
plt.savefig('scatter_plot_z1_high_res.png', dpi=300)
# HIGH Resolution Download
# plt.close()
# files.download('scatter_plot_z1_high_res.png')


plt.figure(figsize=(10, 8), dpi=300)
plt.xlim(0, 0.2)
plt.scatter(data['color_ratio'], data['incandescent_max'], c=data['z2'], s=1, cmap='viridis', alpha=0.6)
plt.colorbar()
plt.savefig('scatter_plot_z2_high_res.png', dpi=300)
# HIGH Resolution Download
# plt.close()
# files.download("scatter_plot_z2_high_res.png")

plt.figure(figsize=(10, 8), dpi=300)
plt.xlim(0, 0.2)
plt.scatter(data['color_ratio'], data['incandescent_max'], c=data['z3'], s=1, cmap='viridis', alpha=0.6)
plt.colorbar()
plt.savefig('scatter_plot_z3_high_res.png', dpi=300)
# HIGH Resolution Download
# plt.close()
# files.download("scatter_plot_z3_high_res.png")

plt.figure(figsize=(10, 8), dpi=300)
plt.xlim(0, 0.2)
plt.scatter(data['color_ratio'], data['incandescent_max'], c=data['z4'], s=1, cmap='viridis', alpha=0.6)
plt.colorbar()
plt.savefig('scatter_plot_z4_high_res.png', dpi=300)
# HIGH Resolution Download
# plt.close()
# files.download("scatter_plot_z4_high_res.png")