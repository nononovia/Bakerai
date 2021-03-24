# %%

import os
import json
import gzip
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score, KFold
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
# %%


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

dg = df[['overall', 'reviewText']]
dg

df.isnull().sum()
dg.dropna(inplace=True)


dg.loc[dg['overall'] > 3.0, 'sentiment'] = 1
dg.loc[dg['overall'] < 3.0, 'sentiment'] = 0
dg.head()

dg.dropna(axis=0, how='any', inplace=True)
dg['reviewText'] = dg['reviewText'].map(lambda x: x.lower())


g = dg.groupby('sentiment')
dg = pd.DataFrame(g.apply(lambda x: x.sample(
    g.size().min()).reset_index(drop=True)))

# %%
vectorizer = CountVectorizer()
X = [x for x in dg['reviewText']]
y = [x for x in dg['sentiment']]
print(X[0])
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=500, random_state=42, train_size=5000, stratify=y)
print(y_train)


X_train_bow, X_test_bow = vectorizer.fit_transform(
    X_train), vectorizer.transform(X_test)


# %%

clf = RandomForestClassifier(random_state=0)
clf.fit(X_train_bow, y_train)
clf.score(X_test_bow, y_test)


# %%
clf = GradientBoostingClassifier(n_estimators=4000, learning_rate=0.5,
                                 max_depth=2, random_state=42, warm_start=True).fit(X_train_bow, y_train)
clf.score(X_test_bow, y_test)
# %%

test = ["very bad product"]
X_test_2 = vectorizer.trans(test)
clf.predict(X_test_2)
# %%
test_set = ['very fun', "bad book do not buy", 'horrible waste of time']
new_test = vectorizer.transform(test_set)

clf.predict(new_test)
