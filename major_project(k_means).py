# -*- coding: utf-8 -*-
"""MAJOR_PROJECT(K-MEANS).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/gist/ZORO12347/72447ccb4a1ce27c13aff41de72a523d/untitled1.ipynb

# ***MAJOR PROJECT (CHOOSE A DATASET AND APPLY K MEANS CLUSTERING)***

---
"""

#1.Take data and create dataframe
import pandas as pd
df=pd.read_csv('/content/DATA (1).csv')

df

df.shape #145 rows, 33 cols

df.info()

#Input - COURSE ID and GRADE

#4.divide the data into i/p
x=df.iloc[:,31:33].values
x

#VISUALISATION
import matplotlib.pyplot as plt
plt.scatter(df['COURSE ID'],df['GRADE'])
#Here we got only one cluster before applying any clustereing technique

#Here our main task is to find out the number of clusters(k)
import numpy as np
np.sqrt(145) #145 is the total no of points
#No. of cluster - k
#k value should not exceed the square root of the total no of points
#Hence k value should be in the range of 2 to 12

#We need to find out the number of clusters(k)
#1.ELBOW METHOD - Slightly Confusing
#2.SILHOUETTE SCORE METHOD - Very accurate

#1.ELBOW METHOD
from sklearn.cluster import KMeans
k=range(2,12) #my range is in between 2 and 12

sse=[] #blank list

#for i in range(2,12):
for i in k:
  model_demo=KMeans(n_clusters=i,random_state=0)
  model_demo.fit(x)
  sse.append(model_demo.inertia_) #.inertia_ calculates the sum of squared error
plt.scatter(k,sse)
plt.plot(k,sse)

#2.SILHOUTTE SCORE METHOD
from sklearn.metrics import silhouette_score
k=range(2,12)
for i in k:
  model_demo=KMeans(n_clusters=i,random_state=0)
  model_demo.fit(x)
  y_pred=model_demo.predict(x)
  print(f"{i} Clusters, Score={silhouette_score(x,y_pred)}")
  plt.bar(i,silhouette_score(x,y_pred))

#7.APPLY CLUSTER
k=11
from sklearn.cluster import KMeans

model=KMeans(n_clusters=k,random_state=0)
model.fit(x)

KMeans(n_clusters=11, random_state=0)

y=model.predict(x) #predicted output
y

y.size

x[y==1,1]
#so the first '1' is cluster no. 1and the second '1' is column index 1
#the value of input, when cluster 1 is selected and column index 1 is selected

np.unique(y,return_counts=True)

#FINAL VISUALISATION
plt.figure(figsize=(10,5))
for i in range(k):
  plt.scatter(x[y==i,0],x[y==i,1],label=f'Cluster {i}')
plt.scatter(model.cluster_centers_[:,0],model.cluster_centers_[:,1],s=15,c='black',label='Centroids')
plt.legend()