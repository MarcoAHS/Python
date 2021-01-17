import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter
import pandas as pd
import numpy as np
import matplotlib.ticker as ticker
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

df = pd.read_csv('C:\\Users\marco\Desktop\Semestre Final 2020\Introduccion al Aprendizaje Automatico\\loan_approval.csv')
df.head()
X = df[['LoanAmount','Credit_History','Property_Area_N']] .values  
X[0:5]
y = df['Loan_Status'].values
y[0:5]

#Normalizacion
X = preprocessing.StandardScaler().fit(X).transform(X.astype(float))
X[0:5]

#Split data
X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.2, random_state=4)
print ('Train set:', X_train.shape,  y_train.shape)
print ('Test set:', X_test.shape,  y_test.shape)

#Select K
k = 4
#Train Model 
neigh = KNeighborsClassifier(n_neighbors = k).fit(X_train,y_train)
neigh

#predict
yhat = neigh.predict(X_test)
yhat[0:5]

#Evaluar con jaccard
print("Train set Accuracy: ", metrics.accuracy_score(y_train, neigh.predict(X_train)))
print("Test set Accuracy: ", metrics.accuracy_score(y_test, yhat))

