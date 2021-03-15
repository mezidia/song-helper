# for creating dataframe
import pandas as pd
import spacy as sp
from spacy.lang.en.stop_words import STOP_WORDS
# Creating a Spacy Parser
from spacy.lang.en import English
# ML Packages
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.metrics import accuracy_score
from sklearn.base import TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
# Use the punctuations of string module
import string

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

# List Comprehensions of our Lemma
[word.lemma_.lower().strip() if word.lemma_ != "-PRON-" else word.lower_ for word in docx]

# Filtering out Stopwords and Punctuations
for word in docx:
    if word.is_stop == False and not word.is_punct:
#     if word.is_stop != True and not word.is_punct:
        print(word)

# Stop words and Punctuation In List Comprehension
[ word for word in docx if word.is_stop == False and not word.is_punct ]

punctuations = string.punctuation

parser = English()

def spacy_tokenizer(sentence):
    mytokens = parser(sentence)
    mytokens = [ word.lemma_.lower().strip() if word.lemma_ != "-PRON-" else word.lower_ for word in mytokens ]
    mytokens = [ word for word in mytokens if word not in stopwords and word not in punctuations ]
    return mytokens

# Custom transformer using spaCy
class predictors(TransformerMixin):
    def transform(self, X, **transform_params):
        return [clean_text(text) for text in X]
    def fit(self, X, y=None, **fit_params):
        return self
    def get_params(self, deep=True):
        return {}

# Basic function to clean the text
def clean_text(text):
    return text.strip().lower()
