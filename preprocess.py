import nltk
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('stopwords')
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import difflib

import pandas as pd

def word_extractor(sentence):
    tokenizer = RegexpTokenizer(r'\w+')
    tokens =tokenizer.tokenize(sentence)
    tokens=[token.lower() for token in tokens]
    tokens = [token for token in tokens if not token in stopwords.words()]
    return tokens

def symptoms(symptoms):
    final_symptoms = []
    final_symptoms_flat = []
    df_train = pd.read_csv('dataset/Training.csv', delimiter=',')
    vocab = df_train.columns.tolist()
    
    
    for symptom in symptoms:
        final_symptoms.append(difflib.get_close_matches(symptom, vocab, cutoff=0.6))
    for sublist in final_symptoms:
        for item in sublist:
            final_symptoms_flat.append(item)
            
    return set(final_symptoms_flat)

#print(symptoms(word_extractor(input("Describe your symptoms: "))))
#from predict import predictor
#print(predictor(symptoms(word_extractor(input("Describe your symptoms: ")))))