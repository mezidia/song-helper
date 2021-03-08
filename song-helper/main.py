import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from keras.wrappers.scikit_learn import KerasClassifier

from .utils import get_songs_features
from .model import base_model


def predict_mood(id_song):
    df = pd.read_csv('data/data_moods.csv')
    col_features = df.columns[6:-3]
    X2 = np.array(df[col_features])
    Y = df['mood']
    # Encodethe categories
    encoder = LabelEncoder()
    encoder.fit(Y)
    encoded_y = encoder.transform(Y)
    target = pd.DataFrame({'mood': df['mood'].tolist(), 'encode': encoded_y}).drop_duplicates().sort_values(['encode'],
                                                                                                            ascending=True)
    # Join the model and the scaler in a Pipeline
    pip = Pipeline([('minmaxscaler', MinMaxScaler()), ('keras', KerasClassifier(build_fn=base_model, epochs=300,
                                                                                batch_size=200, verbose=0))])
    # Fit the Pipeline
    pip.fit(X2, encoded_y)

    # Obtain the features of the song
    preds = get_songs_features(id_song)
    # Pre-process the features to input the Model
    preds_features = np.array(preds[0][6:-2]).reshape(-1, 1).T

    # Predict the features of the song
    results = pip.predict(preds_features)

    mood = np.array(target['mood'][target['encode'] == int(results)])
    name_song = preds[0][0]
    artist = preds[0][2]

    return print("{0} by {1} is a {2} song".format(name_song, artist, mood[0].upper()))
    # print(f"{name_song} by {artist} is a {mood[0].upper()} song")
