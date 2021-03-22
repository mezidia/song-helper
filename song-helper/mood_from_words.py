# Load Exploratory Data Analysis (EDA) packages
import pandas as pd
# Load NLP and Lemmanization packages
import spacy
# Machine Learning (ML) packages
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
# Splitting Data Set
from sklearn.model_selection import train_test_split
from mood_predictors import Predictors

class Consts:
    LANGUAGE_PACKAGE = 'en_core_web_trf'
    PATH_TO_CSV = 'song-helper\song-helper\data\OurData.csv'
    ACCURACY = "Accuracy: "
    PREDICTION = "Prediction=>"
    TEST_SIZE = 0.2
    RAND_STATE = 42
    CLEANER = "cleaner"
    VECTORIZER = 'vectorizer'
    CLASSIFIER = 'classifier'

#class PredictMood():
nlp = spacy.load(Consts.LANGUAGE_PACKAGE)

df = pd.read_csv(Consts.PATH_TO_CSV)

# Vectorization
classifier = LinearSVC(dual=False)

# Features and Labels
X = df[str(df.columns[0])]
ylabels = df[str(df.columns[1])]

X_train, X_test, y_train, y_test = train_test_split(X, ylabels, test_size=Consts.TEST_SIZE, random_state=Consts.RAND_STATE)

# Create the  pipeline to clean, tokenize, vectorize, and classify
pipe_tfid = Pipeline([(Consts.CLEANER, Predictors()),
                    (Consts.VECTORIZER, TfidfVectorizer()),
                    (Consts.CLASSIFIER, classifier)])

pipe_tfid.fit(X_train,y_train)

sample_prediction1 = pipe_tfid.predict(X_test)

# Prediction Results
for (sample, pred) in zip(X_test, sample_prediction1):
    print(sample, Consts.PREDICTION, pred)

# Accuracy
print(Consts.ACCURACY, pipe_tfid.score(X_test,y_test))
print(Consts.ACCURACY, pipe_tfid.score(X_test,sample_prediction1))
print(Consts.ACCURACY, pipe_tfid.score(X_train,y_train))
