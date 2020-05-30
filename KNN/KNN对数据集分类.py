# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 17:25:47 2020

@author: Administrator
"""
import numpy as np
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

iris=datasets.load_iris()
print('数据集结构：',iris.data.shape)

iris_X = iris.data
iris_y = iris.target

iris_train_X,iris_test_X,iris_train_y,iris_test_y=train_test_split(iris_X,iris_y,test_size=0.2,
                                                                   random_state=0)
knn=KNeighborsClassifier()
knn.fit(iris_train_X,iris_train_y)


predict_result=knn.predict(iris_test_X)
print('测试集大小：',iris_test_X.shape)
print('真实集大小：',iris_test_y)

print('预测结果：',predict_result)
print('预测精确率：',knn.score(iris_test_X,iris_test_y))






