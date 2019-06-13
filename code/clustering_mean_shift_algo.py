import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import MeanShift
from sklearn.datasets.samples_generator import make_blobs
centers=[[1,1],[5,5]]
X,Y=make_blobs(n_samples=200,centers=centers,cluster_std=1)
plt.scatter(X[:,0],X[:,1])
plt.show()
ms=MeanShift()
ms.fit(X)
labels=ms.labels_
clusters_centers=ms.cluster_centers_
n_clusters=len(np.unique(labels))
print(" Number of Estimated Clusters",n_clusters)
colors=["g.","r.","c.","y.","b.","k","y.","m."]
print(colors)
print(labels)
for i in range(len(X)):
    plt.plot(X[i][0],X[i][1],colors[labels[i]],markersize=10)
plt.scatter(clusters_centers[:,0],clusters_centers[:,1],marker="x",s=150,linewidth=5, zorder=10)
plt.show()



