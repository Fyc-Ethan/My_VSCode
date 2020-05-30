# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 20:55:56 2020

@author: Administrator
"""

import pandas as pd
iris_dataframe=pd.DataFrame(X_train,columns=iris_dataset.feature_names)

pd.plotting.scatter_matrix(iris_dataframe,c=y_train,figsize=(15,15),marker='o',
                           hist_kwds={'bins':20},s=60,alpha=.8)

