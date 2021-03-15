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
# Splitting Data Set
from sklearn.model_selection import train_test_split
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
    mytokens = [ word for word in mytokens if word not in stopWords and word not in punctuations ]
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

# Vectorization
vectorizer = CountVectorizer(tokenizer = spacy_tokenizer, ngram_range=(1,1))
classifier = LinearSVC()

# Using Tfidf
tfvectorizer = TfidfVectorizer(tokenizer = spacy_tokenizer)

# Features and Labels
X = df['Utterance']
ylabels = df['Emotion']

X_train, X_test, y_train, y_test = train_test_split(X, ylabels, test_size=0.2, random_state=42)

# Create the pipeline to clean, tokenize, vectorize, and classify
pipe = Pipeline([("cleaner", predictors()),
                ('vectorizer', vectorizer),
                ('classifier', classifier)])

# Fit our data
pipe.fit(X_train,y_train)

# Predicting with a test dataset
sample_prediction = pipe.predict(X_test)

# Prediction Results
for (sample,pred) in zip(X_test,sample_prediction):
    print(sample,"Prediction=>",pred)
