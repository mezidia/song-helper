# for creating dataframe
import pandas as pd
import spacy as sp
# ML Packages
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.metrics import accuracy_score
from sklearn.base import TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC

# Load the spacy model that you have installed
nlp = sp.load('en_core_web_md')

filepath = {'emorynlp_train_final.csv'}

df=pd.read_csv('docs\MELD-dataset\data\emorynlp\emorynlp_train_final.csv',usecols=['Utterance', 'Emotion'])
print(df)
