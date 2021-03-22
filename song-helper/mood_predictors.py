#Custom transformer using spaCy
from sklearn.base import TransformerMixin
from words_preprocessor import WordPreprocessor

class Predictors(TransformerMixin):
    """[summary]

    Args:
        TransformerMixin ([type]): [description]
    """

    def transform(self, X, **transform_params):
        return [WordPreprocessor().clean_text(text) for text in X]

    def fit(self, X, y=None, **fit_params):
        return self

    def get_params(self, deep=True):
        return {}
