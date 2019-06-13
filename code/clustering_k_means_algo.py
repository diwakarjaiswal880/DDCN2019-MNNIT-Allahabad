import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
x=[1,5,1.5,8,1,9]
y=[2,8,1.8,8,0.6,11]
print (x )
print (y)
plt.scatter(x,y)
plt.show()
X=np.array([[1,2],[5,8],[1.5,1.8],[8,8],[1,0.6],[9,11]])
kmeans=KMeans(n_clusters=2)
kmeans.fit(X)
centroids=kmeans.cluster_centers_
print(centroids)
labels=kmeans.labels_
print (labels)
colors=["r.","g."]
for i in range(len(X)):
    print ("coordinate:",X[i],"labels:",labels[i])
    plt.plot(X[i][0],X[i][1],colors[labels[i]])
plt.scatter(centroids[:,0],centroids[:,1],marker="x",s=150)
plt.show()
d=pd.read_csv('/home/cloudera/Desktop/diwakar/data/faithful.csv')
print(d.head())
plt.scatter(d.eruptions,d.waiting)
plt.title('Old Faithfull Data Scatter Plot')
plt.xlabel('Length of eruptions')
plt.ylabel('Time between eruptions')
plt.show()
d1=np.array(d)
k=2
kmeans=KMeans(n_clusters=k)
kmeans.fit(d1)
labels=kmeans.labels_
centroids=kmeans.cluster_centers_
for i in range (k):
    ds=d1[np.where(labels==i)]
    plt.plot(ds[:,0],ds[:,1],'o',markersize=7)
    lines=plt.plot(centroids[i,0],centroids[i,1],'kx')
    plt.setp(lines,ms=15.0)
    plt.setp(lines,mew=4.0)
plt.show()





