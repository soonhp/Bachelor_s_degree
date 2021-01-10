# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 20:10:53 2019

@author: 박순혁
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
os.chdir('C:\\Users\\박순혁\\Desktop\\class\\LAB')
cctv=pd.read_excel('python_programming_Data.xlsx')
import statsmodels.api as sm
x = cctv.drop(['CCTV_count','area'], axis=1)
y=cctv.CCTV_count
x = sm.add_constant(x)
model = sm.OLS(y,x).fit()
model.summary()

s=cctv.corr()
np.corrcoef(cctv)

x = cctv.drop(['CCTV_count','area','theft_crime','crime','traffic_crime','drug_crime'], axis=1)
y = cctv.CCTV_count
x=sm.add_constant(x)
model2=sm.OLS(y,x).fit()
model2.summary()


#2. backward elimation
x = cctv.drop(['CCTV_count','area','population'], axis=1)
y = cctv.CCTV_count
cols = list(x.columns)
pmax = 1
while (len(cols) > 0):
    p = []
    x = x[cols]
    x = sm.add_constant(x)
    model = sm.OLS(y, x).fit()
    p = pd.Series(model.pvalues.values[1:], index=cols)
    pmax = max(p)
    features_with_p_max = p.idxmax()
    if (pmax>.05):
        cols.remove(features_with_p_max)
    else:
        break
selected_features_BE = cols
selected_features_BE

x=cctv[['force_crime','violent_crime']]
y=cctv.CCTV_count
x=sm.add_constant(x)
model3=sm.OLS(y,x).fit()
model3.summary()
