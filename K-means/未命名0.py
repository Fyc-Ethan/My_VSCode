# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 18:23:49 2020

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans

dataset=pd.read_csv('Customer_Info.csv')
X=dataset.iloc[:,[4,3]].values

kmeans=KMeans(n_clusters=4,init='k-means++',max_iter=300,n_init=10,random_state=0)
y_kmeans=kmeans.fit_predict(X)

plt.scatter(X[y_kmeans == 0,0],X[y_kmeans == 0,1],s=100,c='red',label='Not very rich')

plt.scatter(X[y_kmeans == 2,0],X[y_kmeans == 2,1],s=100,c='green',label='Middle')

plt.scatter(X[y_kmeans == 1,0],X[y_kmeans == 1,1],s=100,c='blue',label='Rich')

plt.scatter(X[y_kmeans == 3,0],X[y_kmeans == 3,1],s=100,c='black',label='little middle')


plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=250,c='yellow',label='Centroids')

plt.title('Clusters of customer Info')
plt.xlabel('Deposit')
plt.ylabel('Age')
plt.legend()
plt.show()




