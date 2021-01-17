import pandas as pd
import numpy as np
import math

df = pd.read_csv(r"C:\Users\Marco Hernandez\Desktop\FuelConsumption.csv")
df["ONES"] = 1
msk = np.random.rand(len(df)) <0.5
train = df[msk]
test = df[~msk]
train_x = np.asanyarray(train[["ONES",'ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB']])
train_y = np.asanyarray(train[['CO2EMISSIONS']])
theta = np.matmul(np.matmul(np.linalg.inv(np.matmul(train_x.T,train_x)),train_x.T),train_y)
ThetaT = theta.T
y = np.matmul(theta.T,train_x)
print(theta)
print(y)
print(ThetaT)