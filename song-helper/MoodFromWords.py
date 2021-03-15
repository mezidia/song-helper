# for creating dataframe
import pandas as pd
import spacy as sp
from spacy.lang.en.stop_words import STOP_WORDS
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
#print(df)

# Checking for missing values
#print(df.isnull().sum())

# Build a list of stopwords to use to filter
stopWords = list(STOP_WORDS)

# There You should read input
docx = nlp("This is how John Walker was walking. He was also running beside the lawn.")

print("\nLemmatizing of tokens:\n")

# Lemmatizing of tokens
for word in docx:
    print(word.text,"Lemma =>",word.lemma_)

print("\nLemma that are not pronouns:\n")

# Lemma that are not pronouns
for word in docx:
    if word.lemma_ != "-PRON-":
        print(word.lemma_.lower().strip())

