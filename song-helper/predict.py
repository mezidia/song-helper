import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from keras.wrappers.scikit_learn import KerasClassifier

from .utils import SpotifyUtils
from .model import make_model

sp_utils = SpotifyUtils()


class PredictMood:
    """
    Class with the predicting the mood method
    """

    @staticmethod
    def prepare_data(song_features: list) -> list:
        """
        Prepare data from custom to NumPy
        :param song_features: some song features
        :return: song features without keys
        """
        main_song_features = []
        for element in song_features:
            main_song_features.append(element[1])
        return main_song_features

    @staticmethod
    def prepare_artists(artists_string: str) -> str:
        """
        Prepare string from custom to readable
        :param artists_string: custom artists string
        :return: string without elements of lists
        """
        readable_string = ''
        bad_chars = ['"', '[', ']']
        for char in artists_string:
            if char not in bad_chars:
                readable_string += char
            else:
                continue
        return readable_string

    def predict_mood(self, id_song: str, path: str) -> dict:
        """
        Main function to predict the mood
        :param id_song: id of song from Spotify
        :param path: path to dataset
        :return: dictionary with name of song, artists and it mood
        """
        # Read song_features
        csv_data = pd.read_csv(path)
        # Define the features and the target
        col_features = csv_data.columns[6:-3]
        x_points = np.array(csv_data[col_features])
        y_points = csv_data['mood']
        # Encode the labels (targets)
        encoder = LabelEncoder()
        encoder.fit(y_points)
        encoded_y = encoder.transform(y_points)
        target = pd.DataFrame({'mood': csv_data['mood'].tolist(), 'encode': encoded_y}).drop_duplicates().sort_values(
            ['encode'],
            ascending=True)
        # Join the model and the scaler in a Pipeline
        pip = Pipeline([('minmaxscaler', MinMaxScaler()), ('keras', KerasClassifier(build_fn=make_model, epochs=300,
                                                                                    batch_size=200, verbose=0))])
        pip.fit(x_points, encoded_y)
        # Obtain the features of the song
        features = sp_utils.get_song(id_song)
        # Pre-process the features to input the Model
        process_features = np.array(self.prepare_data(features[6:-2])).reshape(-1, 1).T
        results = pip.predict(process_features)
        mood = np.array(target['mood'][target['encode'] == int(results)])
        name_song = features[0][1]
        artist = self.prepare_artists(features[2][1])
        return {
            'name': name_song,
            'artists': artist,
            'mood': mood[0],
        }
        # "{0} by {1} is a {2} song".format(name_song, artist, mood[0].upper())

# obj = PredictMood()
# obj.predict_mood('4Km5HrUvYTaSUfiSGPJeQR', 'data/data_moods.csv')
