# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 14:29:36 2020

@author: Administrator
"""

#填空题
#coding=utf-8
from numpy import *
from matplotlib import pyplot as plt    

#计算两个向量的欧式距离
def distEclud(vecA, vecB):
    return sqrt(sum(power(vecA - vecB, 2)))

#随机选K个点作为种子   
def initCenter(dataSet, k):
    print('2.initialize cluster center...')
    shape=dataSet.shape
    n = shape[1]  #列数    
    classCenter = array(zeros((k,n)))
    #取前k个数据点作为初始聚类中心
    for j in range(n):        
        firstK=dataSet[:k,j]
        classCenter[:,j] = firstK
    return classCenter
#实现k-Means算法   
def myKMeans(dataSet,k):
    m = len(dataSet)    #行数    
    clusterPoints = array(zeros((m,2)))  #各簇中的数据点
    classCenter = initCenter(dataSet, k) #各簇中心
    clusterChanged = True
    print('3.recompute and reallocated...')
    while clusterChanged:  #重复计算，直到簇分配不再变化
        clusterChanged = False
        #将每个数据点分配到最近的簇
        for i in range(m):   
            minDist = inf
            minIndex = -1
            for j in range(k):
                distJI = distEclud(classCenter[j,:],dataSet[i,:])
                if distJI < minDist:
                    minDist = distJI; minIndex = j
            if clusterPoints[i,0] != minIndex: 
                clusterChanged = True
            clusterPoints[i,:] = minIndex,minDist**2
        #重新计算簇中心   
        for cent in range(k):
            ptsInClust = dataSet[nonzero(clusterPoints[:,0]==cent)[0]]
            classCenter[cent,:] = mean(ptsInClust, axis=0)
    return classCenter,clusterPoints

#显示聚类结果    
def show(dataSet, k, classCenter, clusterPoints):   
    print('4.load the map...')
    fig = plt.figure()
    rect=[0.1,0.1,1.0,1.0]
    axprops = dict(xticks=[], yticks=[])
    ax0=fig.add_axes(rect, label='ax0', **axprops)
    imgP = plt.imread('city.png')
    ax0.imshow(imgP)
    ax1=fig.add_axes(rect, label='ax1', frameon=False)
    print('5.show the clusters...')
    numSamples = len(dataSet) #对象数量
    mark = ['ok', '^b', 'om', 'og', 'sc']  
    #根据每个对象的坐标绘制点
    for i in range(numSamples):  
        markIndex = int(clusterPoints[i, 0])%k          
        ax1.plot(dataSet[i, 0], dataSet[i, 1], mark[markIndex])  
    #标记每个簇的中心点    
    for i in range(k):  
        markIndex = int(clusterPoints[i, 0])%k         
        ax1.plot(classCenter[i, 0], classCenter[i, 1], '^r', markersize = 12)  
    plt.show()
      
print('1.load dataset...')
dataSet=loadtxt('testSet.txt')
K=5   #类的数量
classCenter,classPoints= myKMeans(dataSet,K)
show(dataSet,K,classCenter,classPoints)