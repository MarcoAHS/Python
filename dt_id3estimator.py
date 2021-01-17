import numpy as np 
import pandas as pd
from sklearn import metrics
from sklearn.model_selection import train_test_split
from id3 import Id3Estimator
from id3 import export_graphviz


df = pd.read_csv('C:\\Users\marco\Desktop\Semestre Final 2020\Introduccion al Aprendizaje Automatico\FuelConsuption_DT.csv')
df.head()
X = df[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_CITY','FUELCONSUMPTION_HWY','FUELCONSUMPTION_COMB','FUELCONSUMPTION_COMB_MPG',]] .values  
X[0:5]
y = df['CETIFIED'].values
y[0:5]

#Split data
X_trainset, X_testset, y_trainset, y_testset = train_test_split(X, y, test_size=0.3, random_state=3)

#Entrenar mdelo
irisTree = Id3Estimator()
irisTree

#predercir
irisTree.fit(X_trainset,y_trainset)
predTree = irisTree.predict(X_testset)

print (predTree [0:5])
print (y_testset [0:5])

#Evaluate
print("DecisionTrees's Accuracy: ", metrics.accuracy_score(y_testset, predTree))

#Visualizing tree
featureNames = df.columns[0:4]
export_graphviz(irisTree.tree_, 'iris.dot',featureNames)

#En una cmd ejecutar dot -Tpdf iris.dot -o iris.pdf