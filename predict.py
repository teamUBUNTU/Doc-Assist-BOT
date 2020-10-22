from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing
import joblib

import numpy as np
import pandas as pd

df_train = pd.read_csv('dataset/Training.csv', delimiter=',')
df_test = pd.read_csv('dataset/Testing.csv', delimiter=',')
vocab = df_train.columns.tolist()[:-1]

label = preprocessing.LabelEncoder()
label.fit(pd.concat([df_train['prognosis'], df_test['prognosis']]))
labels = label.fit_transform(df_train['prognosis'])

le_name_mapping = dict(zip(label.classes_, label.transform(label.classes_)))


model = joblib.load('model.sav')

def predictor(final_symptoms):
  y_test = np.zeros(132)
  for final_symptom in final_symptoms:
      y_test[vocab.index(final_symptom)] = 1
      
  y_test_in = pd.DataFrame(y_test, vocab).T
  y_pred = model.predict(y_test_in)
  diseases = []
  for disease, code in le_name_mapping.items():
    if code == y_pred:
      diseases.append(disease)
  
  return diseases