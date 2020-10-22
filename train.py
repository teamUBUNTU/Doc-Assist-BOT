import numpy as np
import pandas as pd

from sklearn import preprocessing
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

import joblib

df_train = pd.read_csv('dataset/Training.csv', delimiter=',')
df_test = pd.read_csv('dataset/Testing.csv', delimiter=',')
nRow, nCol = df_train.shape

label = preprocessing.LabelEncoder()
label.fit(pd.concat([df_train['prognosis'], df_test['prognosis']]))
labels = label.fit_transform(df_train['prognosis'])
symptoms = df_train[df_train.columns.difference(['prognosis'])]

model = RandomForestClassifier()
model.fit(symptoms, labels)
joblib.dump(model, 'model.sav')
