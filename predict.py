from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing
import joblib
import pickle
import string
import scipy
from sentence_transformers import SentenceTransformer
#from textblob import TextBlob

import numpy as np
import pandas as pd

df_train = pd.read_csv('dataset/Training.csv', delimiter=',')
df_test = pd.read_csv('dataset/Testing.csv', delimiter=',')
vocab = df_train.columns.tolist()[:-1]

label = preprocessing.LabelEncoder()
label.fit(pd.concat([df_train['prognosis'], df_test['prognosis']]))
labels = label.fit_transform(df_train['prognosis'])

le_name_mapping = dict(zip(label.classes_, label.transform(label.classes_)))


model = joblib.load('models/model.pkl')

model_cardio = joblib.load('cardio.sav')

model_kidney = joblib.load('models/kidney.sav')
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

def cardio_predict(features):
  df = pd.read_csv('dataset/cardio_train.csv', delimiter=';')
  df = df.drop('id',axis = 1)
  X = df[df.columns.difference(['cardio'])]
  y = df['cardio']
  vocab = X.columns.tolist()[:]
  y_test_in = pd.DataFrame(features, vocab)
  X_eval = y_test_in.T
  
  y_eval = model_cardio.predict(X_eval)
  return y_eval

def kidney_predict(features):
  df2 = pd.read_csv('dataset/kidney.csv')

  X = df2[df2.columns.difference(['class'])]
  y = df2['class']
  X = X.drop('Unnamed: 0',axis = 1)
  vocab = X.columns.tolist()[:]
  print(vocab)
  y_test_in = pd.DataFrame(features, vocab)
  X_eval = y_test_in.T
  
  y_eval = model_kidney.predict(X_eval)
  return y_eval

def pre_processing(question):
    def lemmatize_with_pos_tag(sentence):
        tokenized_sentence = TextBlob(sentence)
        tag_dict = {"J": 'a', "N": 'n', "V": 'v', "R": 'r'}
        words_and_tags = [(word, tag_dict.get(pos[0], 'n')) for word, pos in tokenized_sentence.tags]
        lemmatized_list = [wd.lemmatize(tag) for wd, tag in words_and_tags]
        return " ".join(lemmatized_list)
    question = question.lower()
    question = question.replace('[','')
    question = question.replace(']','')
    question.translate(str.maketrans(" ", " ", string.punctuation))
    #question = lemmatize_with_pos_tag(question)
    return question
  
def bert_disease_predict(query):
  
  model_bert = SentenceTransformer('model')
  with open('models/sentence_encoder_symp', 'rb') as f:
    sentence_embeddings = pickle.load(f)
  with open('models/symp.pkl', 'rb') as f:
    symps = pickle.load(f)
  queries = pre_processing(query)
  query_embeddings = model_bert.encode([queries])

  for query, query_embedding in zip(queries, query_embeddings):
    distances = scipy.spatial.distance.cdist([query_embedding], sentence_embeddings, "cosine")[0]
    results = zip(range(len(distances)), distances)
    results = sorted(results, key=lambda x: x[1])
  return results
    