# Load Exploratory Data Analysis (EDA) packages
import pandas as pd
# Load NLP and Lemmanization packages
import spacy
# Load string for punctuation
import string
# Load english for parsing
from spacy.lang.en import English
# Machine Learning (ML) packages
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.metrics import accuracy_score
from sklearn.base import TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
# Splitting Data Set
from sklearn.model_selection import train_test_split
from mood_predictors import Predictors


#class PredictMood():
nlp = spacy.load('en_core_web_trf')

df = pd.read_csv('song-helper\docs\OurData.csv')

parser = English()

def spacy_tokenizer(self, sentence):
    mytokens = parser(sentence)
    mytokens = [ word.lemma_.lower().strip() if word.lemma_ != "-PRON-" else word.lower_ for word in mytokens ]
    return mytokens

# Vectorization
vectorizer = CountVectorizer(tokenizer = spacy_tokenizer, ngram_range=(1,1))
classifier = LinearSVC(dual=False)

# Using Tfidf
tfvectorizer = TfidfVectorizer()

# Features and Labels
X = df['Utterance']
ylabels = df['Emotion']

X_train, X_test, y_train, y_test = train_test_split(X, ylabels, test_size=0.2, random_state=42)

#### Using Tfid
# Create the  pipeline to clean, tokenize, vectorize, and classify
pipe_tfid = Pipeline([("cleaner", Predictors()),
                    ('vectorizer', tfvectorizer),
                    ('classifier', classifier)])

pipe_tfid.fit(X_train,y_train)

sample_prediction1 = pipe_tfid.predict(X_test)

# Prediction Results
for (sample, pred) in zip(X_test,sample_prediction1):
    print(sample,"Prediction=>", pred)

# Accuracy
print("Accuracy: ",pipe_tfid.score(X_test,y_test))
print("Accuracy: ",pipe_tfid.score(X_test,sample_prediction1))
print("Accuracy: ",pipe_tfid.score(X_train,y_train))

print()

example = ["I do enjoy my job",
        "What a poor product!,I will have to get a new one",
        "I feel amazing!"]

print(pipe_tfid.predict(example))

print()

example2 = ["I want some happy music"]

print(pipe_tfid.predict(example2))
