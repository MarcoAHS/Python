import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

k = 5

r = pd.read_csv('C:\\Users\marco\Desktop\Semestre Final 2020\Introduccion al Aprendizaje Automatico\\loan_approval.csv')
r.head()
X = r[['LoanAmount','Credit_History','Property_Area_N']] .values  
Y = r['Loan_Status'].values
X = preprocessing.StandardScaler().fit(X).transform(X.astype(float))
X_tn, X_ts, Y_tn, Y_ts = train_test_split( X, Y, test_size=0.3, random_state=3)
n = KNeighborsClassifier(n_neighbors = k).fit(X_tn,Y_tn)
Y_g = n.predict(X_ts)
Tn_a = metrics.accuracy_score(Y_tn, n.predict(X_tn))
Ts_a = metrics.accuracy_score(Y_ts, Y_g)
print("Train set Accuracy: ", Tn_a)
print("Test set Accuracy: ", Ts_a)
