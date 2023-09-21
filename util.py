import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.tree import DecisionTreeClassifier as dtc
from sklearn.naive_bayes import MultinomialNB as mnb
from sklearn.ensemble import RandomForestClassifier as rfc
from sklearn.ensemble import GradientBoostingClassifier as gbc
from sklearn.svm import SVC as svc

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

class test:

    def __init__(self, path):
        data = pd.read_csv(path)
        col = data.columns
        col = col[:-2]
        self.x = data[col]
        self.y = data['prognosis']

    def train(self):
        self.clf = mnb()
        self.clf.fit(self.x, self.y)

    def valid(self, path):
        data = pd.read_csv(path)
        col = data.columns
        col = col[:-1]
        self.xtest = data[col]
        self.ytest = data['prognosis']
        pred = self.clf.predict(self.xtest)
        accuracy = accuracy_score(self.ytest, pred)
        print("Accuracy of the model: ", accuracy)

    def predict_test(self, test1):
        res = self.clf.predict(test1)
        return res[0]
