# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 20:46:13 2020

@author: Administrator
"""
from sklearn.datasets import load_iris
iris_dataset=load_iris()
iris_dataset

print("数据集的Keys:\n",iris_dataset.keys())
print("特证名:\n",iris_dataset['feature_names'])
print("数据类型:\n",type(iris_dataset['data']))
print("数据维度:\n",iris_dataset['data'].shape)
print("前五条数据:\n",format(iris_dataset['data'][:5]))
print("标记名:\n",iris_dataset['target_names'])
print("标记类型:\n",type(iris_dataset['target']))
print("标记维度:\n",iris_dataset['target'].shape)
print("标记值:\n",iris_dataset['target'])

#
print("数据集简介:\n",iris_dataset['DESCR'][:20]+"\n......")

