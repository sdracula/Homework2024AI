import matplotlib.pyplot as plt
import numpy as np
import math
import random
import time

#计时开始
start = time.time()
# 31个城市的坐标
city_condition = [[106.54, 29.59], [91.11, 29.97], [87.68, 43.77], [106.27, 38.47], [111.65, 40.82], [108.33, 22.84], [126.63, 45.75], [125.35, 43.88], [123.38, 41.8], [114.48, 38.03], [112.53, 37.87], [101.74, 36.56], [117.0, 36.65], [113.6, 34.76], [118.78, 32.04], [117.27, 31.86], [120.19, 30.26], [119.3, 26.08], [115.89, 28.68], [113.0, 28.21], [114.31, 30.52], [113.23, 23.16], [121.5, 25.05], [110.35, 20.02], [103.73, 36.03], [108.95, 34.27], [104.06, 30.67], [106.71, 26.57], [102.73, 25.04], [114.1, 22.2], [113.33, 22.13]]# 距离矩阵
train_v = np.array(city_condition[:10])
train_d=train_v
dist = np.zeros((train_v.shape[0],train_d.shape[0]))
# 使用numpy计算生成距离矩阵，计算不同城市之间的距离:
city_count = 10
Distance = np.zeros([city_count, city_count])
for i in range(city_count): 
    for j in range(city_count): 
        dist[i][j] = math.sqrt( 
            (city_condition[i][0] - city_condition[j][0]) ** 2 + (city_condition[i][1] - city_condition[j][1]) ** 2)
"""
s:已经遍历过的城市
dist：城市间距离矩阵
sumpath:目前的最小路径总长度
Dtemp：当前最小距离
flag：访问标记
"""
i=1
n=train_v.shape[0]
j=0
sumpath=0
s=[]
s.append(0)
# start = time.clock()
while True:
    k=1
    Detemp=10000000
    while True:
        l=0
        flag=0
        if k in s:
            flag = 1
        if (flag==0) and (dist[k][s[i-1]] < Detemp):
            j = k;
            Detemp=dist[k][s[i - 1]];
        k+=1
        if k>=n:
            break;
    s.append(j)
    i+=1;
    sumpath+=Detemp
    if i>=n:
        break;
sumpath+=dist[0][j]
# end = time.clock()
print("结果：")
print(sumpath)
for m in range(n):
    print("%s-> "%(s[m]),end='')
# print()
# print("程序的运行时间是：%s"%(end-start))