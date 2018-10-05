import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

cancer = load_breast_cancer()

def answer_one():
	df = pd.DataFrame(cancer.data, columns = cancer['feature_names'])
	df['target'] = pd.Series(cancer.target)
	return df

def answer_two():
	df = answer_one()
	return pd.Series(data = [len(df[df['target'] == 0]) , len(df[df['target'] == 1])], index = ['malignant', 'benign'])
	
def answer_three():
    df = answer_one()
    return (df.iloc[:, :-1], df['target'])

def answer_four():
	X, y = answer_three()
	X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
	return (X_train, X_test, y_train, y_test)

def answer_five():
	X_train, X_test, y_train, y_test = answer_four()
	knn = KNeighborsClassifier(n_neighbors = 1)
	knn.fit(X_train, y_train)
	return knn

def answer_six():
	df = answer_one()
	knn = answer_five()
	means = df.mean()[:-1].values.reshape(1, -1)
	label = knn.predict(means)
	return label

def answer_seven():
	X_train, X_test, y_train, y_test = answer_four()
	knn = answer_five()
	return knn.predict(X_test)

def answer_eight():
    X_train, X_test, y_train, y_test = answer_four()
    knn = answer_five()
    return knn.score(X_test, y_test)

print((answer_eight()))
