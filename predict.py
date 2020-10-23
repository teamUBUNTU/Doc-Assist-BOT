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


model = joblib.load('model.pkl')


def predictor(final_symptoms):
  y_test = np.zeros(132)
  for final_symptom in final_symptoms:
      y_test[vocab.index(final_symptom)] = 1
      
  y_test_in = pd.DataFrame(y_test, vocab).T
  #y_pred = model.predict(y_test_in)
  
  ######
  p = model.predict_log_proba(y_test_in)
  n = 5 #Top n results
  top_n = np.argsort(p)[:,:-n-1:-1] # Output Labels
  y_pred = np.sort(p)[:,:-n-1:-1]
  ######
  diseases = []
  for disease, code in le_name_mapping.items():
    for top in top_n[0]:
      if code == top:
        diseases.append(disease)
  
  return diseases