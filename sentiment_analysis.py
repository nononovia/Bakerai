#%% 

import os
import json
import gzip
import pandas as pd
from urllib.request import urlopen
import numpy as np
from numpy import loadtxt
# from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import svm 
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.ensemble import AdaBoostClassifier
from sklearn.datasets import make_classification
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score, KFold
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
#%%  
def parse(path):
  g = gzip.open(path, 'rb')
  for l in g:
    yield json.loads(l)

def getDF(path):
  i = 0
  df = {}
  for d in parse(path):
    df[i] = d
    i += 1
  return pd.DataFrame.from_dict(df, orient='index')


df = getDF('./data/Grocery_and_Gourmet_Food_5.json.gz')

#%% 
dg = df[['overall','reviewText']]
# %%
df.isnull().sum()
# %%
dg.dropna(inplace=True)


dg.dropna(axis=0, how = 'any', inplace=True)


dg.loc[dg['overall'] > 3.0, 'sentiment'] = 1
dg.loc[dg['overall'] < 3.0, 'sentiment'] = 0
dg.head()

#%%
vectorizer = CountVectorizer()
X,y= dg.reviewText, dg.sentiment
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 5000, random_state = 42, train_size = 5000,stratify = y)

X_train_bow, X_test_bow = vectorizer.fit_transform(X_train),vectorizer.transform(X_test)


#%% 

clf = GradientBoostingClassifier(n_estimators=1000, learning_rate=1.0,
    max_depth=1, random_state=0, warm_start=True).fit(X_train_bow, y_train)
clf.score(X_test_bow, y_test)
# %%

test = ["very good "]
pred = clf.predict(vectorizer.fit(test))
print(pred)