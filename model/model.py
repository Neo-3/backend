import pandas as pd
import numpy as np
from sklearn import ensemble
from sklearn.ensemble import RandomForestClassifier
import pickle


df = pd.read_csv("imageDataSet.csv")

from sklearn.model_selection import train_test_split, cross_val_score

df1=df.drop("Target",axis=1)
y=df["Target"]
X_train, X_test, y_train, y_test = train_test_split(df1, y, test_size=0.30, random_state=42)

model2 = ensemble.RandomForestClassifier(criterion='gini', max_depth=None, max_features='sqrt', max_leaf_nodes=None, min_samples_leaf=1, min_samples_split=2, n_estimators=150)
model2.fit(X_train, y_train)

pickle.dump(model2, open('model.pkl','wb'))