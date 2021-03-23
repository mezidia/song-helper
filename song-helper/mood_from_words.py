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

class PredictMood():
    def __init__(self):
        self.nlp = spacy.load(Consts.LANGUAGE_PACKAGE)
        self.df = pd.read_csv(Consts.PATH_TO_CSV)

        # Vectorization
        self.classifier = LinearSVC(dual=False)

        # Features and Labels
        self.X = self.df[str(self.df.columns[0])]
        self.ylabels = self.df[str(self.df.columns[1])]

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.ylabels, test_size=Consts.TEST_SIZE, random_state=Consts.RAND_STATE)

            # Create the  pipeline to clean, tokenize, vectorize, and classify
        self.pipe_tfid = Pipeline([(Consts.CLEANER, Predictors()),
                            (Consts.VECTORIZER, TfidfVectorizer()),
                            (Consts.CLASSIFIER, self.classifier)])

        self.pipe_tfid.fit(self.X_train, self.y_train)

    def predict(self, user_text: list) -> list:
        return self.pipe_tfid.predict([user_text])

#predictor = PredictMood()
#print(predictor.predict("I want energetic music"))
