import numpy as np 
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
import matplotlib.pyplot as plt
from six import StringIO
#from sklearn.externals.six import StringIO
import pydotplus
import matplotlib.image as mpimg
from sklearn import tree

df = pd.read_csv('C:\\Users\marco\Desktop\Semestre Final 2020\Introduccion al Aprendizaje Automatico\\iris.csv')
df.head()
X = df[['sepal_length','sepal_width','petal_length','petal_width']] .values  
X[0:5]
y = df['species'].values
y[0:5]

#Split data
X_trainset, X_testset, y_trainset, y_testset = train_test_split(X, y, test_size=0.3, random_state=3)

#Entrenar mdelo
irisTree = DecisionTreeClassifier(criterion="entropy", max_depth = 4)
irisTree

#predercir
irisTree.fit(X_trainset,y_trainset)
predTree = irisTree.predict(X_testset)

print (predTree [0:5])
print (y_testset [0:5])

#Evaluate
print("DecisionTrees's Accuracy: ", metrics.accuracy_score(y_testset, predTree))

#Visualizing tree
#dot_data = StringIO()
#filename = "iris.png"
#featureNames = df.columns[0:4]
#targetNames = df["species"].unique().tolist()
#out=tree.export_graphviz(irisTree,feature_names=featureNames, out_file=dot_data, class_names= np.unique(y_trainset), filled=True,  special_characters=True,rotate=False)  
#graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
#graph.write_png(filename)
#img = mpimg.imread(filename)
#plt.figure(figsize=(100, 200))
#plt.imshow(img,interpolation='nearest')