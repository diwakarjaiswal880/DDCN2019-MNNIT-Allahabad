import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score

names=['sepal_length','sepal_width','petal_length','petal_width','class']

df=pd.read_csv('/home/cloudera/Desktop/diwakar/data/IRIS.csv',names=names
)
print(df.head())
X=np.array(df.iloc[:,0:4])
Y=np.array(df['class'])
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.33)
knn=KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train,Y_train)
pred=knn.predict(X_test)
print (' Accuracy score is',accuracy_score(Y_test, pred))
myList=list(range(1,50))
#subsetting just the odd ones
neighbors=list(filter(lambda x:x%2!=0, myList))
print(neighbors)
cv_scores=[]
for k in neighbors:
    knn=KNeighborsClassifier(n_neighbors=k)
    scores=cross_val_score(knn,X_train,Y_train,cv=10,scoring='accuracy')
    cv_scores.append(scores.mean())
MSE=[1-x for x in cv_scores]
optimal_k=neighbors[MSE.index(min(MSE))]
plt.plot(neighbors,MSE)

#plt.xlabel("k neighbors")
#plt.ylabel("mean standard error")
plt.title("Model MSE Graph")
plt.xlabel('Number of Neighbors k')
plt.ylabel('Misclassification Error')
plt.savefig('/home/cloudera/Desktop/diwakar/figures/asgn2.pdf')
plt.show()



