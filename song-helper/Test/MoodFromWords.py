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

# Load our dataset
df_yelp = pd.read_table('song-helper/song-helper/Test/yelp_labelled.txt')
df_amz = pd.read_table('song-helper/song-helper/Test/amazon_cells_labelled.txt')
df_imdb = pd.read_table('song-helper/song-helper/Test/imdb_labelled.txt')

# Concatenate our Datasets
frames = [df_yelp,df_imdb,df_amz]

# Renaming Column Headers
for colname in frames:
    colname.columns = ["Message","Target"]

# Column names
for colname in frames:
    print(colname.columns)

# Assign a Key to Make it Easier
keys = ['Yelp','IMDB','Amazon']

# Merge or Concat our Datasets
df = pd.concat(frames,keys=keys)

# Length and Shape
df.shape

df.head()

df.to_csv("sentimentdataset.csv")

# Data Cleaning
df.columns

# Checking for Missing Values
df.isnull().sum()

nlp = spacy.load('en_core_web_trf')

parser = English()

def spacy_tokenizer(sentence):
    mytokens = parser(sentence)
    mytokens = [ word.lemma_.lower().strip() if word.lemma_ != "-PRON-" else word.lower_ for word in mytokens ]
    return mytokens

#Custom transformer using spaCy
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
classifier = LinearSVC(dual=False)

# Using Tfidf
tfvectorizer = TfidfVectorizer()

# Features and Labels
X = df['Message']
ylabels = df['Target']

X_train, X_test, y_train, y_test = train_test_split(X, ylabels, test_size=0.2, random_state=42)

# Create the  pipeline to clean, tokenize, vectorize, and classify
pipe = Pipeline([("cleaner", predictors()),
                ('vectorizer', vectorizer),
                ('classifier', classifier)])

# Fit our data
pipe.fit(X_train,y_train)

# Predicting with a test dataset
sample_prediction = pipe.predict(X_test)

# Prediction Results
# 1 = Positive review
# 0 = Negative review
for (sample,pred) in zip(X_test,sample_prediction):
    print(sample,"Prediction=>",pred)

# Accuracy
print("Accuracy: ",pipe.score(X_test,y_test))
print("Accuracy: ",pipe.score(X_test,sample_prediction))

# Accuracy
print("Accuracy: ",pipe.score(X_train,y_train))

# Another random review
pipe.predict(["This was a great movie"])

example = ["I do enjoy my job",
        "What a poor product!,I will have to get a new one",
        "I feel amazing!"]

pipe.predict(example)

#### Using Tfid
# Create the  pipeline to clean, tokenize, vectorize, and classify
pipe_tfid = Pipeline([("cleaner", predictors()),
                    ('vectorizer', tfvectorizer),
                    ('classifier', classifier)])

pipe_tfid.fit(X_train,y_train)

sample_prediction1 = pipe_tfid.predict(X_test)

for (sample,pred) in zip(X_test,sample_prediction1):
    print(sample,"Prediction=>", pred)

print("Accuracy: ",pipe_tfid.score(X_test,y_test))
print("Accuracy: ",pipe_tfid.score(X_test,sample_prediction1))

pipe_tfid.predict(example)
