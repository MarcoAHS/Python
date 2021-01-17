from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np



df = pd.read_csv('C:\\Users\marco\Desktop\Semestre Final 2020\Introduccion al Aprendizaje Automatico\\penguin-data.csv')
df.head()

plt.scatter(df.FlipperLength,df.BodyMass)
plt.xlabel('Dimension 1')
plt.ylabel('Dimension 2')
plt.title('Data')
plt.show()

# Create a model based on 3 centroids
model = KMeans(n_clusters=3, init='k-means++', n_init=100, max_iter=1000)
# Fit to the data and predict the cluster assignments for each data point
km_clusters = model.fit_predict(df.values)
# View the cluster assignments
km_clusters

col_dic = {0:'blue',1:'green',2:'orange'}
mrk_dic = {0:'*',1:'x',2:'+'}
colors = [col_dic[x] for x in km_clusters]
markers = [mrk_dic[x] for x in km_clusters]
for sample in range(len(km_clusters)):
  plt.scatter(df.FlipperLength[sample],df.BodyMass[sample], color = colors[sample], marker=markers[sample])
plt.xlabel('Dimension 1')
plt.ylabel('Dimension 2')
plt.title('Assignments')
plt.show()

# Create 10 models with 1 to 10 clusters
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i)
    # Fit the data points
    kmeans.fit(df.values)
    # Get the WCSS (inertia) value
    wcss.append(kmeans.inertia_)
    
#Plot the WCSS values onto a line graph
plt.plot(range(1, 11), wcss)
plt.title('WCSS by Clusters')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()