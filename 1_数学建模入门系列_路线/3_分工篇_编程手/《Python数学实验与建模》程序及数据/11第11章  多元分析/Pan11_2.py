#程序文件Pan11_2.py
import numpy as np; import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
a=pd.read_csv("iris.csv")
b=a.drop(labels="Species",axis=1)
md=KMeans(3); md.fit(b)  #构建模型并求解模型
labels=md.labels_ ;  centers=md.cluster_centers_
b['cluster']=labels  #数据框b添加一个列变量cluster
c=b.cluster.value_counts()  #各类频数统计
plt.rc('font',family='SimHei'); 
str1=['^r','.k','*b']; plt.subplot(121)
for i in range(len(centers)):
    plt.plot(b['Petal_Length'][labels==i],b['Petal_Width'][labels==i],
                str1[i],markersize=3,label=str(i))
    plt.legend(); plt.xlabel("(a)KMeans聚类结果")
plt.subplot(122); str2=['setosa','versicolour','virginica']
ind=np.c_[np.zeros((1,50)),np.ones((1,50)),2*np.ones((1,50))].flatten()
for i in range(3):
    plt.plot(b['Petal_Length'][ind==i],b['Petal_Width'][ind==i],
                str1[i],markersize=3,label=str2[i])
    plt.legend(); plt.xlabel("(b)原数据的类别")
plt.show()



