import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from keras.wrappers.scikit_learn import KerasClassifier

from .utils import SpotifyUtils
from .model import base_model

sp_utils = SpotifyUtils()


class PredictMood:
    @staticmethod
    def prepare_data(data: list) -> list:
        """
        Prepare data from custom to NumPy
        :param data: some song features
        :return: song features without keys
        """
        result = []
        for element in data:
            result.append(element[1])
        return result

    @staticmethod
    def prepare_artists(string: str) -> str:
        """
        Prepare string from custom to readable
        :param string: custom artists string
        :return: string without elements of lists
        """
        result = ''
        bad_chars = ['"', '[', ']']
        for char in string:
            if char not in bad_chars:
                result += char
            else:
                continue
        return result

    def predict_mood(self, id_song: str, path: str) -> str:
        """
        Main function to predict the mood
        :param id_song: id of song from Spotify
        :param path: path to dataset
        :return: string with name of song and it mood
        """
        df = pd.read_csv(path)
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
        preds = sp_utils.get_song(id_song)
        # Pre-process the features to input the Model
        preds_features = np.array(self.prepare_data(preds[6:-2])).reshape(-1, 1).T

        # Predict the features of the song
        results = pip.predict(preds_features)

        mood = np.array(target['mood'][target['encode'] == int(results)])
        name_song = preds[0][1]
        artist = self.prepare_artists(preds[2][1])

        return "{0} by {1} is a {2} song".format(name_song, artist, mood[0].upper())
        # print(f"{name_song} by {artist} is a {mood[0].upper()} song")

# obj = PredictMood()
# obj.predict_mood('4Km5HrUvYTaSUfiSGPJeQR', 'data/data_moods.csv')
