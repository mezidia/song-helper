# Custom transformer using spaCy
from sklearn.base import TransformerMixin
from sklearn.pipeline import Pipeline
from words_preprocessor import WordPreprocessor


class Predictors(TransformerMixin):
    """
    Class which used in pipe
    """

    def transform(self, X: list, **transform_params: dict) -> list:
        return [WordPreprocessor().clean_text(text) for text in X]

    def fit(self, X: list, y=None, **fit_params: dict) -> Pipeline:
        return self
